import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
st.markdown(
    """
    <style>
    /* Target container utama di kolom pertama */
    .stColumn:first-child > div:first-child {
        background-color: #C7DBFF;   /* pink muda */
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
    st.title("Identifikasi dan Pengambilan Data Otomatis (AIDC)")

    # Bagian 1: Definisi AIDC
    with st.container(border=True):
        st.markdown(
            """
            **Automatic Identification and Data Capture (AIDC)** mengacu pada metode 
            mengidentifikasi **individu, objek, gambar, suara** secara otomatis, mengumpulkan 
            data tentangnya, dan memasukkannya langsung ke sistem komputer **tanpa keterlibatan 
            manusia** (tanpa entri data manual).
            """
        )

    # Gambar II.13 placeholder
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-2/fig13.png", use_container_width=True)
        st.caption("Gambar II.13 – Contoh Teknologi AIDC")

    # Bagian 2: Contoh teknologi AIDC
    with st.container(border=True):
        st.markdown(
            """
            ### 🛠️ Contoh Teknologi AIDC
            """
        )

        # Tampilkan dalam dua kolom di dalam container utama agar lebih padat
        col_tech1, col_tech2 = st.columns(2)
        with col_tech1:
            st.markdown(
                """
                - Barcode
                - QR Code
                - RFID (Radio Frequency Identification)
                - Biometrics (iris, facial recognition)
                - Magnetic stripes
                """
            )
        with col_tech2:
            st.markdown(
                """
                - OCR (Optical Character Recognition)
                - Smart card
                - Voice recognition
                """
            )

    # Bagian 3: Cara kerja AIDC
    with st.container(border=True):
        st.markdown(
            """
            ### ⚙️ Cara Kerja AIDC

            Untuk mengambil data, **transduser** akan mengubah gambar aktual atau suara 
            menjadi **file digital**. File tersebut kemudian disimpan dan nantinya dapat:
            - Dianalisis oleh komputer
            - Dibandingkan dengan file lain dalam database untuk memverifikasi identitas
            - Memberikan otorisasi untuk memasuki sistem keamanan
            """
        )

    # Bagian 4: Sektor pemanfaatan
    with st.container(border=True):
        st.markdown(
            """
            ### 🏭 Sektor Pemanfaatan AIDC

            Teknologi AIDC biasanya dimanfaatkan di berbagai sektor, antara lain:
            - Manufaktur
            - Transportasi
            - Distribusi
            - Ritel
            - Kesehatan
            - Dan sebagainya
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi AIDC", expanded=True):
        st.markdown(
            """
            - Identifikasi otomatis individu/objek/gambar/suara.  
            - Pengambilan data langsung ke komputer.  
            - **Tanpa entri data manual**.
            """
        )

    with st.expander("🧩 Contoh Teknologi AIDC"):
        st.markdown(
            """
            - Barcode, QR Code  
            - RFID  
            - Biometrik (wajah, iris)  
            - Magnetic stripe, Smart card  
            - OCR, Voice recognition
            """
        )

    with st.expander("🔁 Cara Kerja"):
        st.markdown(
            """
            Transduser mengubah sinyal fisik (gambar/suara) → file digital → 
            analisis/verifikasi/otorisasi.
            """
        )

    with st.expander("🏭 Sektor Pengguna"):
        st.markdown(
            "Manufaktur, transportasi, distribusi, ritel, kesehatan, dll."
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Teknologi Contoh", "8+ jenis")
        st.metric("Keunggulan", "Otomatis, cepat, akurat")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Materi kuliah / modul AIDC  
            - Sumber terbuka tentang identifikasi otomatis
            """
        )