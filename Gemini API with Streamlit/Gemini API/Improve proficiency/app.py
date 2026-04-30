import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()

# Get API key 
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load model
model = genai.GenerativeModel("gemini-3-flash-preview")

st.title("Professional Sentence Improver")

# User input
sentence = st.text_input("Enter your sentence:")

if st.button("Improve Sentence"):
    if sentence.strip():
        prompt = f"Improve this sentence professionally:\n\n{sentence}"

        with st.spinner("Improving..."):
            try:
                response = model.generate_content(prompt)
                st.subheader("Improved Sentence:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a sentence.")