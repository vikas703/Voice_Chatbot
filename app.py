# Lightweight Streamlit Web App for Vikas Voice Bot
# Features:
# - Simple text input
# - Text + voice response using gTTS
# - Personal Q&A or ChatGPT fallback

import streamlit as st
from gtts import gTTS
import tempfile
import openai
import os
from dotenv import load_dotenv
from responses import responses
from openai import OpenAI

# Load .env variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def speak_to_audio(text):
    tts = gTTS(text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        return fp.name

def match_question_to_response(query):
    # Normalize query: lowercase + remove spaces and dashes
    original_query = query.lower()
    normalized_query = original_query.replace(" ", "").replace("-", "")

    if "life" in original_query or "story" in original_query:
        return responses["life story"]
    elif "superpower" in normalized_query or "strength" in original_query:
        return responses["superpower"]
    elif "grow" in original_query or "growth" in original_query or "improve" in original_query:
        return responses["growth areas"]
    elif "misconception" in original_query or "wrong idea" in original_query or "coworkers" in original_query:
        return responses["misconception"]
    elif "push" in original_query or "limits" in original_query or "boundaries" in original_query:
        return responses["push limits"]
    return None


client = OpenAI()

def ask_chatgpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.set_page_config(page_title="Vikas Voice Bot")
st.title("🗣️ Vikas Voice Bot")

user_input = st.text_input("Ask your question:")

if st.button("Ask"):
    if user_input:
        if user_input.lower() in ["stop", "exit", "quit", "bye"]:
            response = "Goodbye! Have a great day!"
        else:
            response = match_question_to_response(user_input)
            if not response:
                response = ask_chatgpt(user_input)

        st.markdown(f"**Bot:** {response}")
        audio_path = speak_to_audio(response)
        st.audio(audio_path, format="audio/mp3")
    else:
        st.warning("Please enter a question!")