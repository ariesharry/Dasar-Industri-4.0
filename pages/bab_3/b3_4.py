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
    st.title("Otomatisasi dan Klasifikasinya")

    # Definisi dan konsep dasar
    with st.container(border=True):
        st.markdown(
            """
            **Otomatisasi** adalah pendelegasian fungsi kontrol manusia ke peralatan teknis 
            untuk meningkatkan produktivitas, kualitas, mengurangi biaya, dan meningkatkan 
            keselamatan kerja.

            - **Otomasi** (automation) merujuk pada mesin yang dirancang untuk tugas tertentu 
              (misal: mesin pembotolan, pencuci piring, penyemprot cat).
            - **Robot** adalah mesin serbaguna yang dapat melakukan berbagai tugas (misal: 
              lengan pick and place, robot bergerak, mesin CNC).

            Otomatisasi merupakan teknologi yang menggabungkan **mekatronik** dan **komputer** 
            untuk memproduksi barang/jasa secara otomatis dengan bantuan pengontrol.
            """
        )

    # Komponen otomatisasi
    with st.container(border=True):
        st.markdown(
            """
            ### 🔧 Komponen Otomatisasi
            1. **Sensor** – mengukur parameter (suhu, tekanan, aliran, level).
            2. **Transmitter** – mengirim sinyal listrik mentah.
            3. **Sistem Kontrol** – PLC, DCS, PC‑based controller.
            4. **Aktuator** – drive, control valve, dll.
            """
        )

    # Gambar III.4, III.5, III.6
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-3/fig4.png", use_container_width=True)
        st.caption("Gambar III.4 – Otomatisasi pada Industri Proses")

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-3/fig5.png", use_container_width=True)
        st.caption("Gambar III.5 – Sistem Pengendalian Industri 4.0")

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-3/fig6.png", use_container_width=True)
        st.caption("Gambar III.6 – Pemantauan Sistem Pengendalian Proses Industri 4.0 (Sumber: shell.com)")

    # Jenis-jenis otomatisasi
    with st.container(border=True):
        st.markdown(
            """
            ### 📊 Jenis‑Jenis Otomatisasi
            """
        )
        # Tabel jenis otomatisasi
        jenis_data = {
            "Jenis": ["Fixed Automation", "Programmable Automation", "Flexible Automation"],
            "Deskripsi": [
                "Urutan operasi tetap, peralatan khusus (contoh: lini perakitan mekanis).",
                "Dapat diprogram ulang untuk berbagai tugas (contoh: CAD/CAM, mesin CNC, robot).",
                "Fleksibel, dapat menangani variasi produk (contoh: manufacturing cell, FMS, CIM)."
            ]
        }
        df_jenis = pd.DataFrame(jenis_data)
        st.table(df_jenis)

    # Gambar III.7
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-3/fig7.png", use_container_width=True)
        st.caption("Gambar III.7 – Otomatisasi industri")

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi Otomatisasi", expanded=True):
        st.markdown(
            """
            - Pendelegasian fungsi kontrol manusia ke mesin.
            - Tujuan: produktivitas, kualitas, biaya, keselamatan.
            - Otomasi vs Robot: otomasi untuk tugas khusus, robot serbaguna.
            """
        )

    with st.expander("🔩 Komponen Utama"):
        st.markdown(
            """
            1. Sensor
            2. Transmitter
            3. Sistem Kontrol (PLC, DCS, PC)
            4. Aktuator
            """
        )

    with st.expander("📈 Jenis Otomatisasi"):
        st.markdown(
            """
            - **Fixed**: operasi tetap (lini perakitan).
            - **Programmable**: dapat diprogram ulang (CNC, robot).
            - **Flexible**: fleksibel, banyak variasi (FMS, CIM).
            """
        )

    with st.expander("🏭 Penerapan"):
        st.markdown(
            """
            - Industri proses (gambar III.4)
            - Sistem kendali industri 4.0 (gambar III.5, III.6)
            - Otomatisasi pabrik (gambar III.7)
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Komponen", "4")
        st.metric("Jenis Otomatisasi", "3")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - shell.com (gambar III.6)
            - Materi kuliah otomatisasi
            """
        )