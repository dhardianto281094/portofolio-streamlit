import streamlit as st

def munculkan_Kontak():
    st.title("📞 Kontak Saya")
    st.write("Hubungi saya melalui tautan berikut:")

    # Menampilkan tombol kontak dengan ikon dan link
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <a href="https://www.linkedin.com/in/dimashardianto/" target="_blank">
                <button style="
                    background-color: #0077b5;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;">
                    🔗 LinkedIn
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <a href="https://github.com/dhardianto281094" target="_blank">
                <button style="
                    background-color: black;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;">
                    🐙 GitHub
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <a href="mailto:your.iniakudimas28@gmail.com">
                <button style="
                    background-color: #FF5733;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;">
                    ✉️ Email
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

# Menjalankan fungsi jika script ini dipanggil langsung
if __name__ == "__main__":
    munculkan_Kontak()
