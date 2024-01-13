import streamlit as st

def show_page():
    # Header
    st.title("About")
    st.markdown(
        """
        *Selamat datang di halaman About!* 🌟
        """
    )

    st.image("header_image.png", use_column_width=True)  # Ganti dengan gambar header yang sesuai

    st.markdown(
        """
        ## Universitas Mercu Buana
        ### Teknik Informatika

        **Tim kami:**
        1. **Muh Jadid Taqwa** (41520120026) - *Ketua Kelompok*
        2. **Charles Julius Kangga** (41518120039)
        3. **Saidi Syabab A.J** (41520110096)

        Tujuan kami adalah untuk memenuhi tugas besar 2 pada mata kuliah Pemrograman Smart Web.
        """
    )

    st.markdown(
        """
        ### Terima kasih atas perhatian Anda! 🙏

        Kami berharap Anda menikmati aplikasi ini dan jika Anda memiliki pertanyaan,
        jangan ragu untuk menghubungi kami.
        """
    )

    # Tautan ke alamat website sosial media (fiktif)
    st.markdown(
        """
        [Facebook](https://www.facebook.com) |
        [Twitter](https://www.twitter.com) |
        [Instagram](https://www.instagram.com)
        """
    )

    # Footer
    st.markdown(
        """
        ---
        *Dibuat dengan ❤️ oleh Jasu*
        """
    )

    # Styling tambahan dengan warna yang lebih mencolok
    st.markdown(
        """
        <style>
            body {
                background-color: #3498db; /* Warna latar belakang halaman (putih) */
                color: #000000; /* Warna teks (hitam) */
                line-height: 1.6;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
            }
            img {
                max-width: 100%;
                height: auto;
            }
            a {
                color: #ffd600; /* Warna tautan (kuning) */
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
