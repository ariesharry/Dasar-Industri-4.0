import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
st.markdown(
    """
    <style>
    .stColumn:first-child > div:first-child {
        background-color: #7FA8FF;
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
    st.title("Supervisory Control and Data Acquisition (SCADA)")

    # Definisi dan fungsi SCADA
    with st.container(border=True):
        st.markdown(
            """
            **SCADA** adalah sistem perangkat lunak dan perangkat keras yang memungkinkan organisasi industri untuk:
            1. **Kontrol** proses industri secara lokal atau di lokasi terpencil (*remote*)
            2. **Memantau, mengumpulkan, dan memproses data** real-time
            3. **Berinteraksi langsung** dengan perangkat seperti sensor, katup, pompa, motor melalui perangkat lunak HMI
            4. **Merekam peristiwa** ke dalam file log

            Sistem SCADA sangat penting karena membantu menjaga **efisiensi**, memproses data untuk keputusan yang lebih cerdas,
            dan mengomunikasikan masalah sistem untuk membantu mengurangi **waktu henti** (*down time*).
            """
        )

    # Arsitektur dasar SCADA
    with st.container(border=True):
        st.markdown(
            """
            ### 🏗️ Arsitektur Dasar SCADA

            Arsitektur dasar SCADA dimulai dengan **PLC** atau **Remote Terminal Units (RTU)**. PLC dan RTU adalah mikrokomputer
            yang berkomunikasi dengan berbagai objek seperti mesin pabrik, HMI, sensor, dan perangkat akhir, kemudian merutekan
            informasi ke komputer dengan perangkat lunak SCADA. Perangkat lunak SCADA memproses, mendistribusikan, dan menampilkan
            data, membantu operator menganalisis data dan membuat keputusan.
            """
        )

    # Gambar IV.6
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-4/fig6.png", use_container_width=True)
        st.caption("Gambar IV.6 – Diagram Sistem SCADA (Sumber: clue.club)")

    # Gambar IV.7
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-4/fig7.png", use_container_width=True)
        st.caption("Gambar IV.7 – Contoh Pengendalian Proses dengan Sistem SCADA dengan Tablet (Sumber: inductiveautomation.com)")

    # Perbandingan SCADA dan DCS
    with st.container(border=True):
        st.markdown(
            """
            ### 🔄 SCADA vs DCS (Distributed Control System)

            Ketika mengotomatisasi proses manufaktur, baik DCS maupun SCADA sangat penting untuk platform otomatisasi yang komprehensif.

            | Aspek | SCADA | DCS |
            |-------|-------|-----|
            | **Fokus Utama** | Didorong oleh peristiwa, memprioritaskan pengumpulan data | Operasi tingkat proses |
            | **Skalabilitas** | Lebih terukur dan fleksibel, dapat digunakan untuk satu atau beberapa pabrik tanpa batasan geografis | Ideal untuk mengendalikan operasi di satu fasilitas atau pabrik |
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi SCADA", expanded=True):
        st.markdown(
            """
            - Sistem software + hardware untuk kontrol dan monitoring industri.
            - Memungkinkan kontrol lokal/remote, pengumpulan data real-time, interaksi dengan perangkat, dan logging.
            """
        )

    with st.expander("🔧 Komponen Utama"):
        st.markdown(
            """
            - **PLC/RTU**: mikrokomputer yang berkomunikasi dengan perangkat lapangan.
            - **Perangkat lunak SCADA**: memproses dan menampilkan data.
            - **HMI**: antarmuka manusia-mesin.
            - **Sensor, katup, pompa, motor**: perangkat yang dikendalikan.
            """
        )

    with st.expander("🆚 SCADA vs DCS"):
        st.markdown(
            """
            - **SCADA**: event-driven, fokus pengumpulan data, sangat skalabel (multi-site).
            - **DCS**: fokus kontrol proses, ideal untuk satu pabrik.
            """
        )

    with st.expander("📈 Manfaat SCADA"):
        st.markdown(
            """
            - Menjaga efisiensi
            - Pengambilan keputusan lebih cerdas
            - Mengurangi downtime dengan deteksi dini masalah
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Komponen Kunci", "PLC, RTU, HMI")
        st.metric("Fungsi Utama", "Kontrol, Monitoring, Logging")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - clue.club
            - inductiveautomation.com
            """
        )