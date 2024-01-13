# app.py
import streamlit as st
import pandas as pd
import random
import string

def is_common_password(password):
    # Fungsi ini dapat diperluas dengan menambahkan kata-kata umum atau menggunakan database yang lebih besar
    common_passwords = ["password", "123456", "qwerty", "letmein"]
    return password.lower() in common_passwords

def is_password_strong(password):
    # Fungsi ini dapat diperluas dengan menambahkan kriteria penilaian kekuatan password yang lebih kompleks
    return len(password) >= 12 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password)

def generate_recommendation(user_input):
    # Gabungkan kata dari inputan user dengan karakter yang beragam, angka, dan panjang minimal 12 karakter
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=4))
    recommendation = user_input + random_chars

    while len(recommendation) < 12:
        recommendation += random.choice(string.ascii_letters + string.digits + string.punctuation)

    return recommendation

def show_page():
    st.title("Password Strength Checker")

    # Input password dari pengguna
    user_password = st.text_input("Masukkan password:", type="password")

    if st.button("Check Strength"):
        if user_password:
            # Pemeriksaan kata-kata umum
            if is_common_password(user_password):
                st.warning("Password ini termasuk dalam kategori kata-kata umum yang tidak aman.")
            else:
                # Pemeriksaan kekuatan password
                if is_password_strong(user_password):
                    st.success("Password ini kuat!")
                else:
                    st.warning("Password ini lemah. Pertimbangkan untuk menggunakan karakter yang beragam, angka, dan panjang minimal 12 karakter.")
                    # Berikan rekomendasi password
                    recommendation = generate_recommendation(user_password)
                    st.info(f"Rekomendasi Password: {recommendation}")

# Panggil fungsi show_page untuk mengeksekusi aplikasi Streamlit
if __name__ == "__main__":
    show_page()
