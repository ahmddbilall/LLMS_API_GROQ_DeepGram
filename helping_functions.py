import os
from groq import Groq
from dotenv import load_dotenv
import speech_recognition as sr
import pygame
import time
import logging
import pydub
from io import BytesIO
from pydub import AudioSegment
from deepgram import DeepgramClient, SpeakOptions


logging.basicConfig(level=logging.INFO)
FILENAME = "audio.mp3"


load_dotenv()

client = Groq()


def transcribe(audio_file):
    transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3",
            response_format="json",  
            language="en",  
            temperature=0.0  
    )

    return transcription.text



def format_history(history):
    messages = []
    for message in history:
        role = message.get("role", "user")  
        content = message.get("content", "")
        messages.append({"role": role, "content": content})
    return messages



def response(history):
    formatted_history = format_history(history)
    chat_completion = client.chat.completions.create(
        messages=formatted_history,
        model="llama3-8b-8192"
    )
    return chat_completion.choices[0].message.content



def record_audio(file_path, timeout=10, phrase_time_limit=None, retries=3):
    recognizer = sr.Recognizer()
    for attempt in range(retries):
        try:
            with sr.Microphone() as source:
                print("Calibrating for ambient noise...")
                recognizer.adjust_for_ambient_noise(source)
                print("Recording started")
                audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                print("Recording complete")
                
                # Save the audio data as a WAV file
                with open(file_path, "wb") as file:
                    file.write(audio_data.get_wav_data())
                return
        except sr.WaitTimeoutError:
            print(f"Listening timed out, retrying... ({attempt + 1}/{retries})")
        except Exception as e:
            print(f"Failed to record audio: {e}")
            break



def create_audio(TEXT):
    TEXT = {
    "text": TEXT
    }
    try:
        deepgram = DeepgramClient()

        options = SpeakOptions(
            model='aura-arcas-en',
        )

        response = deepgram.speak.v("1").save('audio.mp3', TEXT, options)

    except Exception as e:
        print(f"Exception: {e}")






def play_audio(file_path):


    """
    Play an audio file using pygame.
    
    Args:
    file_path (str): The path to the audio file to play.
    """
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        pygame.mixer.quit()
    except pygame.error as e:
        logging.error(f"Failed to play audio: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred while playing audio: {e}")