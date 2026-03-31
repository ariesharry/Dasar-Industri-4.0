import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
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

# ================== KOLOM MATERI UTAMA ==================
with cols[0].container(border=True):
    st.title("Cyber Physical Systems (CPS) based Automation")

    # Pengantar transformasi piramida otomatisasi
    with st.container(border=True):
        st.markdown(
            """
            Piramida otomatisasi tradisional mengalami transformasi menuju **Industri 4.0** dengan memanfaatkan teknologi
            **cloud computing**, seperti terlihat pada Gambar IV.11a dan Gambar IV.11b.
            """
        )

    # Gambar IV.11a
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-4/fig11.png", use_container_width=True)
        st.caption("Gambar IV.11a – Perubahan Piramida Otomatisasi (Rev.Ind.3.0) ke Otomatisasi Industri 4.0 (Sumber: foodengineeringmag.com)")

    # Gambar IV.11b
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-4/fig12.png", use_container_width=True)
        st.caption("Gambar IV.11.b – Otomatisasi Industri 4.0 berbasis Cloud (Sumber: www.plattform-i40.de)")

    # Penjelasan level cloud
    with st.container(border=True):
        st.markdown(
            """
            Pada gambar tersebut muncul tingkat baru yaitu **tingkat 5 cloud** yang menggabungkan semua tingkat otomatisasi
            sebelumnya dengan cloud untuk membangun transformasi digital Industri 4.0. Dengan konektivitas ke cloud,
            data dari tingkat mana pun dapat langsung dimasukkan ke dalam **data lake** atau aplikasi lain (misal MES/ERP),
            bahkan wawasan (*insights*) juga dapat diperoleh langsung. Di sinilah tingkat efisiensi dan keunggulan operasional
            berikutnya tercapai. Dengan konektivitas cloud, perusahaan dapat melakukan **integrasi vertikal maupun horizontal**
            lebih mudah dibandingkan era industri sebelumnya.
            """
        )

    # Integrasi Horizontal dan Vertikal
    with st.container(border=True):
        st.markdown(
            """
            ### 🔗 Integrasi Horizontal dan Vertikal

            Industri 4.0 memperkuat pentingnya integrasi horizontal dan vertikal, menjadikannya tulang punggung *smart factory*.

            **Integrasi Horizontal** berarti menciptakan jaringan kolaboratif yang mulus dan terpusat data di seluruh rantai pasokan
            organisasi. Terjadi di beberapa tingkatan:
            - Di lantai produksi: mesin dan unit produksi saling terhubung, mengomunikasikan status, merespons mandiri terhadap
              persyaratan dinamis, memungkinkan produksi lot size satu dan pengurangan downtime melalui pemeliharaan prediktif.
            - Di berbagai fasilitas produksi: data fasilitas dibagi secara mulus, tugas produksi dapat dialihkan antar fasilitas.
            - Di seluruh rantai pasokan: transparansi data dan kolaborasi otomatis dengan pemasok dan penyedia layanan.

            **Integrasi Vertikal** menyatukan semua lapisan logis dalam organisasi dari lapisan lapangan (lantai produksi) hingga
            R&D, jaminan kualitas, manajemen produk, TI, penjualan, pemasaran, dll. Data mengalir bebas dan transparan ke atas dan
            ke bawah, memungkinkan keputusan strategis dan taktis digerakkan oleh data. Perusahaan yang terintegrasi vertikal
            merespons dengan gesit terhadap perubahan pasar.
            """
        )

    # Gambar IV.12
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-4/fig13.png", use_container_width=True)
        st.caption("Gambar IV.12 – CPS pada Integrasi Vertikal dan Horizontal")

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Transformasi Piramida", expanded=True):
        st.markdown(
            """
            - Tambahan level **Cloud** (level 5) pada piramida.
            - Data dari semua level dapat langsung masuk ke cloud.
            - Memudahkan integrasi vertikal & horizontal.
            """
        )

    with st.expander("🔁 Integrasi Horizontal"):
        st.markdown(
            """
            - Kolaborasi di lantai produksi (machine-to-machine).
            - Kolaborasi antar fasilitas produksi.
            - Kolaborasi di seluruh rantai pasokan.
            - Tujuan: produksi fleksibel, respons cepat, pengurangan downtime.
            """
        )

    with st.expander("📊 Integrasi Vertikal"):
        st.markdown(
            """
            - Menyatukan semua lapisan organisasi (lantai produksi hingga pemasaran).
            - Aliran data transparan ke atas/bawah.
            - Keputusan strategis berbasis data.
            - Respons gesit terhadap perubahan pasar.
            """
        )

    with st.expander("☁️ Peran Cloud"):
        st.markdown(
            """
            - Sentralisasi data.
            - Konektivitas langsung ke MES/ERP.
            - Analitik real-time dan insights.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Level Baru", "Cloud (level 5)")
        st.metric("Integrasi", "Horizontal & Vertikal")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - foodengineeringmag.com
            - www.plattform-i40.de
            """
        )