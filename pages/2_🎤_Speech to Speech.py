import streamlit as st
from dotenv import load_dotenv
from helping_functions import *

load_dotenv()

st.set_page_config(page_title="Speech to Speech", page_icon="🎙️")

st.title("Speech to Speech")

if 'historyST' not in st.session_state:
    st.session_state.historyST = []

st.markdown(
    """
    <style>
    .stButton > button {
        height: 80px;
        width: 700px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


if st.button("Record"):
    audio_file = record_audio('recorded_audio.wav')
    filename = os.path.join(os.path.dirname(__file__),os.pardir ,"recorded_audio.wav")
    with open(filename,'rb') as file:
        text = transcribe((filename, file.read()))
    st.session_state.historyST.append({"role": "user", "content": text})
    res = response(st.session_state.historyST)
    st.session_state.historyST.append({"role": "assistant", "content": res})
    create_audio(res)
    play_audio('audio.mp3')
    time.sleep(1)


uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "ogg"])

if uploaded_file is not None:
    text = transcribe(uploaded_file)
    st.session_state.historyST.append({"role": "user", "content": text})
    res = response(st.session_state.historyST)
    st.session_state.historyST.append({"role": "assistant", "content": res})
    create_audio(res)
    play_audio('audio.mp3')
    time.sleep(1)