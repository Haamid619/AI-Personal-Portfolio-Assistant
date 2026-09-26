import streamlit as st

from rag import generate_answer


# Page configuration
st.set_page_config(
    page_title="Haamid AI Portfolio Assistant",
    page_icon="🤖",
    layout="centered"
)


# Title
st.title("🤖 AI Personal Portfolio Assistant")

st.write(
    "Ask me anything about Syed Haamid Ali's "
    "education, skills, projects, and experience."
)


# Chat input
question = st.chat_input(
    "Ask something about my portfolio..."
)


# Generate answer
if question:

    # Display user question
    with st.chat_message("user"):
        st.write(question)

    # Display AI response
    with st.chat_message("assistant"):

        with st.spinner("Searching portfolio..."):

            answer = generate_answer(question)

        st.write(answer)
        