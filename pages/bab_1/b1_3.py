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
    st.title("Karakteristik Industri 4.0")

    # Bagian 1: Pengantar dari BCG
    with st.container(border=True):
        st.markdown(
            """
            Menurut perusahaan Amerika **Boston Consulting Group (BCG)**, saat ini kita berada di 
            tengah-tengah gelombang keempat kemajuan teknologi dengan munculnya teknologi industri 
            digital baru yang dikenal sebagai **Industri 4.0**, yaitu sebuah transformasi yang didukung 
            oleh **sembilan kemajuan teknologi dasar (kunci)**.

            Dalam transformasi tersebut, sensor, mesin, benda kerja, dan sistem teknologi informasi 
            akan terhubung di sepanjang rantai nilai di luar satu perusahaan. Sistem yang terhubung ini 
            (disebut juga *cyber-physical system*) dapat berinteraksi satu sama lain menggunakan 
            standar protokol berbasis internet dan menganalisis data untuk memprediksi kegagalan, 
            mengkonfigurasi diri mereka sendiri, dan beradaptasi dengan perubahan.

            Industri 4.0 memungkinkan pengumpulan dan analisis data di seluruh mesin, menghasilkan 
            proses yang lebih cepat, lebih fleksibel, dan lebih efisien untuk memproduksi barang 
            berkualitas lebih tinggi dengan biaya lebih rendah. Hal ini pada gilirannya akan 
            meningkatkan produktivitas manufaktur, menggeser ekonomi, mendorong pertumbuhan industri, 
            dan memodifikasi profil tenaga kerja, pada akhirnya mengubah daya saing perusahaan dan 
            wilayah *(Rüßmann dkk, 2015)*.
            """
        )

    # Bagian 2: Gambar I.4 (placeholder)
    with st.container(border=True):
        st.markdown(
            """
            **Gambar I.4 – Sembilan Teknologi pada Industri 4.0**  
            *(Sumber: BCG, 2015)*
            """
        )

        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:
            st.image("assets/bab-1/fig1.png", use_container_width=True)

    # Bagian 3: Tabel I.2 Rangkuman Teknologi
    with st.container(border=True):
        st.markdown(
            """
            ### 📋 Tabel I.2 – Rangkuman Konsep Teknologi yang Mendukung Industri 4.0
            Berdasarkan laporan BCG, sembilan teknologi dasar tersebut dapat dirangkum sebagai berikut:
            """
        )

        # Data tabel
        data_teknologi = {
            "Konsep Teknologi": [
                "Big Data & Analytics",
                "Autonomous Robot",
                "Simulation",
                "Horizontal & Vertical Integration",
                "Internet of Things (IoT)",
                "Cloud Computing",
                "Additive Manufacturing",
                "Augmented Reality (AR)",
                "Cyber Security"
            ],
            "Uraian Penjelasan": [
                "Analisis data yang memanfaatkan kumpulan data besar (big data) dapat mengoptimalkan kualitas produksi, menghemat energi, dan meningkatkan layanan mesin/peralatan.",
                "Robot menjadi lebih otonom, fleksibel, dan kooperatif. Dapat berinteraksi satu sama lain, bekerja aman berdampingan dengan manusia, dan belajar dari mereka.",
                "Simulasi 3D dengan data real time digunakan sebagai cerminan dunia fisik untuk menguji dan mengoptimalkan pengaturan mesin sebelum perubahan fisik.",
                "Integrasi vertikal dalam pabrik dan horizontal pada rantai pasok membuat perusahaan, departemen, dan fungsi menjadi lebih kohesif dengan jaringan data universal.",
                "IoT memungkinkan perangkat lapangan berkomunikasi dan berinteraksi satu sama lain serta dengan pengendali terpusat, mendesentralisasi analisis dan keputusan.",
                "Penggunaan cloud untuk data dan fungsionalitas mesin semakin luas, memungkinkan lebih banyak layanan berbasis data untuk sistem produksi.",
                "Metode additive manufacturing digunakan untuk menghasilkan produk dengan desain kompleks dan ringan, mengurangi biaya transportasi dan persediaan.",
                "AR mendukung layanan seperti pemilihan suku cadang dan instruksi perbaikan melalui perangkat seluler, meningkatkan pengambilan keputusan pekerja.",
                "Dengan meningkatnya konektivitas, kebutuhan perlindungan sistem industri dari ancaman siber meningkat drastis; komunikasi aman dan manajemen akses menjadi penting."
            ],
            "Contoh": [
                "Pabrikan semikonduktor Infineon Technologies mengidentifikasi pola dari analisis data untuk mendeteksi chip rusak di awal produksi.",
                "Kuka, perusahaan robot Eropa, menawarkan robot otonom yang dapat berinteraksi satu sama lain.",
                "Siemens dan vendor mesin perkakas Jerman mengembangkan mesin virtual yang mensimulasikan pemesinan komponen dengan data dari mesin fisik.",
                "Dassault Systèmes dan BoostAeroSpace meluncurkan platform kolaborasi untuk industri kedirgantaraan Eropa yang mengelola pertukaran data produk.",
                "Bosch Rexroth melengkapi fasilitas produksi katup dengan proses semi-otomatis dan terdesentralisasi; produk diidentifikasi dengan RFID.",
                "Vendor Manufacturing Execution System (MES) mulai menawarkan solusi berbasis cloud.",
                "Perusahaan industri dirgantara menggunakan AM untuk desain baru yang mengurangi berat pesawat dan biaya bahan baku seperti titanium.",
                "Pekerja dapat menerima instruksi perbaikan melalui kacamata AR (Google Glass) yang menampilkan informasi kebutuhan perbaikan langsung pada sistem.",
                "Beberapa vendor peralatan industri bergabung dengan perusahaan cyber security melalui kemitraan atau akuisisi."
            ]
        }

        df_teknologi = pd.DataFrame(data_teknologi)
        st.dataframe(df_teknologi, use_container_width=True, hide_index=True)
        st.caption("Sumber: diolah dari BCG (2015)")

    # Bagian 4: Penutup / catatan
    with st.container(border=True):
        st.markdown(
            """
            Sembilan teknologi tersebut menjadi fondasi utama transformasi Industri 4.0, 
            mendorong terciptanya pabrik cerdas yang terhubung, adaptif, dan efisien.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Intisari Industri 4.0 versi BCG", expanded=True):
        st.markdown(
            """
            - Didukung **9 teknologi kunci**  
            - Menghubungkan sensor, mesin, benda kerja, dan sistem IT di sepanjang rantai nilai  
            - Menciptakan **cyber-physical system** yang saling berinteraksi  
            - Tujuan: proses lebih cepat, fleksibel, efisien, produk berkualitas, biaya rendah  
            - Dampak: peningkatan produktivitas, pertumbuhan industri, perubahan tenaga kerja
            """
        )

    # Sembilan teknologi dalam expander terpisah
    with st.expander("📊 1. Big Data & Analytics"):
        st.markdown(
            """
            **Uraian:** Analisis big data untuk optimasi kualitas, hemat energi, dan layanan mesin.  
            **Contoh:** Infineon mendeteksi chip rusak lebih awal.
            """
        )
    with st.expander("🤖 2. Autonomous Robot"):
        st.markdown(
            """
            **Uraian:** Robot otonom, fleksibel, kooperatif, bekerja bersama manusia.  
            **Contoh:** Kuka dengan robot yang saling berinteraksi.
            """
        )
    with st.expander("🖥️ 3. Simulation"):
        st.markdown(
            """
            **Uraian:** Simulasi 3D real-time untuk menguji dan optimasi sebelum perubahan fisik.  
            **Contoh:** Siemens mengembangkan mesin virtual.
            """
        )
    with st.expander("🔗 4. Horizontal & Vertical Integration"):
        st.markdown(
            """
            **Uraian:** Integrasi di dalam pabrik (vertikal) dan lintas rantai pasok (horizontal).  
            **Contoh:** Dassault dan BoostAeroSpace platform kolaborasi.
            """
        )
    with st.expander("🌐 5. Internet of Things (IoT)"):
        st.markdown(
            """
            **Uraian:** Komunikasi antar perangkat lapangan dan pengendali terpusat, analisis terdesentralisasi.  
            **Contoh:** Bosch Rexroth dengan identifikasi RFID dan workstation adaptif.
            """
        )
    with st.expander("☁️ 6. Cloud Computing"):
        st.markdown(
            """
            **Uraian:** Data dan fungsionalitas mesin di cloud, layanan berbasis data.  
            **Contoh:** Vendor MES menawarkan solusi cloud.
            """
        )
    with st.expander("🖨️ 7. Additive Manufacturing"):
        st.markdown(
            """
            **Uraian:** Produksi dengan desain kompleks, ringan, mengurangi biaya transportasi.  
            **Contoh:** Industri dirgantara menggunakan titanium dengan AM.
            """
        )
    with st.expander("🥽 8. Augmented Reality (AR)"):
        st.markdown(
            """
            **Uraian:** Informasi real-time untuk pemilihan suku cadang, instruksi perbaikan.  
            **Contoh:** Kacamata AR (Google Glass) untuk panduan perbaikan.
            """
        )
    with st.expander("🔒 9. Cyber Security"):
        st.markdown(
            """
            **Uraian:** Perlindungan sistem industri dari ancaman siber, komunikasi aman.  
            **Contoh:** Kemitraan vendor industri dengan perusahaan keamanan siber.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📈 Fakta Singkat")
        st.metric("Jumlah Teknologi Kunci", "9")
        st.metric("Tahun Laporan BCG", "2015")
        st.metric("Dampak Utama", "Produktivitas Meningkat")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - BCG (2015)  
            - Rüßmann dkk (2015)  
            - Infineon, Kuka, Siemens, Bosch, Dassault, dll.
            """
        )