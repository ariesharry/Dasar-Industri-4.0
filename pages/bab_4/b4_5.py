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
    st.title("Enterprise Resource Planning (ERP)")

    # Definisi dan tujuan ERP
    with st.container(border=True):
        st.markdown(
            """
            **Enterprise Resource Planning (ERP)** adalah perangkat lunak manajemen proses bisnis yang memungkinkan
            suatu organisasi untuk menggunakan sistem aplikasi terintegrasi guna mengelola bisnis dan mengotomatisasi
            banyak fungsi *back office* terkait teknologi, layanan, dan sumber daya manusia.
            """
        )

    # Gambar IV.9 Contoh modul ERP
    with st.container(border=True):
        st.markdown("### 📦 Contoh Modul-modul ERP")
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-4/fig9.png", use_container_width=True)
        st.caption("Gambar IV.9 – Contoh modul-modul ERP (Sumber: layout.alimb.us)")

    # Penjelasan integrasi ERP
    with st.container(border=True):
        st.markdown(
            """
            Perangkat lunak ERP biasanya mengintegrasikan semua aspek operasi – termasuk **perencanaan produk,
            pengembangan, produksi, penjualan dan pemasaran** – dalam satu basis data, aplikasi, dan antarmuka pengguna.
            ERP Suite yang lengkap juga mencakup **manajemen kinerja perusahaan**, yang membantu merencanakan,
            menganggarkan, memprediksi, dan melaporkan hasil keuangan organisasi. Laporan disajikan dalam visualisasi
            yang menarik dan mudah dianalisis.
            """
        )

    # Gambar IV.10 Visualisasi kinerja perusahaan
    with st.container(border=True):
        st.markdown("### 📊 Visualisasi Kinerja Perusahaan")
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-4/fig10.png", use_container_width=True)
        st.caption("Gambar IV.10 – Visualisasi Kinerja Perusahaan dengan Modul-modul ERP (Sumber: datapine.com)")

    # Tujuan dasar ERP
    with st.container(border=True):
        st.markdown(
            """
            **Tujuan dasar** menggunakan sistem ERP adalah menyediakan satu pusat penyimpanan untuk semua informasi
            yang dibagikan oleh semua aspek ERP, sehingga meningkatkan aliran data di seluruh organisasi.
            Sistem ERP menghilangkan duplikasi data dan menyediakan **satu sumber kebenaran** dengan integritas data.
            """
        )

    # Keuntungan open source ERP
    with st.container(border=True):
        st.markdown(
            """
            ### 🌐 Keuntungan Open Source ERP
            Saat ini banyak tersedia sistem ERP komersial, namun sistem ERP *open source* juga tersedia dalam jumlah
            yang tidak sedikit. Penggunaan *open source* ERP tidak berarti mengurangi mutu sistem, bahkan memberikan
            banyak keuntungan:
            1. **Biaya murah** – tidak ada lisensi dan biaya perawatan sistem.
            2. **Lebih mudah di-upgrade** dan dapat dilakukan lebih sering dibandingkan ERP komersial.
            3. **Antarmuka lebih mudah disesuaikan** dengan kebutuhan.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi ERP", expanded=True):
        st.markdown(
            """
            - Perangkat lunak manajemen proses bisnis terintegrasi.
            - Mengotomatisasi fungsi back office (SDM, keuangan, dll).
            """
        )

    with st.expander("🧩 Modul Umum ERP"):
        st.markdown(
            """
            - Perencanaan produk
            - Pengembangan
            - Produksi
            - Penjualan & pemasaran
            - Manajemen kinerja (anggaran, prediksi, laporan)
            """
        )

    with st.expander("🎯 Tujuan ERP"):
        st.markdown(
            """
            - Satu pusat data terintegrasi.
            - Menghilangkan duplikasi data.
            - Satu sumber kebenaran (single source of truth).
            """
        )

    with st.expander("💡 Keuntungan Open Source ERP"):
        st.markdown(
            """
            - Biaya rendah (tanpa lisensi).
            - Upgrade lebih mudah dan sering.
            - Kustomisasi antarmuka sesuai kebutuhan.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Fungsi Utama", "Integrasi proses bisnis")
        st.metric("Jenis ERP", "Komersial & Open Source")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - layout.alimb.us
            - datapine.com
            """
        )