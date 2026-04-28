# 📚 LearnMate AI

> 🚀 Live App: https://learn-mate-ai.streamlit.app/

LearnMate AI is an AI-powered study assistant that converts images of notes, textbooks, or handwritten content into structured notes, quizzes, and audio summaries using **Google Gemini AI + Streamlit**.

---

## ✨ Features

- 📸 Upload images (notes, textbooks, handwritten pages)
- 🧠 AI-generated structured notes
- 🔊 Text-to-speech audio conversion
- ❓ Automatic MCQ quiz generation
- 🌐 Multi-language support (English / Bangla)
- ⚡ Simple and interactive UI


## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🎈
- Google Generative AI 🤖
- Pillow (PIL) 🖼️
- gTTS 🔊
- python-dotenv 🔐

---

## 📂 Project Structure
LearnMate-AI/
│
├── app.py # Streamlit UI (main app)
├── api_calling.py # Gemini AI logic (notes, quiz, audio)
├── working_image.py # Image processing test module
├── working_audio.py # Text-to-speech test module
│
├── .env # API key (not pushed to GitHub)
├── README.md # Documentation



---

## ⚙️ How It Works

1. Upload images of notes or textbook pages  
2. Select language (English / Bangla)
3. Select difficulty (Easy / Medium / Hard)  
4. Click “Button”  
5. AI generates:
   - 📝 Clean structured notes   
   - 🔊 Audio explanation
   - ❓ MCQ quiz questions 

---

## 📦 Installation (Local Setup)

- bash
- git clone https://github.com/your-username/LearnMate-AI.git
- cd LearnMate-AI
- pip install -r requirements.txt
- streamlit run app.py

## 🔑 Environment Variables
- Create a .env file in the root directory:
- GEMINI_API_KEY=your_api_key_here

## Future Improvements
-📄 PDF support
-🧠 Quiz answer explanations
-📊 Progress tracking system
-🌙 Dark mode UI
-☁️ Cloud storage for notes

## 👨‍💻 Author
-Sadia Afsana
