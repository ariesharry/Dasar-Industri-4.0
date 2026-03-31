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
    st.title("Prinsip Desain Industri 4.0")

    # Pengantar
    with st.container(border=True):
        st.markdown(
            """
            Menurut **Mabkhot dkk (2018)** dan **Hermann dkk (2015)**, prinsip desain Industri 4.0 
            merupakan pedoman bagi perusahaan yang ingin memahami, mengidentifikasi, dan 
            mengimplementasikan proyek-proyek Industri 4.0. Terdapat **6 prinsip** utama:
            """
        )

    # Menampilkan 6 prinsip dalam grid 2 kolom (3 baris)
    col_left, col_right = st.columns(2)

    with col_left:
        with st.container(border=True):
            st.markdown("### 1. Interoperabilitas")
            st.markdown(
                """
                Salah satu kebutuhan perusahaan industri untuk melakukan transformasi industri 4.0 
                adalah menyediakan infrastruktur **Internet of Things (IoT)** dan **Internet of Services (IoS)** 
                termasuk **Cyber-Physical System (CPS)**. CPS merupakan gabungan antara dunia fisik 
                dan virtual. Untuk mengintegrasikan dunia nyata dan virtual dibutuhkan interoperabilitas.
                
                Standar menjadi faktor kunci keberhasilan komunikasi CPS agar mesin/peralatan dari 
                berbagai produsen (*multi vendor*) dapat saling berkomunikasi.
                """
            )

        with st.container(border=True):
            st.markdown("### 3. Desentralisasi")
            st.markdown(
                """
                Dengan meningkatnya permintaan untuk produk individu (kustomisasi), sistem terpusat 
                semakin sulit dikendalikan. Komputer tertanam (*embedded*) pada mesin/peralatan 
                industri 4.0 memungkinkan mereka mengambil keputusan secara mandiri (terdesentralisasi).
                """
            )

        with st.container(border=True):
            st.markdown("### 5. Orientasi Layanan")
            st.markdown(
                """
                Industri 4.0 didasarkan pada arsitektur berorientasi layanan. CPS dapat menawarkan 
                fungsionalitasnya sebagai layanan web. Industri 4.0 ditantang untuk melayani permintaan 
                dengan fokus pada pelanggan (*customer centricity*), serta menghasilkan produk dan 
                layanan bernilai tambah lebih tinggi (mis. personalisasi).
                """
            )

    with col_right:
        with st.container(border=True):
            st.markdown("### 2. Virtualisasi")
            st.markdown(
                """
                Virtualisasi berarti CPS pada industri 4.0 dapat memantau proses fisik dan membuat 
                salinan virtual dunia fisik. Data sensor dari mesin/peralatan pabrik dapat diolah 
                dengan model pabrik virtual dan simulasi untuk optimasi dan pengambilan keputusan.
                """
            )

        with st.container(border=True):
            st.markdown("### 4. Kemampuan Real-time")
            st.markdown(
                """
                Dalam industri 4.0, tugas-tugas pabrik dapat menggunakan data/informasi yang 
                dikumpulkan dan dianalisis secara **real-time**. Status pabrik dilacak dan dianalisis 
                terus menerus, sehingga pabrik dapat bereaksi cepat terhadap kegagalan mesin dan 
                mengubah rute produk ke mesin lain.
                """
            )

        with st.container(border=True):
            st.markdown("### 6. Modularitas")
            st.markdown(
                """
                Modul unit produksi baru dapat ditambahkan pada sistem produksi yang ada dengan 
                prinsip **plug & play**. Dengan sistem modular, industri 4.0 mampu beradaptasi secara 
                fleksibel terhadap perubahan persyaratan dan penggantian atau perluasan modul secara 
                individual.
                """
            )

    # Ringkasan tambahan
    with st.container(border=True):
        st.markdown(
            """
            Keenam prinsip ini menjadi fondasi dalam merancang sistem Industri 4.0 yang tangguh, 
            adaptif, dan berorientasi pada kebutuhan masa depan.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("🔗 1. Interoperabilitas", expanded=True):
        st.markdown(
            """
            - Konektivitas antar mesin multi‑vendor melalui IoT/IoS  
            - Cyber‑Physical System (CPS) menggabungkan fisik dan virtual  
            - Standar komunikasi adalah kunci
            """
        )

    with st.expander("💻 2. Virtualisasi"):
        st.markdown(
            """
            - Pemantauan proses fisik secara virtual  
            - Penggunaan model simulasi untuk optimasi  
            - Pengambilan keputusan berbasis data
            """
        )

    with st.expander("⚙️ 3. Desentralisasi"):
        st.markdown(
            """
            - Keputusan mandiri oleh mesin/peralatan  
            - Embedded computer memungkinkan otonomi  
            - Mendukung kustomisasi produk
            """
        )

    with st.expander("⏱️ 4. Kemampuan Real-time"):
        st.markdown(
            """
            - Pengumpulan dan analisis data secara langsung  
            - Pelacakan status pabrik terus menerus  
            - Respon cepat terhadap gangguan
            """
        )

    with st.expander("🎯 5. Orientasi Layanan"):
        st.markdown(
            """
            - Arsitektur berorientasi layanan (SOA)  
            - Fokus pada pelanggan dan personalisasi  
            - Produk dan layanan bernilai tambah
            """
        )

    with st.expander("🧩 6. Modularitas"):
        st.markdown(
            """
            - Sistem plug & play  
            - Fleksibilitas terhadap perubahan  
            - Penambahan/pergantian modul mudah
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📈 Fakta Singkat")
        st.metric("Jumlah Prinsip", "6")
        st.metric("Tahun Referensi", "2015, 2018")
        st.metric("Fokus Utama", "Interkoneksi & Otonomi")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Mabkhot dkk (2018)  
            - Hermann dkk (2015)
            """
        )