import streamlit as st

st.title("Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selector
operation = st.selectbox("Choose operation", ["+", "-", "*", "/"])

# Calculate button
if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
        st.success(f"Result: {result}")

    elif operation == "-":
        result = num1 - num2
        st.success(f"Result: {result}")

    elif operation == "*":
        result = num1 * num2
        st.success(f"Result: {result}")

    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Cannot divide by zero")