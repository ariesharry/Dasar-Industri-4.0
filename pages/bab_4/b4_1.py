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
    st.title("Piramida Otomatisasi")

    # Pengertian piramida otomatisasi
    with st.container(border=True):
        st.markdown(
            """
            Piramida otomasi adalah representasi bergambar dari berbagai tingkat otomasi dalam sebuah pabrik.
            Piramida ini menjelaskan secara visual bagaimana teknologi diintegrasikan dalam industri.
            Pada era revolusi industri 3.0 (sebelum industri 4.0), piramida otomatisasi digambarkan seperti pada
            Gambar V.1 dan dijelaskan pada Tabel IV.1 berikut.
            """
        )

    # Tabel IV.1 Piramida Otomatisasi
    with st.container(border=True):
        st.markdown("### 📊 Tabel IV.1 Piramida Otomatisasi")
        data_tabel = {
            "Tingkat": ["0 – Lapangan/Proses Produksi", "1 – Kontrol/Sensing-Manipulasi", "2 – Pemantauan dan Pengawasan", "3 – Perencanaan Manajemen Operasi"],
            "Uraian": [
                "Level ini memiliki perangkat, aktuator, dan sensor di lapangan (field) atau lantai produksi. Contoh: motor listrik, aktuator hidrolik/pneumatik, sakelar, sensor fotolistrik.",
                "Level ini memuat PLC (Programmable Logic Controller) dan PID controller. Pekerja mengontrol perangkat level 0 berdasarkan informasi sensor.",
                "Level ini menggunakan SCADA (Supervisory Control and Data Acquisition) dengan antarmuka HMI untuk memonitor dan mengontrol beberapa sistem dari satu lokasi.",
                "Level ini menggunakan MES (Manufacturing Execution System) untuk memonitor seluruh proses dari bahan baku hingga produk jadi, membantu manajemen mengambil keputusan real-time."
            ]
        }
        df_tabel = pd.DataFrame(data_tabel)
        st.table(df_tabel)

    # Gambar IV.1 Piramida Otomatisasi Tradisional
    with st.container(border=True):
        st.image("https://via.placeholder.com/600x400?text=Gambar+IV.1+-+Piramida+Otomatisasi+Tradisional", use_container_width=True)
        st.caption("Gambar IV.1 – Piramida Otomatisasi Tradisional (Sumber: www.plattform-i40.de)")

    # Perkembangan komunikasi antar level
    with st.container(border=True):
        st.markdown(
            """
            ### 🔄 Komunikasi Antar Level pada Era Industri 4.0
            Dalam perkembangan saat ini, level-level pada piramida otomatisasi saling berkomunikasi (Gambar IV.2)
            menggunakan beberapa jenis protokol, di antaranya:
            - **MQTT (Message Queuing Telemetry Transport)** – protokol ringan berbasis client-server (broker). Client dapat *publish* data ke broker, dan client lain dapat *subscribe* untuk menerima data.
            - **OPC UA (Open Protocol Communication Unified Architecture)** – protokol yang akan dijelaskan kemudian.
            """
        )

    # Gambar IV.2 Pertukaran data
    with st.container(border=True):
        st.image("https://via.placeholder.com/600x300?text=Gambar+IV.2+-+Pertukaran+data+pada+setiap+tingkat+otomatisasi", use_container_width=True)
        st.caption("Gambar IV.2 – Pertukaran data pada setiap tingkat otomatisasi (Sumber: Springer)")

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Piramida Otomatisasi", expanded=True):
        st.markdown(
            """
            - Representasi tingkat otomasi di pabrik.
            - Terdiri dari 4 level (0 hingga 3) pada era industri 3.0.
            """
        )

    with st.expander("📋 Empat Level"):
        st.markdown(
            """
            **Level 0** – Lapangan: sensor, aktuator.  
            **Level 1** – Kontrol: PLC, PID.  
            **Level 2** – Supervisi: SCADA, HMI.  
            **Level 3** – Manajemen: MES.
            """
        )

    with st.expander("🌐 Protokol Komunikasi"):
        st.markdown(
            """
            - **MQTT**: protokol ringan, publish/subscribe.
            - **OPC UA**: arsitektur terpadu untuk komunikasi industri.
            """
        )

    with st.expander("🔄 Perubahan Era 4.0"):
        st.markdown(
            """
            Level-level saling terhubung dan bertukar data secara real-time, tidak lagi hierarkis kaku.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Jumlah Level", "4")
        st.metric("Protokol Umum", "MQTT, OPC UA")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - www.plattform-i40.de
            - Springer (link)
            """
        )