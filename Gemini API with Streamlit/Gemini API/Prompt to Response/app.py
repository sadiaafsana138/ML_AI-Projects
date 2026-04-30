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

# UI
st.title("Gemini Prompt App")

prompt = st.text_area("Enter your prompt:")

if st.button("Generate Response"):
    if prompt.strip():
        with st.spinner("Generating..."):
            try:
                response = model.generate_content(prompt)
                st.subheader("Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt.")