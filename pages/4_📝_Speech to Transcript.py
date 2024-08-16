import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

from helping_functions import transcribe

load_dotenv()


client = Groq()

st.set_page_config(page_title="Audio to Text Converter",page_icon="📢",  layout="centered", )

st.title("📢 Audio to Text Converter")
st.header("Upload an audio file")

uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])

if uploaded_file is not None:
    transcription = transcribe(uploaded_file)

    st.markdown("**Transcription:**")
    st.write(transcription.text)
    