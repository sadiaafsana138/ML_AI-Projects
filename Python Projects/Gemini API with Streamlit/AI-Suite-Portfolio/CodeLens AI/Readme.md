# 🧠 CodeLens AI

🔗 Live Demo: https://codelens-ai.streamlit.app/

> An AI-powered coding assistant that helps you **debug code from images**, get **hints**, or receive **full solutions with explanations** using Google Gemini AI.

---

## 🚀 Overview

**CodeLens AI** is a Streamlit-based smart coding assistant that analyzes uploaded images containing:

- 💻 Code snippets  
- ❌ Error messages  
- 🧾 Debugging screenshots  

It then provides:
- 🔧 Debug explanation  
- 💡 Helpful hints  
- 🧾 Full working solution  

---

## ✨ Features

- 📸 Upload code/error screenshots  
- 🔧 AI-powered debugging  
- 💡 Get step-by-step hints  
- 🧾 Get full corrected solution  
- ⚡ Fast response using Gemini AI  
- 🎯 Simple and interactive UI  

---

## 🛠️ Tech Stack

- Python 🐍  
- Streamlit 🎈  
- Google Generative AI (Gemini) 🤖  
- Pillow (PIL) 🖼️  
- dotenv 🔐  

---

## 📂 Project Structure
```
CodeLens-AI/
│
├── app.py # Streamlit UI
├── api_calling.py # Gemini AI logic (core functionality)
├── requirements.txt # Dependencies
├── .env # API key (not pushed to GitHub)
├── README.md # Documentation
```


---

## ⚙️ How It Works

1. Upload an image containing code or an error
2. Choose an option:
   - 🔧 Debug
   - 💡 Hint
   - 🧾 Solution
3. AI analyzes the image using Gemini
4. Returns structured response

---

## 🧠 AI Modes

### 🔧 Debug Mode
- Finds bugs in code
- Explains errors clearly

### 💡 Hint Mode
- Gives only guidance
- No full solution

### 🧾 Solution Mode
- Provides full corrected code
- Explains fixes step-by-step

---

## 🔐 Environment Variables

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## 📦 Installation

```bash
git clone https://github.com/your-username/CodeLens-AI.git
cd CodeLens-AI
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Requirements

```
streamlit
google-generativeai
python-dotenv
pillow
```


## ⭐ Future Improvements

- 🧠 Multi-language code support (Python, JS, C++)
- 📄 PDF/code file upload
- 🔊 Voice explanation
- 🧑‍🏫 LeetCode-style AI coach mode

---

## 📜 License

This project is for educational purposes.


## 👨‍💻 Author

**Sadia Afsana**
