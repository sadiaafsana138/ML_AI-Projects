# Streamlit Projects Collection

This repository contains 5 simple Streamlit applications.

------------------------------------------------------------------------

## 1. Personal Info Card App

Live: https://personal-info-card.streamlit.app/

``` python
import streamlit as st

st.markdown("<h1 style='font-size: 60px;'>Personal Info Card App</h1>", unsafe_allow_html=True)

st.markdown("<h3>Name</h3>", unsafe_allow_html=True)
name = st.text_input("", key="name")

st.markdown("<h3>Age</h3>", unsafe_allow_html=True)
age = st.number_input("", min_value=0, max_value=100, step=1, key="age")

st.markdown("<h3>Profession</h3>", unsafe_allow_html=True)
profession = st.selectbox("", ["-- Select --", "Student", "Employee", "Businessman", "Freelancer"])

if st.button("Submit"):
    if not name:
        st.warning("⚠️ Please enter your name!")
    elif age == 0:
        st.warning("⚠️ Please enter your age!")
    elif profession == "-- Select --":
        st.warning("⚠️ Please select your profession!")
    else:
        st.success("✅ Information saved!")
        st.markdown(f"""
        ---
        👤 **Name:** {name}  
        🎂 **Age:** {age}  
        💼 **Profession:** {profession}
        """)
```

------------------------------------------------------------------------

## 2. Smart Image Gallery App

Live: https://smart-image-gallery.streamlit.app/

``` python
import streamlit as st
from PIL import Image

st.title("Image Gallery App")

uploaded_files = st.file_uploader(
    "Upload up to 3 images (jpg, jpeg, png)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if st.button("Submit"):
    if uploaded_files:
        if len(uploaded_files) > 3:
            st.error("You can upload maximum 3 images only!")
        else:
            if len(uploaded_files) == 3:
                st.success("Exactly 3 images uploaded!")

            cols = st.columns(len(uploaded_files))

            for idx, file in enumerate(uploaded_files):
                image = Image.open(file)
                cols[idx].image(image, use_container_width=True)
    else:
        st.warning("Please upload at least 1 image!")
```

------------------------------------------------------------------------

## 3. Audio & Video Player App

Live: https://audio-video-player.streamlit.app/

``` python
import streamlit as st

st.title("Audio & Video Player App")

if "active" not in st.session_state:
    st.session_state.active = None
    st.session_state.audio_file = None
    st.session_state.video_file = None

st.header("Audio Player")

audio_file = st.file_uploader("Upload Audio", type=["mp3", "ogg"])

if st.button("Submit Audio"):
    if audio_file:
        st.session_state.active = "audio"
        st.session_state.audio_file = audio_file
        st.session_state.video_file = None
        st.rerun()
    else:
        st.error("Please upload an audio file first!")

if st.session_state.active == "audio" and st.session_state.audio_file:
    st.audio(st.session_state.audio_file)

st.header("Video Player")

video_file = st.file_uploader("Upload Video", type=["mp4", "mkv"])

if st.button("Submit Video"):
    if video_file:
        st.session_state.active = "video"
        st.session_state.video_file = video_file
        st.session_state.audio_file = None
        st.rerun()
    else:
        st.error("Please upload a video file first!")

if st.session_state.active == "video" and st.session_state.video_file:
    st.video(st.session_state.video_file)
```

------------------------------------------------------------------------

## 4. Text Style Explorer

Live: https://text-explorer.streamlit.app/

``` python
import streamlit as st

st.set_page_config(page_title="Text Style Explorer", layout="centered")

st.title("Text Style Explorer")

user_text = st.text_input("Enter your text:")

if st.button("Submit"):
    if user_text:
        st.divider()
        st.title(user_text)
        st.divider()
        st.header(user_text)
        st.divider()
        st.subheader(user_text)
        st.divider()
        st.text(user_text)
```

------------------------------------------------------------------------

## 5. Basic Calculator App

Live: https://basic-calculator-using-st.streamlit.app/

``` python
import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox("Choose operation", ["+", "-", "*", "/"])

if st.button("Calculate"):
    if operation == "+":
        st.success(f"Result: {num1 + num2}")
    elif operation == "-":
        st.success(f"Result: {num1 - num2}")
    elif operation == "*":
        st.success(f"Result: {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            st.success(f"Result: {num1 / num2}")
        else:
            st.error("Cannot divide by zero")
```

------------------------------------------------------------------------

## 🚀 About

These are beginner-friendly Streamlit projects for learning UI, input
handling, file upload, media playback, and basic operations.
