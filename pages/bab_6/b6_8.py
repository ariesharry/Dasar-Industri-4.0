import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .stColumn:first-child > div:first-child {
        background-color: #FBEFEF;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
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
    st.title("Tingkatan Analisis")

    with st.container(border=True):
        st.markdown(
            """
            Sebagian besar organisasi menganalisis rantai pasokan mereka menggunakan laporan dan indikator kinerja utama (KPI) untuk menentukan apa yang terjadi. Bentuk dasar analisis rantai pasokan ini dikenal sebagai **Analisis Deskriptif**. Banyak organisasi telah menggunakan data warehouse dan sistem intelijen bisnis (BI) sebagai alat untuk mendiagnosis "apa yang terjadi" dan "mengapa". Pengguna analitik yang lebih matang dan maju telah berupaya untuk mengubah data menjadi wawasan prediktif dan preskriptif. Seiring waktu, perusahaan berevolusi dari menggunakan laporan dan metrik berwawasan ke belakang ke kemampuan pengambilan keputusan berwawasan ke depan yang menyarankan rencana tindakan yang optimal dan menambah nilai lebih signifikan.
            """
        )

    with st.container(border=True):
        st.image("https://via.placeholder.com/600x200?text=Gambar+VI.8+-+Tingkatan+Analisis", use_container_width=True)
        st.caption("Gambar VI.8 Tingkatan Analisis")

    with st.container(border=True):
        st.markdown(
            """
            Bagi produsen, membuka kunci potensi data lama, data real time, dan data tidak terstruktur untuk membuat keputusan yang digunakan menyeimbangkan kualitas dan hasil pada era Industri 4.0 sangatlah penting. Rata-rata situs yang berjalan lebih dari seratus aplikasi perangkat lunak, memiliki tantangan yang luar biasa untuk membuat data tersebut dapat diakses dan ditindaklanjuti (actionable). Manufaktur kognitif menyatukan jutaan titik data di seluruh sistem, peralatan, dan proses untuk mendapatkan wawasan (insight) yang bisa ditindaklanjuti (actionable) di seluruh rantai nilai, dimulai dari desain produk hingga operasi hingga customer support. Manufaktur kognitif menemukan pola dan menjawab pertanyaan di seluruh pabrik tentang pengguna, peralatan, lokasi, streaming data sensor dan sebagainya.

            Guna mendukung semua tingkat analisis pada industri maka diperlukan lima kemampuan:

            1. **Kemampuan deskriptif** dalam bentuk Laporan & Dashboard, Clustering & Association, Pattern Based Analysis.
            2. **Kemampuan diagnostik** seperti analisis akar permasalahan, simulasi, analisis what-if, dan segmentasi.
            3. **Kemampuan prediktif**, seperti simulasi, skenario what-if, kurva sensitivitas, dan perkiraan statistik.
            4. **Kemampuan preskriptif** berupa optimasi deterministik dan stochastic, dan tradeoffs.
            5. **Kemampuan kognitif**, seperti pembelajaran mesin, resolusi otomatis, kecerdasan buatan, dan penasihat cerdas.
            """
        )

with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📊 Analisis Deskriptif", expanded=True):
        st.markdown(
            """
            - Menjawab "apa yang terjadi".
            - Menggunakan laporan, KPI, dashboard.
            """
        )

    with st.expander("🔍 Analisis Diagnostik"):
        st.markdown(
            """
            - Menjawab "mengapa terjadi".
            - Menggunakan root cause analysis, simulasi, segmentasi.
            """
        )

    with st.expander("🔮 Analisis Prediktif"):
        st.markdown(
            """
            - Menjawab "apa yang akan terjadi".
            - Menggunakan simulasi, perkiraan statistik.
            """
        )

    with st.expander("✅ Analisis Preskriptif"):
        st.markdown(
            """
            - Menjawab "apa yang harus dilakukan".
            - Menggunakan optimasi, trade-offs.
            """
        )

    with st.expander("🧠 Analisis Kognitif"):
        st.markdown(
            """
            - Menggunakan AI, machine learning.
            - Menghasilkan rekomendasi cerdas.
            """
        )

    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Jumlah Tingkatan", "5")

    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Shi‑Nash & Hardoon (2017)
            """
        )