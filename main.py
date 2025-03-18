import streamlit as st
from PIL import Image
import about  # Pastikan modul ini ada dan berisi fungsi about_me()

# Konfigurasi halaman
st.set_page_config(page_title='Portfolio Saya', page_icon='✨', layout='wide')

# CSS untuk mempercantik tampilan
def load_css():
    st.markdown(
        """
        <style>
            body {
                background-color: #f0f2f6;
            }
            .title {
                font-size: 50px;
                color: #ff4b4b;
                font-weight: bold;
                text-align: center;
            }
            .subtitle {
                font-size: 25px;
                color: #444;
                text-align: center;
            }
            .sidebar .sidebar-content {
                background-color: #ffebe6;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

# Panggil fungsi CSS
load_css()

# Header utama
st.markdown('<p class="title">Portfolio Saya</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">💡 Data Analyst | Data Scientist 💡</p>', unsafe_allow_html=True)

# Sidebar Navigasi
st.sidebar.title('📌 Navigasi')
st.sidebar.markdown("---")
page = st.sidebar.radio('Pilih Halaman:', ['🏠 Tentang Saya', '📊 Dashboard', '📉 Customer_Satisfacation', '📬 Kontak'])

# Konten Halaman
if page == '🏠 Tentang Saya':
    about.about_me()

elif page == '📊 Dashboard':
    st.header('📌 Proyek Data Analyst')
    st.write("Berikut penjelasan proyek yang telah saya kerjakan:")
    st.markdown("- 🏪 **Customer Segmentation menggunakan RFM Analysis**")
    st.markdown("---")
    import Dashboard
    Dashboard.tampilan_dashboard()


elif page == '📉 Customer_Satisfacation':
    import Customer_Satisfacation
    Customer_Satisfacation.Tampilkan_Customer_Satisfacation()
    st.header('📊 Customer Satisfacation')
    st.write("Analisis kepuasan pelanggan berdasarkan ulasan pelanggan terhadap layanan maskapai penerbangan.")
    st.markdown("---")
    from Customer_Satisfacation import Tampilkan_Customer_Satisfaction
    Tampilkan_Customer_Satisfaction()
    from Customer_Satisfacation import Tampilkan_Customer_Satisfaction
    Tampilkan_Customer_Satisfaction()


 
elif page == '📬 Kontak':
    import Kontak
    Kontak.munculkan_Kontak()
    
    # Formulir Kontak
    with st.form("contact_form"):
        name = st.text_input("Nama")
        email = st.text_input("Email")
        message = st.text_area("Pesan")
        submitted = st.form_submit_button("Kirim")
        if submitted:
            st.success("Pesan Anda telah terkirim! ✅")
