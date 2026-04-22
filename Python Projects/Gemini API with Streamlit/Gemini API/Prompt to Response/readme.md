# Gemini Prompt App 🚀

A simple Streamlit web application that allows users to enter a prompt and generate responses using Google's Gemini model.

---

## 🌟 Features

- Clean and simple UI using Streamlit
- Uses Google Gemini API (`gemini-3-flash-preview`)
- Environment variable support for secure API key handling
- Error handling for API failures

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Generative AI (Gemini API)
- python-dotenv

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gemini-prompt-app.git
cd gemini-prompt-app
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup Environment Variables

Create a `.env` file in the root directory and add your Google API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## 📁 Project Structure

```
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

1. User enters a prompt in the text area.
2. On clicking **Generate Response**, the app sends the prompt to the Gemini API.
3. The API returns generated text.
4. The response is displayed in the app.

---

## ⚠️ Error Handling

- Displays warnings if the prompt is empty
- Catches API errors and shows them in the UI

---

## 📌 Requirements Example

Create a `requirements.txt` file with:

```txt
streamlit
google-generativeai
python-dotenv
```

---

## 🚀 Deployment

You can deploy this app easily on:

- Streamlit Cloud
- Render
- Railway

Make sure to add your `GOOGLE_API_KEY` in the platform's environment variables.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

- Google Generative AI
- Streamlit

---

## 💡 Future Improvements

- Add model selection
- Add chat history
- Improve UI/UX
- Add download/export responses

---

Happy coding! 🎉

