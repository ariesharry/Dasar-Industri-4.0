import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .stColumn:first-child > div:first-child {
        background-color: #C7DBFF;
        border-radius: 20px;
        padding: 20px;
        
    }
    .stColumn:first-child .stContainer {
        background-color: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)

cols = st.columns([0.7, 0.3])

with cols[0].container(border=True):
    st.title("Data Science")

    with st.container(border=True):
        st.markdown(
            """
            Menurut Kotu & Deshpande (2019), data science adalah kumpulan teknik yang digunakan untuk mengekstraksi nilai dari data. Ilmu ini sangat penting bagi organisasi mana pun yang mengumpulkan, menyimpan, dan memproses data sebagai bagian dari operasinya. Teknik ilmu data (Data science) bergantung pada menemukan pola, koneksi, dan hubungan yang berguna dalam data. Ilmu data juga biasa disebut sebagai penemuan pengetahuan, pembelajaran mesin, analisis prediktif, dan penambangan data. Namun, setiap istilah memiliki konotasi yang sedikit berbeda tergantung pada konteksnya. Beberapa teknik yang digunakan dalam data science ditelusuri menggunakan statistik terapan, pembelajaran mesin, visualisasi, logika, dan ilmu komputer. Secara umum, data science adalah penggalian atau bisa juga disebut mengekstrak data agar dapat difilter serta didapatkan data yang benar untuk menghasilkan produk data yang sebenar-benarnya. Data science berfokus pada pemanfaatan data untuk prediksi, eksplorasi, pemahaman, dan intervensi. Studi ini juga memberikan prioritas kepada pengetahuan tentang algoritma optimasi dengan mengelola trade-off yang diperlukan antara kecepatan dan akurasi. Data science mengacu pada bidang pekerjaan yang terkait dengan pengumpulan, persiapan, analisis, visualisasi, manajemen, dan pelestarian koleksi informasi yang besar. Meskipun data science cenderung terhubung dengan database dan ilmu komputer, namun dibutuhkan juga keterampilan lain seperti keterampilan non-matematika. Gambar VI.6 mewakili lima tahap siklus hidup data science.
            """
        )

    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-6/fig6.png", use_container_width=True)
        st.caption("Gambar VI.6 Siklus Hidup Data Science (Sumber: datascience.berkeley.edu)")

    with st.container(border=True):
        st.markdown(
            """
            Secara tradisional, data sekarang ini sebagian besar terstruktur dan berukuran kecil, yang dapat dianalisis dengan menggunakan alat Business Intelligence (BI) sederhana. Tidak seperti data dalam sistem tradisional yang sebagian besar terstruktur, saat ini sebagian besar data tidak terstruktur atau semi-terstruktur.
            """
        )

with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi Data Science", expanded=True):
        st.markdown(
            """
            - Kumpulan teknik untuk mengekstrak nilai dari data.
            - Fokus pada pola, koneksi, hubungan.
            - Digunakan untuk prediksi, eksplorasi, pemahaman, intervensi.
            """
        )

    with st.expander("🔄 Siklus Hidup Data Science"):
        st.markdown(
            """
            - Tahapan: capture, process, analyze, communicate.
            - Iteratif, melibatkan berbagai keterampilan.
            """
        )

    with st.expander("📊 Data Modern"):
        st.markdown(
            """
            - Sebagian besar data tidak terstruktur.
            - Membutuhkan teknik analisis lebih kompleks dibanding BI tradisional.
            """
        )

    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Fokus Utama", "Prediksi, Eksplorasi")

    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Kotu & Deshpande (2019)
            - datascience.berkeley.edu
            """
        )