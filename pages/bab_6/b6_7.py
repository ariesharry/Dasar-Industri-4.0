import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .stColumn:first-child > div:first-child {
        background-color: #caf0f8;
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
    st.title("Advanced Analytics (Algorithm, Regression, Decision Trees, Time Series Analysis)")

    with st.container(border=True):
        st.markdown(
            """
            Advanced analytics adalah pemeriksaan data atau konten yang otonom atau semi-otonom menggunakan teknik dan alat-alat canggih, biasanya di luar kecerdasan bisnis tradisional guna menemukan wawasan yang lebih dalam, membuat prediksi, atau menghasilkan rekomendasi. Teknik advanced analytics termasuk penambangan data/teks, pembelajaran mesin, pencocokan pola, perkiraan, visualisasi, analisis semantik, analisis sentimen, analisis jaringan dan klaster, statistik multivariat, analisis grafik, simulasi, pemrosesan peristiwa kompleks, jaringan saraf. Advanced analytics adalah bagian dari data science yang menggunakan metode dan alat-alat tingkat tinggi agar fokus pada proyeksi tren, peristiwa, dan perilaku masa depan dan memberikan kemampuan bagi organisasi untuk menggunakan model statistik lanjut seperti perhitungan "what-if". Area utama advanced analytics adalah analisis data prediktif, big data dan data mining (sisense.com, akses 2019). Analitik ini menggunakan teknik pemodelan canggih untuk memprediksi peristiwa masa depan atau menemukan pola yang tidak dapat dideteksi sebaliknya. Dengan analitik lebih lanjut, maka dapat menjawab pertanyaan "mengapa ini terjadi", "bagaimana jika tren ini berlanjut", "apa yang akan terjadi selanjutnya (prediksi)", "apa yang terbaik yang bisa terjadi (optimisasi)".
            """
        )

    with st.container(border=True):
        st.markdown(
            """
            ### Perbandingan Business Intelligence dan Advanced Analytics
            """
        )
        data_comp = {
            "Aspek": ["Orientasi", "Tipe pertanyaan", "Metode", "Big Data", "Tipe Data", "Generasi Pengetahuan", "Pengguna", "Inisiatif Bisnis"],
            "Business Intelligence (BI)": [
                "Mengukur kinerja masa lalu",
                "Apa yang terjadi, kapan, siapa, berapa banyak",
                "Pelaporan (KPI, matriks), pemantauan, dashboard, OLAP, ad hoc query",
                "Ya",
                "Terstruktur, beberapa tidak terstruktur",
                "Manual",
                "Pengguna bisnis",
                "Reaktif"
            ],
            "Advanced Analytics": [
                "Memprediksi masa depan",
                "Apa yang akan terjadi? Apa yang akan terjadi jika kita mengubah sesuatu? Apa berikutnya?",
                "Model prediktif, data mining, text mining, multimedia mining, model deskriptif, analisis statistik/kuantitatif, simulasi, optimasi",
                "Ya",
                "Terstruktur dan tidak terstruktur",
                "Otomatis",
                "Ilmuwan data, analis bisnis, IT, pengguna bisnis",
                "Proaktif"
            ]
        }
        df_comp = pd.DataFrame(data_comp)
        st.table(df_comp)

    with st.container(border=True):
        st.markdown(
            """
            Advanced analytics sangat penting karena dibutuhkan terutama pada analitik prediktif guna dapat membantu mengungkap masa depan dan mengoptimalkan operasi karena aplikasi business intelligence yang banyak digunakan oleh perusahaan belum dapat menyentuh data yang berpotensi besar untuk meningkatkan aset perusahaan tersebut. Advanced analytics juga dapat digunakan perusahaan untuk mengimbangi persaingan.
            """
        )

with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi Advanced Analytics", expanded=True):
        st.markdown(
            """
            - Analisis otonom/semi-otonom dengan teknik canggih.
            - Di luar BI tradisional.
            - Fokus: prediksi, optimasi, wawasan mendalam.
            """
        )

    with st.expander("🔧 Teknik Advanced Analytics"):
        st.markdown(
            """
            - Data mining, text mining, machine learning.
            - Simulasi, neural networks, analisis multivariat.
            - Analisis sentimen, jaringan, klaster.
            """
        )

    with st.expander("🆚 Perbedaan dengan BI"):
        st.markdown(
            """
            - **BI**: orientasi masa lalu, reaktif, manual.
            - **AA**: orientasi masa depan, proaktif, otomatis.
            """
        )

    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Pertanyaan AA", "Mengapa, bagaimana jika, apa selanjutnya")

    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - sisense.com
            """
        )