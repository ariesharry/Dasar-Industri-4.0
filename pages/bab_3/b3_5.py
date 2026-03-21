import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
st.markdown(
    """
    <style>
    /* Target container utama di kolom pertama */
    .stColumn:first-child > div:first-child {
        background-color: #FBEFEF;   /* pink muda */
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
    st.title("Aplikasi Robot untuk Berbagai Otomatisasi pada Industri Manufaktur")

    # Bagian 1: Robot industri tradisional vs cobot
    with st.container(border=True):
        st.markdown(
            """
            ### 🏭 Robot Industri: Tradisional vs Collaborative Robot (Cobot)

            **Robot industri** adalah robot manufaktur yang diprogram untuk melakukan fungsi‑fungsi industri dalam proses diskrit.

            - **Robot tradisional** menangani muatan ringan hingga berat, beroperasi dengan kecepatan tinggi, akurasi dan pengulangan tinggi. Aplikasi: pengelasan, pengecatan, pengecoran, penanganan material, perakitan.
            - **Cobot (collaborative robot)** dapat bekerja aman bersama manusia tanpa kandang pelindung. Dilengkapi sensor canggih, perangkat lunak, dan EOAT untuk menghindari cedera. Biasanya memiliki 6 atau 7 sumbu.
            """
        )

    # Gambar III.8, III.9, III.10
    with st.container(border=True):
        st.image("https://via.placeholder.com/600x200?text=Gambar+III.8+-+Aplikasi+Robot+dalam+Industri", use_container_width=True)
        st.caption("Gambar III.8 – Aplikasi Robot dalam Industri")

        st.image("https://via.placeholder.com/600x200?text=Gambar+III.9+-+Aplikasi+Robot+untuk+Welding", use_container_width=True)
        st.caption("Gambar III.9 – Aplikasi Robot untuk Welding (Sumber: genesis-systems.com)")

        st.image("https://via.placeholder.com/600x200?text=Gambar+III.10+-+Aplikasi+Robot+pada+Industri+Perakitan+Mobil", use_container_width=True)
        st.caption("Gambar III.10 – Aplikasi Robot pada Industri Perakitan Mobil (Sumber: eulixe.com)")

    # Bagian 2: Cobot lebih detail
    with st.container(border=True):
        st.markdown(
            """
            ### 🤝 Collaborative Robot (Cobot)

            Konsep manusia dan robot bekerja bahu‑membahu bukan hal baru. Cobot memungkinkan interaksi fisik dan kolaborasi dengan pekerja manusia.

            **Aplikasi cobot:**
            - Pick & place
            - Packaging & palletizing
            - Quality inspection
            - Process task
            """
        )

    # Gambar III.11, III.12, III.13
    with st.container(border=True):
        st.image("https://via.placeholder.com/600x200?text=Gambar+III.11+-+Collaborative+Robot+(Cobot)+UR3", use_container_width=True)
        st.caption("Gambar III.11 – Collaborative Robot (Cobot) – UR3 Robot, PT JVC Electronics Indonesia (Sumber: universal-robots.com)")

        st.image("https://via.placeholder.com/600x200?text=Gambar+III.12+-+Axis+Robot", use_container_width=True)
        st.caption("Gambar III.12 – Axis robot (Sumber: giatuinhanh.vn)")

        st.image("https://via.placeholder.com/600x200?text=Gambar+III.13+-+Macam-macam+bentuk+cobot", use_container_width=True)
        st.caption("Gambar III.13 – Macam-macam bentuk cobot (Sumber: zhuanlan.zhihu.com)")

    # Bagian 3: Investasi robot berdasarkan sasaran
    with st.container(border=True):
        st.markdown(
            """
            ### 💡 Investasi Robot Berdasarkan Sasaran Efisiensi

            Kebutuhan jenis investasi robot tergantung pada sasaran peningkatan efisiensi:
            """
        )

        # Tabel sasaran dan solusi
        investasi_data = {
            "Sasaran": [
                "Mengurangi biaya manufaktur",
                "Mengurangi biaya quality assurance (QA)",
                "Pemenuhan pesanan lebih cepat",
                "Administrasi back‑office lebih cepat",
                "Mengurangi waktu permintaan pesanan"
            ],
            "Solusi Robot": [
                "Lini produksi dengan robotic arm",
                "Sistem inspeksi dengan machine vision",
                "Warehouse robot",
                "Robotic Process Automation (RPA)",
                "Platform layanan pelanggan otomatis"
            ]
        }
        df_investasi = pd.DataFrame(investasi_data)
        st.table(df_investasi)

    # Bagian 4: RPA dan AI
    with st.container(border=True):
        st.markdown(
            """
            ### 🤖 Robotic Process Automation (RPA) dan AI

            **RPA** adalah fitur otomatisasi proses cerdas yang menggambarkan robot yang digerakkan oleh logika, mengeksekusi aturan terprogram pada data terstruktur.

            Tingkat inteligensia antara RPA dan AI diilustrasikan pada gambar berikut.
            """
        )
        st.image("https://via.placeholder.com/600x250?text=Gambar+III.14+-+Intelligent+Automation", use_container_width=True)
        st.caption("Gambar III.14 – Intelligent automation: dari RPA (process‑driven) ke ML/AI (data‑driven)")

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Robot Tradisional vs Cobot", expanded=True):
        st.markdown(
            """
            - **Tradisional**: kecepatan tinggi, akurasi, untuk tugas berat (las, cat, dll), perlu kandang.
            - **Cobot**: bekerja bersama manusia, sensor canggih, aman tanpa kandang, aplikasi pick&place, inspeksi, dll.
            """
        )

    with st.expander("🔧 Aplikasi Cobot"):
        st.markdown(
            "Pick & place, packaging, palletizing, quality inspection, process task."
        )

    with st.expander("💼 Investasi Robot"):
        st.markdown(
            """
            - **Robotic arm** → biaya manufaktur turun.
            - **Machine vision** → QA lebih murah.
            - **Warehouse robot** → pemenuhan pesanan cepat.
            - **RPA** → administrasi lebih cepat.
            - **Platform otomatis** → layanan pelanggan.
            """
        )

    with st.expander("📈 RPA vs AI"):
        st.markdown(
            """
            - **RPA**: process‑driven, aturan terprogram, data terstruktur.
            - **AI/ML**: data‑driven, pembelajaran, data tak terstruktur.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Robot Tradisional", "kecepatan & akurasi")
        st.metric("Cobot", "kolaborasi aman")
        st.metric("RPA", "otomatisasi proses administrasi")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - genesis-systems.com
            - eulixe.com
            - universal-robots.com
            - zhuanlan.zhihu.com
            """
        )