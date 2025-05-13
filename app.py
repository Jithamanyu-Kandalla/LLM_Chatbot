import streamlit as st
from engine import ChatbotEngine

st.title("LLM-Powered NLP Chatbot with Hugging Face")

bot = ChatbotEngine()

user_input = st.text_area("Enter your message:")
if st.button("Generate Response"):
    response = bot.chat(user_input)
    st.write(response)
