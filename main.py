import streamlit as st

# Title of the app
st.title("Login or Signup")

# Input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Buttons for login and signup
if st.button("Login"):
    st.write("Login button clicked")
elif st.button("Signup"):
    st.write("Signup button clicked")
