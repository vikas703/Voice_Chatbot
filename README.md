---
title: Vikas Voice Bot
emoji: 🗣️
colorFrom: indigo
colorTo: purple
sdk: streamlit
sdk_version: "1.28.0"
app_file: app.py
pinned: false
---
# 🗣️ Vikas Voice Bot

A lightweight Streamlit voice assistant that answers questions about **ME** (Vikas) and general questions using **ChatGPT**.

### ✅ Features

- Personal answers for specific questions (like “What’s your superpower?”)
- ChatGPT fallback for general queries (like “Tell me a joke”)
- Clean and easy Streamlit interface
- Tried my best to keep it as simple as possiable, as mentioned in the Project info

---

## 🚀 How to Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/vikas-voice-bot.git
cd vikas-voice-bot
```

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Create a `.env` File

In the project root folder, create a file named `.env` with the following content:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

### 4. Run the App

streamlit run app.py
