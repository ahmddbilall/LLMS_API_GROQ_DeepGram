import os
import streamlit as st
from dotenv import load_dotenv

from helping_functions import *

load_dotenv()



st.set_page_config(page_title="Text to Speech", page_icon="🎙️")

st.title("Text to Speech")

if 'historyTextSpeech' not in st.session_state:
    st.session_state.historyTextSpeech = []


input = st.text_input('Enter your message')

if input:
    st.session_state.historyTextSpeech.append({"role": "user", "content": input})
    
    response_text = response(st.session_state.historyTextSpeech)
    
    st.session_state.historyTextSpeech.append({"role": "assistant", "content": response_text})
    
    create_audio(response_text)
    play_audio('audio.mp3')
    time.sleep(1)