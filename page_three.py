# page_three.py
import streamlit as st
import pandas as pd
import random
import string
import base64

def generate_password(length):
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=4))
    password = random_chars

    while len(password) < length:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    return password

def generate_passwords_for_employees(data):
    # Menambah kolom password
    data["Password"] = data["Pegawai"].apply(lambda x: generate_password(12))
    return data

def show_page():
    st.title("Generate Passwords for Employees")

    # Set warna latar belakang dan teks
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f5f5;
            color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Upload file CSV
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        # Membaca data dari file CSV
        data = pd.read_csv(uploaded_file)

        # Menampilkan preview data
        st.subheader("Preview Data Pegawai")
        st.write(data.head())

        # Menambahkan kolom password
        if st.button("Add Passwords"):
            data_with_passwords = generate_passwords_for_employees(data)
            st.subheader("Data Pegawai dengan Password")
            st.write(data_with_passwords)

            # Menyimpan hasil ke file CSV
            csv_file = data_with_passwords.to_csv(index=False)
            st.markdown(get_csv_download_link(csv_file), unsafe_allow_html=True)

def get_csv_download_link(csv_file):
    # Mengenkripsi file CSV menjadi format base64
    b64 = base64.b64encode(csv_file.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="passwords.csv" style="color: #fff; background-color: #007BFF; padding: 10px; border-radius: 5px; text-decoration: none;">Download CSV File</a>'
    return href

# Panggil fungsi show_page untuk mengeksekusi aplikasi Streamlit
if __name__ == "__main__":
    show_page()
