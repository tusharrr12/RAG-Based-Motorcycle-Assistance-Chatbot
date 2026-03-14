import streamlit as st
import requests

st.set_page_config(page_title="Bike Assistance AI", page_icon=" ")

st.title("RAG-Based Motorcycle Assistance Chatbot")

st.write("Ask any motorcycle troubleshooting question using service manuals.")

API_URL = "http://127.0.0.1:8000/ask"

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# user input
prompt = st.chat_input("Ask about your bike problem...")

if prompt:

    # show user message
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    try:
        response = requests.post(
            API_URL,
            json={"question": prompt}
        )

        data = response.json()

        answer = data["answer"]

        sources = data.get("sources", [])

        reply = answer

        if sources:
            reply += "\n\n**Sources:**\n"
            for s in sources:
                reply += f"- {s}\n"

    except Exception as e:
        reply = f"Error connecting to API: {e}"

    # show assistant message
    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })