import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
st.markdown(
    """
    <style>
    /* Target container utama di kolom pertama */
    .stColumn:first-child > div:first-child {
        background-color: #caf0f8;   /* pink muda */
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

# ================== KOLOM MATERI UTAMA ==================
with cols[0].container(border=True):
    st.title("Arsitektur Internet of Things")

    # Pengantar
    with st.container(border=True):
        st.markdown(
            """
            Menurut **Zhang dan Yu** (dalam Soumyalatha & Hegde, S.G., 2016), arsitektur IoT 
            diklasifikasikan menjadi **empat lapisan** seperti yang ditunjukkan pada Gambar II.8.
            """
        )

    # Gambar II.8 placeholder
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-2/fig8.png", use_container_width=True)
        st.caption("Gambar II.8 – Arsitektur Internet of Things (Sumber: Soumyalatha & Hegde, S.G., 2016)")

    # Lapisan 1: Sensor Layer
    with st.container(border=True):
        st.markdown(
            """
            ### 📡 1. Lapisan Sensor (Sensor Layer)
            Ini adalah lapisan terendah arsitektur IoT, terdiri dari:
            - Jaringan sensor
            - Sistem tertanam (*embedded systems*)
            - Tag RFID dan pembaca
            - Sensor lunak lainnya

            Masing-masing sensor ini memiliki **identifikasi** dan **penyimpanan informasi**.
            """
        )

    # Lapisan 2: Gateway and Network Layer
    with st.container(border=True):
        st.markdown(
            """
            ### 🌐 2. Lapisan Gerbang dan Jaringan (Gateway and Network Layer)
            Bertanggung jawab untuk **mentransfer informasi** yang dikumpulkan oleh sensor 
            ke lapisan berikutnya. Didukung protokol universal standar yang **skalabel** dan 
            **fleksibel** untuk mentransfer data dari perangkat heterogen (berbagai jenis node sensor).  
            Layer ini harus memiliki kinerja tinggi dan jaringan yang kuat.
            """
        )

    # Lapisan 3: Management Service Layer
    with st.container(border=True):
        st.markdown(
            """
            ### 🗂️ 3. Lapisan Layanan Manajemen (Management Service Layer)
            Bertindak sebagai **antarmuka dua arah** antara lapisan gateway‑jaringan dan lapisan aplikasi.
            Bertanggung jawab atas:
            - Manajemen perangkat
            - Manajemen informasi
            - Menangkap sejumlah besar data mentah dan mengekstraksi informasi relevan secara **real‑time**.
            """
        )

    # Lapisan 4: Application Layer
    with st.container(border=True):
        st.markdown(
            """
            ### 💻 4. Lapisan Aplikasi (Application Layer)
            Lapisan teratas IoT yang menyediakan **antarmuka pengguna** untuk mengakses berbagai aplikasi.
            Aplikasi dapat digunakan di berbagai sektor, seperti:
            - Transportasi
            - Perawatan kesehatan
            - Pertanian
            - Rantai pasokan
            - Pemerintah
            - Ritel, dan lain‑lain.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Empat Lapisan Arsitektur IoT", expanded=True):
        st.markdown(
            """
            1. **Sensor Layer** – perangkat keras penginderaan (sensor, RFID, embedded system).  
            2. **Gateway & Network Layer** – transfer data, protokol universal, kinerja tinggi.  
            3. **Management Service Layer** – manajemen perangkat & informasi, ekstraksi data real‑time.  
            4. **Application Layer** – antarmuka pengguna untuk berbagai sektor.
            """
        )

    with st.expander("🔁 Aliran Data"):
        st.markdown(
            """
            Sensor → Gateway & Network → Management Service → Application  
            *(dan sebaliknya untuk kontrol/konfigurasi)*
            """
        )

    with st.expander("🏭 Contoh Sektor Aplikasi"):
        st.markdown(
            "Transportasi, Kesehatan, Pertanian, Rantai Pasok, Pemerintah, Ritel"
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Jumlah Lapisan", "4")
        st.metric("Sumber", "Zhang & Yu, 2016")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Soumyalatha & Hegde, S.G. (2016) – *"Internet of Things: Architectures, Protocols and Applications"*  
            - Zhang & Yu (dalam Soumyalatha & Hegde, 2016)
            """
        )