import streamlit as st
import pandas as pd
import numpy as np

# Simulasi Data proportion fill_survey
def generate_data():
    data = pd.DataFrame({
        "Responded": np.random.choice([0, 1], size=100, p=[0.3, 0.7]),  # 70% responden mengisi survey
        "proportion": np.random.rand(100)  # Nilai acak antara 0 - 1
    })
    return data

def tampilan_dashboard():
    st.title(" Analisis Proportion Fill Survey")
    
    # Generate Data
    data = generate_data()

    # Menampilkan Data
    st.write("###  Data Survey")
    st.dataframe(data)

    # Menampilkan Visualisasi
    st.markdown("###  Distribusi Responden")
    st.bar_chart(data.groupby("Responded")["proportion"].mean())

    # Menambahkan Filter
    st.markdown("###  Filter Data")
    min_val, max_val = st.slider("Pilih rentang proportion:", 
                                 float(data["proportion"].min()), 
                                 float(data["proportion"].max()), 
                                 (0.2, 0.8))

    filtered_data = data[(data["proportion"] >= min_val) & (data["proportion"] <= max_val)]

    st.write(f" **Jumlah Data setelah Filter: {filtered_data.shape[0]}**")
    st.dataframe(filtered_data)

# Menjalankan fungsi utama jika file dijalankan langsung
if __name__ == "__main__":
    tampilan_dashboard()
