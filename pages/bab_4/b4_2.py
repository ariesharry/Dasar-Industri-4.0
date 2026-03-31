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
    st.title("Programmable Logic Controller (PLC) dan Perangkat Pendukung Lainnya")

    # Definisi PLC
    with st.container(border=True):
        st.markdown(
            """
            **Programmable Logic Controller (PLC)** adalah sistem kontrol komputer industri yang terus-menerus
            memonitor keadaan perangkat input dan membuat keputusan berbasis logika untuk mengontrol keadaan
            perangkat output pada proses atau mesin secara otomatis (Gambar IV.3).
            """
        )

    # Gambar IV.3
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-4/fig3.png", use_container_width=True)
        st.caption("Gambar IV.3 – Diagram komponen PLC secara umum (Sumber: vsquareengineering.in)")

    # Perangkat Input
    with st.container(border=True):
        st.markdown(
            """
            ### 📥 Perangkat Input
            - **Switch and Pushbutton**
            - **Sensing Device**:
              - Limit Switch
              - Photoelectric sensor
              - Proximity Sensor
            - **Condition Sensor**:
              - Pressure Switch
              - Level Switch
              - Temperature Switch
              - Vacuum Switch
              - Float Switch
            - **Encoder**
            """
        )

    # Perangkat Output
    with st.container(border=True):
        st.markdown(
            """
            ### 📤 Perangkat Output
            - Valve
            - Motor starter
            - Solenoid
            - Actuator
            - Horn & alarm
            - Stack light
            - Control relay
            - Counter/totalizer
            - Pump
            - Printer
            - Fan
            """
        )

    # Gambar IV.4
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-4/fig4.png", use_container_width=True)
        st.caption("Gambar IV.4 – Modul PLC (Sumber: esuppliersindia.com)")

    # Manfaat PLC
    with st.container(border=True):
        st.markdown(
            """
            ### ⚙️ Manfaat PLC
            Kemampuan untuk **mengubah dan mereplikasi operasi atau proses** sambil mengumpulkan dan
            mengomunikasikan data. PLC disusun secara **modular**, sehingga pengguna dapat mencampur dan
            mencocokkan jenis perangkat input dan output yang paling sesuai dengan aplikasinya.
            """
        )

    # Perangkat pendukung: Programming device & HMI
    with st.container(border=True):
        st.markdown(
            """
            ### 🖥️ Perangkat Pendukung
            Di luar PLC itu sendiri terdapat perangkat pendukung lainnya:
            - **Perangkat pemrograman** (komputer desktop, laptop, tablet). Beberapa PLC memiliki tampilan dan tombol bawaan untuk pemrograman langsung.
            - **Human Machine Interface (HMI)** – menyediakan tingkat abstraksi lebih tinggi, memodelkan sistem kontrol secara keseluruhan.
            """
        )

    # Gambar IV.5
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-4/fig5.png", use_container_width=True)
        st.caption("Gambar IV.5 – Pemanfaatan HMI dalam Sistem")

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi PLC", expanded=True):
        st.markdown(
            """
            - Sistem kontrol industri berbasis komputer.
            - Memonitor input dan mengontrol output secara otomatis berdasarkan logika.
            """
        )

    with st.expander("🔌 Perangkat Input Umum"):
        st.markdown(
            """
            - Switch, Pushbutton
            - Sensor: Limit, Photoelectric, Proximity
            - Condition Sensor: Pressure, Level, Temperature, dll.
            - Encoder
            """
        )

    with st.expander("⚡ Perangkat Output Umum"):
        st.markdown(
            """
            - Valve, Motor starter, Solenoid, Actuator
            - Alarm, Stack light, Relay
            - Counter, Pump, Printer, Fan
            """
        )

    with st.expander("🧩 Keunggulan PLC"):
        st.markdown(
            """
            - Mudah diprogram ulang
            - Modular (I/O dapat disesuaikan)
            - Mengumpulkan dan mengomunikasikan data
            """
        )

    with st.expander("🖱️ Perangkat Pendukung"):
        st.markdown(
            """
            - **Programming device** (komputer, tablet)
            - **HMI** antarmuka manusia-mesin untuk visualisasi dan kontrol
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Fungsi Utama", "Kontrol otomatis berbasis logika")
        st.metric("Komponen I/O", "Input & Output devices")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - vsquareengineering.in
            - esuppliersindia.com
            """
        )