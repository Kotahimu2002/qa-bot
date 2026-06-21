import streamlit as st
from src.query import ask_question

st.title("Document Q&A Bot")

question = st.text_input(
    "Ask a Question"
)

if question:

    answer = ask_question(question)

    st.write(answer)
