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
    st.title("Open Protocol Communication Unified Architecture (OPC-UA)")

    # Definisi OPC UA
    with st.container(border=True):
        st.markdown(
            """
            **OPC Unified Architecture (OPC UA)** adalah protokol komunikasi mesin ke mesin untuk otomasi industri
            yang dikembangkan oleh **OPC Foundation**. OPC UA adalah standar yang memfasilitasi pertukaran data antara
            PLC, HMI, server, klien, dan mesin lainnya untuk keperluan interkonektivitas dan aliran informasi.
            Jenis komunikasi ini penting dalam pabrik karena banyak jenis peralatan yang mengukur parameter proses,
            menghasilkan data, atau merekam data.
            """
        )

    # Platform yang didukung
    with st.container(border=True):
        st.markdown(
            """
            ### ⚙️ Platform yang Didukung OPC UA
            OPC UA berfungsi pada berbagai platform, antara lain:
            - **Platform perangkat keras**: PC tradisional, server berbasis cloud, PLC, mikrokontroler (ARM, dll.)
            - **Sistem Operasi**: Microsoft Windows, Apple OSX, Android, distribusi Linux, dll.

            OPC UA menyediakan infrastruktur untuk **interoperabilitas** di seluruh perusahaan, dari mesin-ke-mesin,
            mesin-ke-perusahaan, dan segala sesuatu di antaranya.
            """
        )

    # Peran OPC UA dalam Industri 4.0
    with st.container(border=True):
        st.markdown(
            """
            ### 🌐 OPC UA dan Industri 4.0
            OPC UA merupakan salah satu protokol komunikasi terpenting untuk **Industri 4.0 dan IoT**.
            Dengan OPC UA, akses ke mesin, perangkat, dan sistem lain distandarisasi, memungkinkan pertukaran data
            yang seragam dan tidak tergantung pabrik.
            """
        )

    # Gambar IV.13
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-4/fig14.png", use_container_width=True)
        st.caption("Gambar IV.13 – Pemanfaatan Protokol OPC UA dalam rangka integrasi vertikal dan horizontal (Sumber: fn8group.com)")

    # Keunggulan OPC UA
    with st.container(border=True):
        st.markdown(
            """
            ### ✅ Keunggulan OPC UA
            OPC UA dapat digunakan dengan mudah, pertukaran data aman, dapat mengakomodasi sistem lama (*legacy system*)
            serta infrastruktur yang ada, dan memungkinkan skalabilitas.

            **Alasan utama OPC UA akan terus diadopsi dalam industri manufaktur:**
            1. Memungkinkan mendukung **manufaktur cerdas** (*smart manufacturing*).
            2. Berkontribusi pada **pengurangan kompleksitas** komunikasi antar perangkat dan mesin, sehingga meningkatkan efisiensi pabrik.
            3. Dapat mengakomodasi **sistem lama** (*legacy system*), permesinan baru, dan lini produk dengan mudah.
            4. **Lintas platform**.
            5. **Bukan format eksklusif** (*non-proprietary*).
            6. Dapat menerima dan menginterpretasikan **beberapa titik data dari berbagai sumber**.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Apa itu OPC UA?", expanded=True):
        st.markdown(
            """
            - Protokol komunikasi mesin-ke-mesin untuk otomasi industri.
            - Standar dari OPC Foundation.
            - Memfasilitasi pertukaran data antar perangkat (PLC, HMI, server, dll).
            """
        )

    with st.expander("💻 Platform Didukung"):
        st.markdown(
            """
            - Hardware: PC, cloud, PLC, mikrokontroler.
            - OS: Windows, OSX, Android, Linux.
            """
        )

    with st.expander("🔗 Peran dalam Industri 4.0"):
        st.markdown(
            """
            - Protokol kunci untuk Industri 4.0 dan IoT.
            - Menstandarisasi akses data antar perangkat.
            - Mendukung interoperabilitas.
            """
        )

    with st.expander("✅ Keunggulan"):
        st.markdown(
            """
            1. Mendukung smart manufacturing.
            2. Mengurangi kompleksitas komunikasi.
            3. Akomodasi sistem lama dan baru.
            4. Lintas platform.
            5. Non-proprietary.
            6. Multi-sumber data.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Pengembang", "OPC Foundation")
        st.metric("Peran Utama", "Interoperabilitas industri")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - fn8group.com
            - OPC Foundation
            """
        )