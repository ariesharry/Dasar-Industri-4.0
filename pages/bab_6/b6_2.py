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
    st.title("Structured Data dan Unstructured Data")

    with st.container(border=True):
        st.markdown(
            """
            Big data dapat datang dalam berbagai bentuk, termasuk data terstruktur (structured data) dan data tidak terstruktur (unstructured data). Menurut Dietrich, D. (2015), structured data adalah data yang berisi tipe data, format, dan struktur yang didefinisikan seperti data pada spreadsheet sederhana, data transaksi, OLAP, file CSV. Gambar VI.2 merupakan contoh data terstruktur, yaitu berupa data beban listrik yang terlayani oleh suatu perusahaan jasa penyedia listrik dalam rentang per setengah jam setiap harinya selama satu bulan dengan satuan MW. Data menjelaskan pemakaian beban listrik yang terpakai pada kelompok siang hari dan malam hari serta rata-rata pemakaian beban setiap harinya.
            """
        )

    with st.container(border=True):
        st.image("https://via.placeholder.com/600x200?text=Gambar+VI.2+-+Contoh+Data+Terstruktur", use_container_width=True)
        st.caption("Gambar VI.2 Contoh Data Terstruktur")

    with st.container(border=True):
        st.markdown(
            """
            Unstructured data adalah data yang tidak memiliki struktur yang melekat, yang dapat mencakup dokumen teks, PDF, gambar, dan video. Sebagian besar data yang ada pada big data adalah unstructured data sehingga butuh perlakuan lebih lanjut dan khusus dalam mengolahnya guna menghasilkan informasi yang lebih bernilai. Contoh unstructured data yang dihasilkan manusia adalah text files, email, social media, website, mobile data, komunikasi, media dan aplikasi bisnis. Contoh unstructured data yang dihasilkan mesin antara lain satellite imagery, scientific data, digital surveillance dan sensor data.

            Tren data pada Gambar VI.3 menunjukkan bahwa pada tahun 2020, lebih dari 80% data merupakan data tidak terstruktur.
            """
        )

    with st.container(border=True):
        st.image("https://via.placeholder.com/600x150?text=Gambar+VI.3+-+Perkembangan+Data", use_container_width=True)
        st.caption("Gambar VI.3 Perkembangan Data (Sumber: Sharma)")

with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Data Terstruktur", expanded=True):
        st.markdown(
            """
            - Format dan tipe data terdefinisi.
            - Contoh: spreadsheet, CSV, data transaksi.
            - Mudah diolah dengan alat tradisional.
            """
        )

    with st.expander("📌 Data Tidak Terstruktur"):
        st.markdown(
            """
            - Tidak memiliki struktur baku.
            - Contoh: teks, PDF, gambar, video, sensor data.
            - Dominan (>80% dari total data).
            - Memerlukan teknik khusus untuk pengolahan.
            """
        )

    with st.expander("📊 Tren Data"):
        st.markdown(
            """
            - Proporsi data tidak terstruktur terus meningkat.
            - Pada 2020 mencapai lebih dari 80%.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Data Tidak Terstruktur (2020)", ">80%")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Dietrich, D. (2015)
            - Sharma, H. (2019)
            """
        )