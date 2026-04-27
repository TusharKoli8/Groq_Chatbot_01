import streamlit as st
from llm import get_response

st.set_page_config(page_title="AI Chatbot")

st.title("Chat with your AI Assistant ")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            try:
                response = get_response(st.session_state.messages)
            except Exception as e:
                response = f"Error: {str(e)}"

            st.markdown(response)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    