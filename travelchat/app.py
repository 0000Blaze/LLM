from openai import OpenAI
import streamlit as st
import dotenv
import os
import json
from utils import query

dotenv.load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)


st.title("💬 Travel Chatbot")
st.caption("Ask me about travelling in Nepal")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    if "This is the prompt start" not in msg["content"] and msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    results = query(prompt, top_k=2)
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "system", "content": "You are a travel bot for Nepal. Provide concise answer to the user queries using the prompt and the results from vector db search."})
    st.session_state.messages.append({"role": "user", "content": f"This is the prompt start {prompt}. prompt ends here. This is json result from vector db search for prompt{json.dumps(results)}"})   
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
