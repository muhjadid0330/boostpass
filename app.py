import streamlit as st
from page_one import show_page as show_page_one
from page_two import show_page as show_page_two
from page_three import show_page as show_page_three
from page_four import show_page as show_page_four
from page_five import show_page as show_page_five
from page_six import show_page as show_page_six

# Set page configuration before any other Streamlit commands
st.set_page_config(page_title="Password Generator", page_icon="🔐")

# Dictionary untuk memetakan nama halaman ke fungsi yang sesuai
pages = {
    "Home": show_page_one,
    "SafetyKey Pro": show_page_two,
    "EmployeePass Gen": show_page_three,
    "PassGuardian": show_page_four,
    "PasswordGold": show_page_six,
    "About": show_page_five
}

# Tambahkan gaya CSS untuk sidebar
st.markdown(
    """
    <style>
        .sidebar-content {
            background-color: #2E4053; /* Warna latar belakang sidebar */
            color: #FFFFFF; /* Warna teks sidebar */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar dengan pilihan halaman
selected_page = st.sidebar.radio("Select Page", list(pages.keys()), index=0)

# Panggil fungsi yang sesuai dengan halaman yang dipilih
pages[selected_page]()
