import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
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

# ================== KOLOM MATERI UTAMA ==================
with cols[0].container(border=True):
    st.title("Definisi Komputasi Awan")

    # Definisi dasar
    with st.container(border=True):
        st.markdown(
            """
            **Komputasi awan (cloud computing)** adalah istilah umum untuk layanan yang di‑host melalui internet.
            Data dan program disimpan serta diakses via internet, bukan dari hard drive komputer lokal (*on‑premise*).
            Aplikasi berjalan di server pusat data dan tampil sama seperti di komputer lokal. Semua file tersimpan
            di server dan dapat diakses kapan saja dengan koneksi internet. Nama "cloud" terinspirasi dari simbol
            awan yang mewakili internet dalam diagram.
            """
        )

    # Cara kerja
    with st.container(border=True):
        st.markdown(
            """
            ### ⚙️ Cara Kerja
            Cloud computing menggunakan internet sebagai server pengolah data. Pengguna login ke internet,
            terhubung ke program tanpa instalasi. Infrastruktur (penyimpanan, instruksi) disimpan secara virtual,
            perintah diteruskan ke server aplikasi, diproses, dan hasilnya ditampilkan sebagai halaman yang diperbarui.
            """
        )

    # Komponen / istilah terkait
    with st.container(border=True):
        st.markdown(
            """
            ### 🧩 Komponen Utama dalam Cloud
            - **Cloud server** : server virtual berbasis internet, data aman walau perangkat hilang.
            - **Virtual desktop** : desktop kerja dalam bentuk virtual (VDI), diakses dengan model client‑server.
            - **Platform software** : sistem operasi atau kerangka kerja untuk menjalankan aplikasi.
            - **Applications** : perangkat lunak untuk tugas khusus (hiburan, bisnis, produktivitas).
            - **Storage/data** : penyimpanan file online (cloud storage) seperti Google Drive.
            """
        )

    # Contoh layanan cloud populer
    with st.container(border=True):
        st.markdown(
            """
            ### 📦 Contoh Layanan Cloud
            - **Google Drive** – penyimpanan online 5GB gratis, akses dari berbagai perangkat, kolaborasi.
            - **Windows Azure** – sistem operasi cloud dari Microsoft untuk mengembangkan dan mengatur aplikasi.
            - **Amazon Web Services (AWS)** – platform sebagai layanan (PaaS) terkemuka.
            - **Git & GitHub** – kontrol versi dan repositori berbasis cloud untuk kolaborasi pengembangan.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi", expanded=True):
        st.markdown(
            """
            - Penyimpanan & akses data via internet.
            - Tidak bergantung pada hard drive lokal.
            - Nama berasal dari simbol awan di diagram.
            """
        )

    with st.expander("⚙️ Cara Kerja"):
        st.markdown(
            """
            - Login via internet → perintah ke server → proses → hasil tampil.
            - Tanpa instalasi aplikasi di lokal.
            """
        )

    with st.expander("🧩 Komponen"):
        st.markdown(
            """
            - Cloud server, virtual desktop, platform software, aplikasi, storage.
            """
        )

    with st.expander("📦 Contoh Layanan"):
        st.markdown(
            """
            - Google Drive, Azure, AWS, GitHub.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Istilah Kunci", "On‑premise vs Cloud")
        st.metric("Contoh Storage", "Google Drive")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Modul Industri 4.0 Dasar
            - datamation.com
            """
        )