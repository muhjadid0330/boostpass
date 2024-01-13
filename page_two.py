# page_two.py
import streamlit as st
import random
import string

def show_page():
    def generate_password(user_input, length):
        # Menambahkan karakter acak ke input pengguna
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=4))
        password = user_input + random_chars

        # Menambahkan karakter acak untuk memenuhi persyaratan panjang password
        while len(password) < length:
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)

        return password

    def password_strength(password):
        # Evaluasi kekuatan password berdasarkan panjang
        if len(password) < 8:
            return "Sangat Lemah"
        elif len(password) < 12:
            return "Lemah"
        elif len(password) < 16:
            return "Moderat"
        else:
            return "Kuat"

    # Streamlit App
    st.title("SecurePass Generator")

    # Input dari pengguna
    user_input = st.text_input("Masukkan kata kunci:", "")

    # Opsi panjang password
    length = st.slider("Panjang Password:", min_value=8, max_value=20, value=12, step=1)

    # Tombol untuk generate password
    if st.button("Generate Password"):
        if user_input:
            generated_password = generate_password(user_input, length)
            st.success(f"Password yang dihasilkan: {generated_password}")

            # Menampilkan kekuatan password
            strength = password_strength(generated_password)
            st.info(f"Kekuatan Password: {strength}")

            # Tombol untuk menyalin password ke clipboard
            st.button("Salin Password", on_click=lambda: st.text_area("Password", generated_password, height=1))

    # Menyediakan informasi tentang keamanan password di setiap halaman
    st.info(
        "Pastikan untuk menggunakan password yang kuat dan tidak membagikan password Anda dengan orang lain."
    )

    # Footer
    st.markdown(
        """
        ---
        Dibuat dengan ❤️ oleh Jasu
        """
    )
