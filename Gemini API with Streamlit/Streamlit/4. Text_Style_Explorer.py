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
