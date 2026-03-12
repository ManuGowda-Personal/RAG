import streamlit as st
from query import ask_question

st.set_page_config(page_title="HR Assistant", page_icon="🤖")

st.title("🤖 HR Policy Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask a question about HR policy")

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    answer = ask_question(question)

    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )