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
    st.title("Manufacturing Execution System (MES)")

    # Definisi dan tujuan MES
    with st.container(border=True):
        st.markdown(
            """
            **Manufacturing Execution System (MES)** adalah sistem informasi yang menghubungkan, memantau, dan mengontrol
            sistem manufaktur dan aliran data yang kompleks di lantai pabrik.

            **Tujuan utama MES** adalah memastikan pelaksanaan operasi manufaktur yang efektif dan meningkatkan hasil produksi.
            MES melacak dan mengumpulkan data real-time yang akurat tentang siklus hidup produksi lengkap,
            mulai dari rilis pesanan hingga tahap pengiriman produk jadi.
            """
        )

    # Data yang dikumpulkan MES
    with st.container(border=True):
        st.markdown(
            """
            **Data yang dikumpulkan MES:**
            - Silsilah produk
            - Kinerja
            - Keterlacakan (traceability)
            - Manajemen material
            - Pekerjaan dalam proses (Work-in-Process / WIP)
            - Aktivitas pabrik lainnya secara real-time

            Data ini memungkinkan pembuat keputusan memahami kondisi lantai pabrik dan mengoptimalkan proses produksi.
            """
        )

    # MESA-11 dan fungsi inti MES
    with st.container(border=True):
        st.markdown(
            """
            ### 📋 Model MESA-11
            **Manufacturing Enterprise Solutions Association (MESA) International** mendefinisikan ruang lingkup MES
            melalui model **MESA-11** (1997) yang mencakup 11 fungsi inti MES.
            """
        )

        # Tabel 11 fungsi MES
        fungsi_mes = {
            "No": list(range(1, 12)),
            "Fungsi Inti MES": [
                "Resource Allocation & Status",
                "Dispatching Production",
                "Data Collection/Acquisition",
                "Quality Management",
                "Maintenance Management",
                "Performance Analysis",
                "Operations/Detail Scheduling",
                "Document Control",
                "Labor Management",
                "Process Management",
                "Product Tracking & Genealogy"
            ]
        }
        df_mes = pd.DataFrame(fungsi_mes)
        st.table(df_mes)

    # Gambar IV.8 Modul-modul MES
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-4/fig8.png", use_container_width=True)
        st.caption("Gambar IV.8 – Modul-modul pada Manufacturing Execution System (Sumber: MESA International)")

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Apa itu MES?", expanded=True):
        st.markdown(
            """
            - Sistem informasi untuk memantau dan mengontrol manufaktur.
            - Menghubungkan data real-time dari lantai pabrik.
            - Tujuan: efektivitas operasi, peningkatan hasil produksi.
            """
        )

    with st.expander("📊 Data yang Dikelola MES"):
        st.markdown(
            """
            - Silsilah produk, kinerja, keterlacakan
            - Material, WIP, aktivitas pabrik
            """
        )

    with st.expander("🧩 11 Fungsi Inti MES (MESA-11)"):
        st.markdown(
            """
            1. Resource Allocation & Status  
            2. Dispatching Production  
            3. Data Collection  
            4. Quality Management  
            5. Maintenance Management  
            6. Performance Analysis  
            7. Operations Scheduling  
            8. Document Control  
            9. Labor Management  
            10. Process Management  
            11. Product Tracking & Genealogy
            """
        )

    with st.expander("🏭 Manfaat MES"):
        st.markdown(
            """
            - Optimalisasi produksi
            - Pengambilan keputusan berbasis data
            - Pelacakan produk end-to-end
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Fungsi Inti", "11 (MESA-11)")
        st.metric("Tahun Model", "1997")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - MESA International
            - Sumber industri manufaktur
            """
        )