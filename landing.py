import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.svm import SVC
from textblob import TextBlob


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return 'Positif'
    else:
        return 'Negatif'


def main():
    st.title("Sentiment Analysis")
    st.markdown(
        "------------------------------------------------------------------------------------")

    data = pd.DataFrame()
    st.sidebar.title("Navbar")
    menu = ["Home", "Contact", "Data Content"]
    choice = st.sidebar.radio("Menu", menu)

    if choice == "Home":
        st.header("Selamat datang di halaman utama!")

        col1, col2 = st.columns(2)
        with col1:
            st.image("powerLogo.png")
        with col2:
            st.write("Sentiment analysis adalah proses penting dalam analisis teks yang memahami opini, sentimen, dan perasaan. Twitter sebagai platform populer menjadi sumber data berharga. Analisis sentimen terkait ChatGPT menggunakan algoritma SVM dan Naive Bayes. Kombinasi pemrosesan bahasa alami (NLP) dan algoritma tersebut memberikan wawasan tentang pandangan masyarakat terhadap aplikasi ini.")
            st.write("Pentingnya analisis sentimen pada Twitter terkait ChatGPT terletak pada informasi yang diperoleh mengenai respons masyarakat. SVM dan Naive Bayes memungkinkan analisis sentimen yang cepat dan akurat. Memahami pandangan masyarakat membantu pengembangan dan penggunaan ChatGPT di masa depan, serta meningkatkan kualitas pelayanan yang sesuai dengan kebutuhan pengguna.")

    elif choice == "Contact":
        st.subheader(
            "Selamat datang di halaman About Us! Kami adalah tim yang terdiri dari lima orang dengan tujuan untuk membuat proyek ini.")
        st.subheader("Anggota Tim:")
        team_members = [
            {"nama": "Haura Jihan Putri", "nim": "203503516034",
                "universitas": "Universitas Nasional"},
            {"nama": "Nurul Nabila", "nim": "2011500267",
                "universitas": "Universitas Budi Luhur"},
            {"nama": "Christian Jerico Rejeki", "nim": "1152000057",
                "universitas": "Institut Teknologi Indonesia"},
            {"nama": "Fredrik Dwiyanto", "nim": "1220210046",
                "universitas": "Universitas Pancasila"},
            {"nama": "Sri Dwita Girsang", "nim": "201011201390",
                "universitas": "Universitas Pamulang"}
        ]

        col1, col2 = st.columns(2)
        for i, member in enumerate(team_members):
            if i % 2 == 0:
                column = col1
            else:
                column = col2

            with column:
                st.write(f"Nama: {member['nama']}")
                st.write(f"NIM: {member['nim']}")
                st.write(f"Universitas: {member['universitas']}")
                st.write("---")

    if choice == "Data Content":
        # Memuat data dari file pkl
        data = joblib.load('model.pkl')

        # Memuat model
        model = joblib.load('model.pkl')

        # Input teks
        text = st.text_area("Masukkan teks di sini:")

        # Tombol untuk menganalisis sentimen
        if st.button("Analisis Sentimen"):
            if text:
                result = analyze_sentiment(text)
                st.success(f"Hasil Analisis Sentimen: {result}")
            else:
                st.warning("Masukkan teks terlebih dahulu.")


if __name__ == '__main__':
    main()
