import streamlit as st

st.title("Audio & Video Player App")

if "active" not in st.session_state:
    st.session_state.active = None
    st.session_state.audio_file = None
    st.session_state.video_file = None

# ---------------- AUDIO ----------------
st.header("Audio Player")

audio_file = st.file_uploader(
    "Upload Audio",
    type=["mp3", "ogg"],
    key="audio_uploader"
)

if st.button("Submit Audio"):
    if audio_file:
        st.session_state.active = "audio"
        st.session_state.audio_file = audio_file
        st.session_state.video_file = None
        st.rerun()   # force UI refresh
    else:
        st.error("Please upload an audio file first!")

# Only render audio if active
if st.session_state.active == "audio" and st.session_state.audio_file:
    st.audio(st.session_state.audio_file)

# ---------------- VIDEO ----------------
st.header("Video Player")

video_file = st.file_uploader(
    "Upload Video",
    type=["mp4", "mkv"],
    key="video_uploader"
)

if st.button("Submit Video"):
    if video_file:
        st.session_state.active = "video"
        st.session_state.video_file = video_file
        st.session_state.audio_file = None
        st.rerun()   # force UI refresh
    else:
        st.error("Please upload a video file first!")

# Only render video if active
if st.session_state.active == "video" and st.session_state.video_file:
    st.video(st.session_state.video_file)