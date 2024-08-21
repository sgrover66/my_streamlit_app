import streamlit as st

# Function to handle user registration
def register_user(username, password, email):
    st.success(f"User {username} registered successfully!")

# Display the registration form
def show_registration_form():
    st.title("User Registration")

    # Create a registration form
    with st.form(key='registration_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")

        # Create a submit button
        submit_button = st.form_submit_button(label="Register")

    # Handle form submission
    if submit_button:
        if username and password and email:
            register_user(username, password, email)
        else:
            st.error("Please fill out all fields.")

# Run the registration form
if __name__ == "__main__":
    show_registration_form()
