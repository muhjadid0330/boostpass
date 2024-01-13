# page_one.py
import streamlit as st

def show_page():
    st.title("Password Generator")
    
    # Tambahkan logo
    logo_path = "logo.png"
    st.image(logo_path, caption="Password Generator", width=200)  # Ubah nilai width sesuai kebutuhan

    st.write(
        """
        Selamat datang di Password Generator! Gunakan alat ini untuk membuat kata sandi yang kuat dan aman.
        
        ### Cara Menggunakan:
        1. Pilih panjang kata sandi yang diinginkan.
        2. Tentukan jenis karakter yang ingin Anda masukkan (huruf besar, huruf kecil, angka, simbol).
        3. Tekan tombol "Generate Password" untuk membuat kata sandi baru.
        4. Salin kata sandi dan gunakan sesuai kebutuhan Anda.

        Jangan lupa menyimpan kata sandi dengan aman!
        """
    )

    # Tambahkan fitur password generator di bawah ini
    # ...

    # Contoh tombol dan input untuk memulai
    generate_button = st.button("Generate Password")
    if generate_button:
        generated_password = generate_password()  # Gantilah ini dengan fungsi yang sesuai
        st.success(f"Kata Sandi Baru: {generated_password}")

# Fungsi untuk menghasilkan kata sandi
def generate_password():
    # Gantilah ini dengan logika Anda untuk menghasilkan kata sandi
    return "GeneratedPassword123"
