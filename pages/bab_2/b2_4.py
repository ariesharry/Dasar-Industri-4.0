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
    st.title("Karakteristik Internet of Things")

    # Bagian pengantar
    with st.container(border=True):
        st.markdown(
            """
            Melalui penerapan konsep teknologi IoT dengan interkoneksi antara dunia fisik 
            dengan dunia maya – baik melalui eksploitasi identifikasi, pengambilan data, 
            pengolahan data, dan kemampuan dalam berkomunikasi – membuka peluang baru 
            dalam dimensi IoT untuk **mengakses apapun, setiap saat dan dari tempat manapun**.
            
            Berikut adalah karakteristik utama IoT:
            """
        )

    # Karakteristik 1: Dinamis dan beradaptasi
    with st.container(border=True):
        st.markdown(
            """
            ### 🔄 1. Dinamis dan Beradaptasi dengan Sendiri
            Perangkat dan sistem IoT dapat memiliki kemampuan untuk **beradaptasi secara dinamis** 
            dengan perubahan konteks dan mengambil tindakan berdasarkan kondisi operasinya, 
            konteks pengguna, atau lingkungan penginderaan.
            """
        )

    # Karakteristik 2: Konfigurasi Diri
    with st.container(border=True):
        st.markdown(
            """
            ### ⚙️ 2. Konfigurasi Diri
            Perangkat IoT mungkin memiliki kemampuan **konfigurasi sendiri** (self‑configuring), 
            memungkinkan sejumlah besar perangkat bekerja bersama untuk menyediakan fungsionalitas 
            tertentu seperti pengaturan jaringan, atau mengambil pembaruan (*fetch*) perangkat lunak terbaru.
            """
        )

    # Karakteristik 3: Protokol Komunikasi yang Interoperable
    with st.container(border=True):
        st.markdown(
            """
            ### 🌐 3. Protokol Komunikasi yang Interoperable
            Perangkat IoT dapat mendukung sejumlah **protokol komunikasi yang dapat dioperasikan** 
            (interoperable), begitu juga dengan infrastruktur yang ada. Hal ini memungkinkan perangkat 
            dari berbagai vendor dan teknologi untuk saling berkomunikasi secara lancar.
            """
        )

    # Penutup (opsional)
    with st.container(border=True):
        st.markdown(
            """
            Karakteristik di atas menjadikan IoT sebagai teknologi yang fleksibel, tangguh, 
            dan mampu berintegrasi dengan ekosistem digital yang semakin kompleks.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Karakteristik IoT", expanded=True):
        st.markdown(
            """
            **1. Dinamis & Adaptif**  
            → Beradaptasi dengan perubahan konteks & lingkungan.

            **2. Konfigurasi Diri**  
            → Perangkat dapat mengatur diri sendiri, update software, dll.

            **3. Protokol Interoperable**  
            → Mendukung berbagai protokol komunikasi agar dapat terintegrasi.
            """
        )

    with st.expander("💡 Mengapa Karakteristik Ini Penting?"):
        st.markdown(
            """
            - **Adaptif**: IoT dapat merespons kondisi real‑time.  
            - **Self‑configuring**: Memudahkan pengelolaan perangkat dalam skala besar.  
            - **Interoperabilitas**: Memastikan perangkat dari berbagai produsen dapat bekerja sama.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Jumlah Karakteristik Utama", "3")
        st.metric("Fokus Utama", "Adaptif, Mandiri, Terintegrasi")

    # Referensi (umum)
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Materi kuliah / modul IoT  
            - Berbagai sumber literatur IoT
            """
        )