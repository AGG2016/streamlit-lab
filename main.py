from backend.core import run_llm
import streamlit as st
from streamlit_chat import message

st.header("Lumen - Ticket Summarizer Bot")


prompt = st.text_input("Prompt", placeholder="Enter the ticket here..")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if prompt:
    with st.spinner("Generating response.."):
        generated_response = run_llm(
            context=prompt, chat_history=st.session_state["chat_history"]
        )

        formatted_response = (
            generated_response
        )

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append((prompt, generated_response))

if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(user_query, is_user=True)
        message(generated_response)