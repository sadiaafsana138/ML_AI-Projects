import streamlit as st
from PIL import Image

st.title("Image Gallery App")

# File uploader
uploaded_files = st.file_uploader(
    "Upload up to 3 images (jpg, jpeg, png)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

# Submit button
if st.button("Submit"):

    if uploaded_files:
        # check limit
        if len(uploaded_files) > 3:
            st.error("You can upload maximum 3 images only!")

        else:
            if len(uploaded_files) == 3:
                st.success("Exactly 3 images uploaded!")

            # show images side by side
            cols = st.columns(len(uploaded_files))

            for idx, file in enumerate(uploaded_files):
                image = Image.open(file)
                cols[idx].image(image, use_container_width=True)

    else:
        st.warning("Please upload at least 1 image!")