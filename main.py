import streamlit as st
# import pandas   
from login_signup import login_signup

st.title("Login or Sign Up")
st.sidebar.title("Project CMS")
page = st.sidebar.radio("## Menu", ["Login", "Create an account"])
     
        

 

        # if login_button:
        #     #match the username with the email
        #     pass
        #     # login_signup.check_username(username)
        #     st.success("Congratulations! You have successfully logged in.")

      
            # st.success("Congratulations! You have successfully signed up.")

    #     st.title("Login")
    #     username = st.number_input("Username")
    #     password = st.text_input("Password", "type here", type="password")
    #     if st.button("Login"):
    #         st.success("Congratulations! You have successfully logged in.")
    # elif page == "Signup":
    #     st.title("Signup")
    #     new_username = st.text_input("New Username")
    #     new_password = st.text_input("New Password", "type here", type="password")
    #     if st.button("Create Account"):
    #         st.success("Account created successfully!")




# Define the content for each page
# def home():
#     st.title("Home Page")
#     st.write("Welcome to the Home Page!")
#     st.write("This is the main page of your Streamlit app.")

# def page1():
#     st.title("Page 1")
#     st.write("Welcome to Page 1!")
#     st.write("Here is where the content for Page 1 goes.")

# def page2():
#     st.title("Page 2")
#     st.write("Welcome to Page 2!")
#     st.write("This is the content for Page 2.")
# col1, col2, col3 = st.columns([2,2.3,2])
# with col2:
#     col2_1, col2_2 = st.columns([1, 2]) 
#     with col2_1:
#         login_button = st.button("Login")     
#     with col2_2:
#         sign_up_button = st.button("create an account")

# if sign_up_button:
#     login()
          
            
# Page routing logic
if page == "Login":
    login_signup.login()
elif page == "Create an account":
    login_signup.create_an_account()
# elif page == "Page 2":
#     page2()
