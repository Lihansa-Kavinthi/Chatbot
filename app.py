import streamlit as st
from agent import build_agent
from emotion_detector import detect_emotion
from crisis_handler import is_crisis, crisis_message

st.set_page_config(page_title="Mental Health Support", page_icon="💙")
st.title("💙 Mental Health Support Agent")
st.caption("A safe space to talk. I'm here to listen.")

if "chain" not in st.session_state:
    st.session_state.chain = build_agent()
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("How are you feeling today?")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    if is_crisis(user_input):
        response = crisis_message()
    else:
        emotion = detect_emotion(user_input)
        enriched = f"[User emotion detected: {emotion}] {user_input}"
        response = st.session_state.chain.predict(input=enriched)

    st.chat_message("assistant").write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})