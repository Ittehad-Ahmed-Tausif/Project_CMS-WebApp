import streamlit as st
import re
import time
from datetime import datetime

class login_signup:

    def login():
        st.text("")
        username = st.text_input("Email or phone number")
        password = st.text_input("Password", type="password")

        st.text("")
        col1, col2, col3 = st.columns([2,2.3,2])
        with col2:
            col2_1, col2_2 = st.columns([1, 2]) 
            with col2_1:
                login_button = st.button("Login") 
            with col2_2:
                forgot_password = st.button("Forgot Password")
                
        if login_button:
            #match the username with the email
            st.success("Congratulations! You have successfully logged in.")
        if forgot_password:
            # Redirect to forgot password page
            st.write("Redirecting to forgot password page...")

            time.sleep(1)
            
            login_signup.forgot_password()

    def create_an_account():
        first_name = st.text_input("First Name") 
        last_name = st.text_input("Last Name")
        dob = st.date_input("Date of Birth", datetime.today())
        gender = st.radio("Gender", ("Other", "Male", "Female"), horizontal=True)   
        address1 = st.text_input("Address Line 1")         
        address2 = st.text_input("Address Line 2") 
        phone_number = st.text_input("Phone Number")        
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        retype_password = st.text_input("Retype Password", type="password")

        st.text("")

        # a button to create an account 
        col1, col2, col3 = st.columns([2,2,1])
        with col2:
            create_account_button = st.button("Create an account")

        if create_account_button:
            if not re.match(r"^[A-Za-z][A-Za-z ]*$", first_name):
                    st.warning("First name must contain only characters.")
            elif not re.match(r"^[A-Za-z][A-Za-z ]*$", last_name):
                st.warning("Last name must contain only characters.")
            elif not re.match(r"^[A-Za-z][A-Za-z ]*$", address1):
                st.warning("Last name must contain only characters.")
            elif phone_number.isnumeric() == False:
                st.warning("Phone number must contain only digits.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.warning("Invalid email address. Please enter a valid email address.")
            elif len(password) < 8:
                st.warning("Password must be at least 8 characters long.")
            else:
                count = 0
                if any(c.isupper() for c in password):
                    count += 1
                if any(c.islower() for c in password):
                    count += 1
                if any(c.isdigit() for c in password):
                    count += 1
                if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password):
                    count += 1
                
                if count < 3:
                    st.warning("Password must contain at least three of the following: uppercase letters [A], lowercase letters [a], digits [0], special characters [@].")
                elif password != retype_password:
                    st.warning("Passwords do not match. Please retype the password.")
                else:
                    st.success("Congratulations! You have successfully created an account.")
                
    def forgot_password():
        st.warning("This site is currently under construction. Some features may not be available.")
    
    #checked