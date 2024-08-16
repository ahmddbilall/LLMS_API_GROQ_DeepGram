import streamlit as st
from groq import Groq
from dotenv import load_dotenv

from helping_functions import response

load_dotenv()

client = Groq()







st.set_page_config(page_title="Text To Text", page_icon="💬", layout="centered")
st.title("🤖 Welcome Back Bilal!")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def translateRole(role):
    return 'user' if role == 'user' else 'assistant'

for message in st.session_state.chat_history:
    role = message.get("role", "user")
    content = message.get("content", "")
    with st.chat_message(translateRole(role)):
        st.markdown(content)

user_question = st.chat_input("Ask a question:")

if user_question:
    st.chat_message('user').markdown(user_question)
    
    st.session_state.chat_history.append({"role": "user", "content": user_question})
    
    response_text = response(st.session_state.chat_history)
    
    st.session_state.chat_history.append({"role": "assistant", "content": response_text})
    
    st.chat_message('assistant').markdown(response_text)
