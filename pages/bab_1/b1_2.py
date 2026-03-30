import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
st.markdown(
    """
    <style>
    /* Target container utama di kolom pertama */
    .stColumn:first-child > div:first-child {
        background-color: #7FA8FF;   /* pink muda */
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
    st.title("Model Arsitektur Industri 4.0")

    # Bagian 1: Latar Belakang Perlunya Model Arsitektur
    with st.container(border=True):
        st.markdown(
            """
            Usaha untuk menemukan berbagai aspek pada industri 4.0 tidak cukup hanya 
            memahami definisi industri 4.0. Maka untuk dapat membantu perusahaan lebih 
            memahami posisi saat ini dan kemampuan perusahaan untuk berintegrasi ke dalam 
            perkembangan revolusi industri 4.0 disusunlah model **Reference Architectural 
            Model Industrie 4.0 (RAMI 4.0)**, yaitu model lapisan terstruktur tiga dimensi 
            seperti terlihat pada Gambar I.2 yang dikembangkan oleh **Platform Industrie 4.0** Jerman.
            
            Namun demikian beberapa negara lainnya seperti **Industrial Internet Consortium (IIC)** 
            di Amerika Serikat juga mengembangkan model referensi dengan nama 
            **Industrial Internet Reference Architecture (IIRA)**.
            
            Saat ini kedua konsorsium dari kedua negara tersebut telah mengadakan kolaborasi, 
            masing-masing melakukan pemetaan agar satu sama lain dapat tercipta interoperabilitas 
            *(Shi-Wan Lin, dkk, 2017)*.
            """
        )

    # Bagian 2: Penjelasan RAMI 4.0
    with st.container(border=True):
        st.markdown(
            """
            ### 🧩 RAMI 4.0 – Model Referensi Industri 4.0

            RAMI 4.0 adalah model referensi untuk revolusi industri 4.0 yang telah 
            **distandarisasi** dan digunakan oleh industri manufaktur secara luas di dunia. 
            Model ini memungkinkan semua peserta di revolusi industri 4.0 menggunakan 
            kerangka acuan umum untuk saling bertukar dan memahami.

            Ini adalah kerangka **tiga dimensi** yang mampu menggambarkan semua aspek penting 
            revolusi industri 4.0, di mana hubungan yang kompleks dapat dipecah menjadi 
            kelompok-kelompok kecil dan akan lebih mudah untuk didekati dan diimplementasikan 
            secara bertahap.
            
            RAMI 4.0 mengintegrasikan berbagai standar otomatisasi, seperti 
            **IEC 62890, IEC 62264, IEC 61512**.
            """
        )

    # Gambar I.2 (Placeholder)
    with st.container(border=True):
        st.markdown(
            """
            **Gambar I.2 – RAMI 4.0**  
            *(Ilustrasi: sumbu kanan = tingkat hirarki, sumbu kiri = daur hidup produk & value stream, sumbu vertikal = layer arsitektur)*
            """
        )

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-1/fig2.jpg", use_container_width=True)
        st.caption("Sumber: www.plattform-i40.de (placeholder)")

    # Bagian 3: Tiga Dimensi RAMI 4.0
    with st.container(border=True):
        st.markdown(
            """
            ### 📐 Tiga Dimensi RAMI 4.0
            """
        )

        # Tiga sub‑bagian bisa dibuat dengan tiga kolom atau satu per satu
        col_a, col_b, col_c = st.columns(3)

        with col_a.container(border=True):
            st.markdown(
                """
                **1. Dimensi Tingkat Hirarki**  
                *(sumbu horizontal kanan)*

                Menjelaskan hierarki kendali sistem produksi, dari produk dan peralatan 
                di lantai produksi sampai ke tingkat perusahaan dan dunia luar.

                - Dunia terkoneksi  
                - Enterprise  
                - Work centre  
                - Station (machine)  
                - Control device  
                - Field device  
                - Product

                Merupakan pengembangan dari **IEC 62264** dengan mengintegrasikan 
                *produk* dan *dunia terkoneksi*.
                """
            )

        with col_b.container(border=True):
            st.markdown(
                """
                **2. Dimensi Proses**  
                *(sumbu horizontal kiri)*

                Menunjukkan aliran daur hidup produk atau arus nilai tambah dalam proses 
                produksi yang diiringi digitalisasi (standar **IEC 62890**).

                Dibagi menjadi dua bagian:  
                - **Type** (model): pengembangan (CAD), maintenance usage  
                - **Instance** (produk nyata): production, maintenance usage (service)
                """
            )

        with col_c.container(border=True):
            st.markdown(
                """
                **3. Dimensi Arsitektur (Layer)**  
                *(sumbu vertikal)*

                Enam lapisan yang menunjukkan sudut pandang berbagai aspek industri 
                terhadap Industri 4.0:

                1. Asset  
                2. Integration  
                3. Communication  
                4. Information  
                5. Functional  
                6. Business
                """
            )

    # Bagian 4: Perluasan IEC 62264 (Gambar I.3)
    with st.container(border=True):
        st.markdown(
            """
            ### 🔁 Perluasan Standar IEC 62264 menjadi RAMI 4.0

            Dalam model otomatisasi dan sistem IT standar IEC 62264, produk manufaktur 
            masih terpisah (terisolasi) dengan tingkat atasnya, digambarkan sebagai piramida. 
            Sedangkan dalam Industri 4.0 (RAMI 4.0) digambarkan sebagai **jejaring** dari 
            setiap komponen (proses, perangkat, produk, organisasi, ekosistem) dalam 
            realitas konektivitas di mana‑mana (*ubiquitous connectivity*).

            RAMI 4.0 merupakan perluasan dari hierarki standar IEC 62264, yaitu dengan 
            mengintegrasikan **produk** dengan **dunia yang terkoneksi**.
            """
        )
        # Placeholder gambar I.3
        st.image("https://via.placeholder.com/500x200?text=Perluasan+IEC+62264+ke+RAMI+4.0", use_container_width=True)
        st.caption("Gambar I.3 – Perluasan IEC 62264 menjadi RAMI 4.0  (Sumber: www.plattform-i40.de)")

    # Bagian 5: Detail Dimensi Arsitektur (6 Lapisan)
    with st.container(border=True):
        st.markdown(
            """
            ### 🏗️ Enam Lapisan Arsitektur RAMI 4.0
            """
        )

        # Tabel deskripsi lapisan
        layer_data = {
            "Lapisan": ["Aset", "Integrasi", "Komunikasi", "Informasi", "Fungsional", "Bisnis"],
            "Deskripsi": [
                "Mesin/peralatan, pelanggan, supplier, dan entitas fisik lainnya di dunia nyata.",
                "Link antara dunia fisik dengan digital. Virtualisasi aset (driver, HMI, sensor readers).",
                "Metode standar komunikasi (TCP/IP, HTTP, LAN, WAN, BLE, Wi‑Fi) agar aset saling berkomunikasi.",
                "Menyimpan informasi untuk manajemen, operasi, pelacakan, dan pengendalian aset.",
                "Bertanggung jawab atas production rule, action, processing, system control; fungsionalitas aset tervirtualisasi.",
                "Proses struktur organisasi, produksi, kegiatan bisnis, strategi, lingkungan, dan tujuan bisnis."
            ]
        }
        df_layers = pd.DataFrame(layer_data)
        st.table(df_layers)

    # Bagian 6: Perkembangan Model
    with st.container(border=True):
        st.markdown(
            """
            ### 🔄 Perkembangan Model Arsitektur

            Perlu diketahui bahwa model Arsitektur Industri 4.0 saat ini **masih terus dikembangkan**. 
            Hal ini bertujuan demi terwujudnya model yang secara global dapat digunakan sebagai 
            acuan penerapan Industri 4.0 di berbagai tipe dan level industri.  
            *(Hoedi Prasetyo, dkk, 2018)*
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Apa itu RAMI 4.0?", expanded=True):
        st.markdown(
            """
            - Model referensi arsitektur Industri 4.0  
            - Dikembangkan **Platform Industrie 4.0** Jerman  
            - Berstandar **IEC 62890, 62264, 61512**  
            - Kerangka **tiga dimensi**  
            - Membantu perusahaan memahami posisi dan integrasi ke Industri 4.0
            """
        )

    with st.expander("🌎 Model Lain & Kolaborasi"):
        st.markdown(
            """
            - **IIRA** dari Industrial Internet Consortium (AS)  
            - Kedua konsorsium melakukan **pemetaan** untuk interoperabilitas  
            - Tujuan: model global yang dapat digunakan berbagai tipe industri
            """
        )

    with st.expander("📊 Tiga Dimensi RAMI 4.0"):
        st.markdown(
            """
            1. **Tingkat Hirarki** (produk s.d. dunia terkoneksi) – perluasan IEC 62264  
            2. **Proses** (daur hidup produk: type vs instance) – IEC 62890  
            3. **Arsitektur (layer)** – 6 lapisan dari aset hingga bisnis
            """
        )

    with st.expander("🔩 Enam Lapisan Arsitektur"):
        st.markdown(
            """
            - **Aset** : entitas fisik  
            - **Integrasi** : virtualisasi & konektivitas  
            - **Komunikasi** : protokol dan jaringan  
            - **Informasi** : data manajemen  
            - **Fungsional** : kontrol & aturan produksi  
            - **Bisnis** : organisasi & strategi
            """
        )

    with st.expander("🔄 Perbedaan dengan Model Tradisional"):
        st.markdown(
            """
            - IEC 62264 tradisional: **piramida terisolasi**  
            - RAMI 4.0: **jejaring terintegrasi** (produk terhubung dengan dunia luar)
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📈 Fakta Singkat")
        st.metric("Standar Utama", "IEC 62890, 62264, 61512")
        st.metric("Jumlah Lapisan", "6")
        st.metric("Dimensi", "3")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Shi-Wan Lin, dkk (2017)  
            - Hoedi Prasetyo, dkk (2018)  
            - www.plattform-i40.de  
            - IEC 62264, IEC 62890, IEC 61512
            """
        )