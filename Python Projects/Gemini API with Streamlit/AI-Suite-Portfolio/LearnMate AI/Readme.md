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
├── app.py
├── api_calling.py
├── working_image.py
├── working_audio.py
│
├── requirements.txt
├── .env
├── README.md


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

 bash
- git clone https://github.com/your-username/LearnMate-AI.git
- cd LearnMate-AI
- pip install -r requirements.txt
- streamlit run app.py

## 🔑 Environment Variables
- Create a .env file in the root directory:
- GEMINI_API_KEY=your_api_key_here


## Requirements

altair==6.0.0
annotated-types==0.7.0
anyio==4.13.0
attrs==26.1.0
blinker==1.9.0
cachetools==7.0.5
certifi==2026.2.25
cffi==2.0.0
charset-normalizer==3.4.7
click==8.1.8
colorama==0.4.6
cryptography==46.0.7
distro==1.9.0
gitdb==4.0.12
GitPython==3.1.46
google-auth==2.49.2
google-genai==1.72.0
gTTS==2.5.4
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.11
Jinja2==3.1.6
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
MarkupSafe==3.0.3
narwhals==2.19.0
numpy==2.4.4
packaging==26.0
pandas==3.0.2
pillow==12.2.0
protobuf==7.34.1
pyarrow==23.0.1
pyasn1==0.6.3
pyasn1_modules==0.4.2
pycparser==3.0
pydantic==2.12.5
pydantic_core==2.41.5
pydeck==0.9.1
python-dateutil==2.9.0.post0
python-dotenv==1.2.2
referencing==0.37.0
requests==2.33.1
rpds-py==0.30.0
six==1.17.0
smmap==5.0.3
sniffio==1.3.1
streamlit==1.56.0
tenacity==9.1.4
toml==0.10.2
tornado==6.5.5
typing-inspection==0.4.2
typing_extensions==4.15.0
tzdata==2026.1
urllib3==2.6.3
watchdog==6.0.0
websockets==16.0

## Future Improvements
📄 PDF support
🧠 Quiz answer explanations
📊 Progress tracking system
🌙 Dark mode UI
☁️ Cloud storage for notes

## 👨‍💻 Author
Sadia Afsana
