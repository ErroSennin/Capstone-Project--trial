import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt


st.set_page_config(
    page_title = 'Capstone Project',
    layout='wide'
)

st.title("Perbandingan Jumlah Penganggutan di Indonesia Sebelum dan Sesudah Covid-19")

st.subheader("Pandemi Covid-19 telah memberikan dampak signifikan terhadap berbagai sektor kehidupan di Indonesia, termasuk ketenagakerjaan.  Dalam artikel ini, kita akan menggali lebih dalam mengenai bagaimana pandemi ini mempengaruhi angka pengangguran. Data dari Badan Pusat Statistik (BPS) pada Februari 2021 menunjukkan bahwa 6,36 juta penduduk usia kerja terdampak Covid-19, menurun 1,76 juta orang dibandingkan dengan Agustus 2020. Gambar di bawah menunjukkan gambaran yang lebih jelas mengenai dampak Covid-19 terhadap penduduk usia kerja di Indonesia. Data tersebut dapat membantu pemerintah dalam merumuskan kebijakan yang tepat untuk mengatasi dampak pandemi dan meningkatkan kesejahteraan masyarakat.")


# Image
from PIL import Image

image = Image.open("dampak-covid-19-terhadap-penduduk-usia-kerja.png")
st.image(
    image,
    caption="Badan Pusat Statistik"
)


st.title("Penduduk Bekerja dan Pengangguran Tahun 2019")

df = pd.read_csv("abc.csv")


chart = alt.Chart(df).mark_bar().encode(
    x="Status",
    y="Jumlah",
    color="Status",
    tooltip=["Bulan", "Tahun", "Jumlah"]
)

st.altair_chart(chart, use_container_width=True)
st.caption("Tabel Tahun 2019")
st.table(df)


st.title("Penduduk Bekerja dan Pengangguran Tahun 2023")
df2 = pd.read_csv("abc2023.csv")
chart = alt.Chart(df2).mark_bar().encode(
    x="Status",
    y="Jumlah",
    color="Status",
    tooltip=["Bulan", "Tahun", "Jumlah"]
)

st.altair_chart(chart, use_container_width=True)
st.caption("Tabel Tahun 2023")
st.table(df2)


st.title("Kesimpulan")
st.subheader("Meskipun data pada gambar menunjukkan bahwa jumlah dan persentase pekerja lebih tinggi daripada pengangguran, penting untuk dicatat bahwa tingkat pengangguran di Indonesia masih tergolong tinggi. Sangat diperlukan solusi untuk dapat mengatasi masalah pengangguran secara efektif. Diperlukan juga peran aktif dari berbagai pihak, seperti swasta, akademisi, dan masyarakat sipil untuk bersama-sama mengatasi masalah pengangguran.")


st.caption("__Referensi: Badan Pusat Statistik. (2021, Februari). Dampak Covid-19 terhadap Penduduk Usia Kerja__")

