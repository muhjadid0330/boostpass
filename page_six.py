# page_six.py
import streamlit as st
import random
import string

def show_page():
    show_header()
    password_length, include_uppercase, include_lowercase, include_numbers, include_symbols = password_settings()
    
    if st.button("Generate Password"):
        generated_password = generate_password(password_length, include_uppercase, include_lowercase, include_numbers, include_symbols)
        if generated_password:
            st.success("Generated Password: " + generated_password)

    show_footer()

def show_header():
    st.image("https://i.imgur.com/hivPbWc.png", width=200)
    st.title("Password Generator")

def password_settings():
    password_length = st.number_input("Password length", min_value=4, max_value=20, value=8)
    include_uppercase = st.checkbox("Include uppercase letters", value=True)
    include_lowercase = st.checkbox("Include lowercase letters", value=True)
    include_numbers = st.checkbox("Include numbers", value=True)
    include_symbols = st.checkbox("Include symbols", value=True)

    return password_length, include_uppercase, include_lowercase, include_numbers, include_symbols

def generate_password(password_length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        st.warning("Please select at least one character type.")
        return ""

    password = ''.join(random.choice(characters) for _ in range(password_length))
    return password

def show_footer():
    st.markdown("&copy; Copyright Boost Pass 2023. All rights reserved.")
