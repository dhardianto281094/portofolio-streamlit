import streamlit as st
import pandas as pd
import plotly.express as px

def Tampilkan_Customer_Satisfacation():
    """Fungsi untuk menampilkan analisis kepuasan pelanggan di Streamlit."""
    
    # Simulasi Data
    data = pd.DataFrame({
        "is_satisfied": ["Satisfied", "Not Satisfied"],
        "proportion": [0.652444, 0.347556]
    })

    #  Judul utama
    st.title(" Customer Satisfaction Analysis")

    #  Deskripsi singkat
    st.markdown("""
    ###  **Analisis Kepuasan Pelanggan**
    Grafik di bawah ini menunjukkan **proporsi pelanggan yang puas dan tidak puas** berdasarkan survei.  
    Data ini dapat digunakan untuk memahami pengalaman pelanggan dan meningkatkan layanan.
    """)

    #  Membuat visualisasi Pie Chart dengan Plotly
    fig = px.pie(
        data, 
        names="is_satisfied", 
        values="proportion",
        title="Proportion of Satisfied vs. Not Satisfied Customers",
        color="is_satisfied",
        color_discrete_map={"Satisfied": "#2ECC71", "Not Satisfied": "#E74C3C"},
        hole=0.3  # Membuat tampilan Donut Chart
    )

    # Menampilkan Pie Chart di Streamlit
    st.plotly_chart(fig, use_container_width=True)

    #  Menampilkan Tabel Data dengan Format Persen
    st.subheader(" Customer Satisfaction Data")
    st.dataframe(data.style.format({"proportion": "{:.2%}"}))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

def Tampilkan_Customer_Satisfaction():
    """Fungsi untuk menampilkan analisis kepuasan pelanggan dengan distribusi sentimen."""

    # Konfigurasi halaman
    st.title(" Customer Satisfaction & Sentiment Analysis")

    # Simulasi Data Sentimen
    sentiment_data = pd.DataFrame({
        "vader_sentiment": ["Positive", "Negative", "Neutral"],
        "count": [700, 566, 23]
    })

    #  Bar Chart untuk Sentimen
    fig_bar = px.bar(
        sentiment_data, 
        x="vader_sentiment", 
        y="count",
        color="vader_sentiment",
        title="Distribution of Customer Sentiment",
        color_discrete_map={"Positive": "#2ECC71", "Negative": "#E74C3C", "Neutral": "#3498DB"}
    )

    # Menampilkan Bar Chart di Streamlit
    st.plotly_chart(fig_bar, use_container_width=True)

    #  Simulasi Data Distribusi Histogram
    x1 = np.random.randn(200) - 2  # Distribusi mirip Negatif
    x2 = np.random.randn(200)      # Distribusi mirip Netral
    x3 = np.random.randn(200) + 2  # Distribusi mirip Positif

    # Group Data
    hist_data = [x1, x2, x3]
    group_labels = ["Negative", "Neutral", "Positive"]

    # Membuat Distplot (Distribusi Data)
    fig_hist = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5], 
                                  colors=["#E74C3C", "#3498DB", "#2ECC71"])

    # Menampilkan Distplot di Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

    #  Menampilkan Data dalam Tabel
    st.subheader(" Customer Sentiment Data")
    st.dataframe(sentiment_data.style.format({"count": "{:,}"}))  # Format angka dengan koma

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

def Tampilkan_Customer_Satisfaction():
    """Fungsi untuk menampilkan analisis kepuasan pelanggan dengan Word Cloud dan rekomendasi bisnis."""

    # Konfigurasi halaman
    st.title(" Customer Satisfaction & Word Cloud Analysis")

    #  Data Sentimen & Kata Kunci
    df_top_word = pd.DataFrame({
        "vader_sentiment": ["Positive", "Positive", "Negative", "Negative", "Neutral", "Neutral"],
        "token": ["good service", "great experience", "bad support", "slow response", "okay", "acceptable"]
    })

    # **Visualisasi Word Cloud Berdasarkan Sentimen**
    st.subheader("☁️ Word Cloud Sentiment Analysis")

    # Identifikasi kategori sentimen unik
    groups = df_top_word["vader_sentiment"].unique()

    # Buat layout subplot berdasarkan jumlah kategori sentimen
    fig, axes = plt.subplots(1, len(groups), figsize=(15, 5), squeeze=False)

    for idx, group in enumerate(groups):
        text = " ".join(df_top_word[df_top_word["vader_sentiment"] == group]["token"])
        
        # Generate Word Cloud
        wordcloud = WordCloud(width=400, height=400, background_color="white", colormap="plasma").generate(text)
        
        # Tampilkan Word Cloud di subplot
        axes[0, idx].imshow(wordcloud, interpolation="bilinear")
        axes[0, idx].set_title(f"{group}", fontsize=14, fontweight="bold")
        axes[0, idx].axis("off")

    plt.tight_layout()
    st.pyplot(fig)  # Menampilkan di Streamlit

    #  **Kesimpulan & Rekomendasi Bisnis**
    st.subheader(" Business Insights & Recommendations")
    
    st.markdown("""
    - **Positive Sentiment:** Pelanggan puas dengan layanan yang baik dan pengalaman yang menyenangkan.  
    - **Negative Sentiment:** Keluhan utama terkait layanan support yang buruk dan respon lambat.  
    - **Neutral Sentiment:** Beberapa pelanggan memiliki pengalaman yang biasa saja, tidak terlalu positif atau negatif.  

    ** Rekomendasi Bisnis:**  
    - **Tingkatkan layanan customer support** untuk mengatasi keluhan utama.  
    - **Gunakan teknologi AI chatbot** untuk mempercepat respon terhadap pelanggan.  
    - **Berikan loyalty program** kepada pelanggan yang puas untuk mempertahankan engagement mereka.  
    """)

    st.success(" **Gunakan insight ini untuk meningkatkan strategi bisnis Anda!**")

