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
    st.title("Perbedaan Artificial Intelligence (AI), Machine Learning (ML), dan Deep Learning (DL)")

    with st.container(border=True):
        st.markdown(
            """
            AI merupakan sistem yang masih manual dan masih harus disetting untuk melaksanakan satu tugas tertentu. Kemudian Marchine Learning adalah suatu program pembelajaran yang berupa saraf neuron yang berfungsi untuk memerintah suatu otak pada komputer yang menyelesaikan masalah tanpa diprogram secara eksplisit akan tetapi memberikan analisis atau kesimpulan yang lebih tepat. Sedangkan, Deep Learning adalah kemampuan sistem yang di setting dengan baik demi meningkatkan kerja pada komputer dan biasanya memperhitungkan data yang tidak eksak, seperti bahasa, suara atau gambar. Untuk mengetahui perbedaan mendasar Artificial Intellegence (AI), Machine Learning (ML), dan Deep Learning (DL) dapat dilihat pada Tabel VIII.1.
            """
        )

        # Tabel VIII.1 Perbedaan AI, ML, DL
        data_tabel = {
            "Aspek": ["Kemunculan", "Definisi", "Hubungan", "Tujuan"],
            "Artificial Intelligence (AI)": [
                "sekitar tahun 1950an",
                "Kecerdasan simulasi dalam mesin",
                "Subset dari data science",
                "Membangun mesin yang mampu berpikir seperti manusia"
            ],
            "Machine Learning (ML)": [
                "sekitar tahun 1960an",
                "Praktik mendapatkan mesin untuk membuat keputusan tanpa diprogram; algoritma belajar dari data",
                "Subset dari data science & AI",
                "Membuat mesin belajar melalui data sehingga dapat memecahkan masalah"
            ],
            "Deep Learning (DL)": [
                "sekitar tahun 1970an",
                "Proses menggunakan Artificial Neural Network untuk memecahkan masalah kompleks; menggunakan banyak jaringan saraf berlapis",
                "Subset dari data science, AI, & ML",
                "Membangun jaringan saraf yang secara otomatis menemukan pola untuk deteksi fitur"
            ]
        }
        df_tabel = pd.DataFrame(data_tabel)
        st.table(df_tabel)

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Ringkasan Perbedaan", expanded=True):
        st.markdown(
            """
            - **AI**: sistem manual, disetting untuk tugas tertentu.
            - **ML**: program pembelajaran, menyelesaikan masalah tanpa diprogram eksplisit.
            - **DL**: kemampuan sistem dengan setting baik untuk data tidak eksak (bahasa, suara, gambar).
            """
        )

    with st.expander("📅 Tahun Kemunculan"):
        st.markdown(
            """
            - AI: 1950an
            - ML: 1960an
            - DL: 1970an
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Hubungan", "DL ⊂ ML ⊂ AI ⊂ Data Science")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Tabel VIII.1 (diolah dari berbagai sumber)
            """
        )