import streamlit as st

# App title with custom font size
st.markdown("<h1 style='font-size: 60px;'>Personal Info Card App</h1>", unsafe_allow_html=True)

# Name input
st.markdown("<h3>Name</h3>", unsafe_allow_html=True)
name = st.text_input("", key="name")

# Age input
st.markdown("<h3>Age</h3>", unsafe_allow_html=True)
age = st.number_input("", min_value=0, max_value=100, step=1, key="age")

# Profession dropdown
st.markdown("<h3>Profession</h3>", unsafe_allow_html=True)
profession = st.selectbox("", ["-- Select --", "Student", "Employee", "Businessman", "Freelancer"])

# Submit button
if st.button("Submit"):
    # Validate fields
    if not name:
        st.warning("⚠️ Please enter your name!")
    elif age == 0:
        st.warning("⚠️ Please enter your age!")
    elif profession == "-- Select --":
        st.warning("⚠️ Please select your profession!")
    else:
        # Display info card
        st.success("✅ Information saved!")
        st.markdown(f"""
        ---
        👤 **Name:** {name}  
        🎂 **Age:** {age}  
        💼 **Profession:** {profession}
        """)