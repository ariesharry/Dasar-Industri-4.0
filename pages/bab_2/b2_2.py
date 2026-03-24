import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
st.markdown(
    """
    <style>
    /* Target container utama di kolom pertama */
    .stColumn:first-child > div:first-child {
        background-color: #caf0f8;   /* pink muda */
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
    st.title("Definisi, Konsep, dan Pilar Internet of Things")

    # Bagian 1: Definisi IoT (Hung, 2017)
    with st.container(border=True):
        st.markdown(
            """
            ### 📌 Definisi Internet of Things

            Menurut **Hung, M. (2017)** – Wakil Presiden Gartner Research –  
            *Internet of Things (IoT)* adalah **jaringan objek fisik khusus** yang mengandung 
            **teknologi tertanam** (*embedded technology*) untuk berkomunikasi, merasakan 
            (*sensing*), atau berinteraksi dengan keadaan internal atau lingkungan eksternal.

            Jaringan ini menghubungkan **aset, proses, dan personel**, memungkinkan 
            pengambilan data dan peristiwa, sehingga perusahaan dapat mempelajari perilaku, 
            melakukan tindakan pencegahan, atau menambah bahkan mengubah proses bisnisnya.
            """
        )

    # Bagian 2: Konsep Kerja IoT
    with st.container(border=True):
        st.markdown(
            """
            ### ⚙️ Konsep Kerja IoT

            IoT berkembang dari konvergensi **teknologi nirkabel**, 
            **micro‑electromechanical systems (MEMS)**, dan **internet**.

            Tiga elemen utama dalam konsep kerja IoT (sumber: mobnasesemka.com):
            1. **Barang fisik** yang dilengkapi modul IoT.
            2. **Perangkat koneksi ke internet** seperti modem dan router wireless.
            3. **Cloud Data Center** tempat menyimpan aplikasi beserta database.
            """
        )

        # Gambar II.3 (placeholder)
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-2/fig3.png", use_container_width=True)
        st.caption("Gambar II.3 – Konsep Kerja IoT (Sumber: mobnasesemka.com)")

        # Gambar II.4 (placeholder)
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-2/fig4.png", use_container_width=True)
        st.caption("Gambar II.4 – Mekanisme Kerja IoT")

        st.markdown(
            """
            Seluruh penggunaan barang yang terhubung ke internet akan menyimpan data. 
            Data tersebut terkumpul sebagai **big data** yang kemudian dapat diolah 
            untuk dianalisis. Hasilnya dimanfaatkan bagi kepentingan masing‑masing 
            perusahaan/instansi untuk menemukan pengetahuan baru beserta solusinya.
            """
        )

    # Bagian 3: Contoh Sistem IoT
    with st.container(border=True):
        st.markdown(
            """
            ### 🏭 Contoh Sistem IoT

            Ekosistem IoT terdiri dari **perangkat pintar** berkemampuan web yang menggunakan 
            prosesor tertanam, sensor, dan perangkat keras komunikasi untuk mengumpulkan, 
            mengirim, dan bertindak berdasarkan data dari lingkungan.

            - Perangkat IoT berbagi data sensor dengan menghubungkan ke **gateway IoT** 
              atau perangkat tepi lainnya, lalu data dikirim ke **cloud** untuk dianalisis.
            - Perangkat juga dapat berkomunikasi langsung dengan perangkat terkait dan 
              bertindak berdasarkan informasi yang diperoleh.
            - Sebagian besar pekerjaan dilakukan **tanpa campur tangan manusia**, meskipun 
              manusia dapat berinteraksi (mengatur, memberi instruksi, mengakses data).
            """
        )
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-2/fig5.png", use_container_width=True)
        st.caption("Gambar II.5 – Contoh Sistem IoT")

    # Bagian 4: Empat Pilar IoT
    with st.container(border=True):
        st.markdown(
            """
            ### 🧱 Empat Pilar IoT (Khan, H.M., 2018)

            IoT memiliki empat pilar utama:
            """
        )

        # Tampilkan dalam bentuk grid atau tabel
        pilar_data = {
            "Pilar": [
                "**Machine to Machine (M2M)**",
                "**Radio Frequency IDentification (RFID)**",
                "**Wireless Sensor Network (WSN)**",
                "**Supervisory Control And Data Acquisition (SCADA)**"
            ],
            "Deskripsi": [
                "Menggunakan perangkat untuk menangkap peristiwa melalui koneksi jaringan ke server pusat, yang menerjemahkan peristiwa menjadi informasi bermakna.",
                "Menggunakan gelombang radio untuk mentransfer data dari tag elektronik yang dilampirkan ke suatu objek ke sistem pusat melalui pembaca, untuk tujuan identifikasi dan pelacakan.",
                "Terdiri dari sensor otonom yang didistribusikan secara spasial untuk memantau kondisi fisik atau lingkungan.",
                "Sistem otonom berdasarkan teori loop tertutup atau sistem pintar/CPS yang menghubungkan, memantau, dan mengendalikan peralatan melalui jaringan di fasilitas seperti pabrik atau gedung."
            ]
        }
        df_pilar = pd.DataFrame(pilar_data)
        st.table(df_pilar)

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-2/fig6.png", use_container_width=True)
        st.caption("Gambar II.6 – Pilar IoT (Sumber: IoTlearners.com)")

    # Bagian 5: Contoh Inovasi IoT Karya Anak Bangsa
    with st.container(border=True):
        st.markdown(
            """
            ### 🇮🇩 Inovasi IoT Kreator Indonesia

            Beberapa *business model* baru dan karya unggulan di bidang IoT (Pratiwi, A., 2019):
            """
        )

        inovasi_data = {
            "Produk": ["HARA", "Qlue", "Spekun", "eFishery", "Nodeflux"],
            "Deskripsi Singkat": [
                "Produk Dattabot untuk sektor pertanian & pangan: menangani potensi lahan, optimasi pertanian, pencegahan hama.",
                "Layanan smart city berbasis IoT: traffic light terhubung command center, kotak sampah pintar, detektor polusi udara.",
                "Bike sharing pertama di Indonesia (kerjasama Telkomsel & Banopolis) menggunakan NB‑IoT dan RFID untuk parkir sepeda.",
                "Alat pemberi pakan ikan otomatis dengan penjadwalan dan dosis tepat, mencatat data real‑time, mencegah over‑feeding.",
                "Menggabungkan AI, Machine Learning, Deep Learning di bidang Computer Vision untuk retail (pemantauan stok) dan properti (sistem parkir)."
            ]
        }
        df_inovasi = pd.DataFrame(inovasi_data)
        st.table(df_inovasi)

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi IoT (Hung, 2017)", expanded=True):
        st.markdown(
            """
            - Jaringan objek fisik dengan **teknologi tertanam** (embedded).
            - Mampu berkomunikasi, sensing, berinteraksi dengan lingkungan.
            - Menghubungkan aset, proses, personel.
            - Data yang dihasilkan dapat mengubah proses bisnis.
            """
        )

    with st.expander("🔧 Tiga Elemen Konsep Kerja IoT"):
        st.markdown(
            """
            1. **Barang fisik** + modul IoT  
            2. **Perangkat koneksi** (modem, router)  
            3. **Cloud Data Center** (aplikasi & database)
            """
        )

    with st.expander("🧩 Empat Pilar IoT (Khan, 2018)"):
        st.markdown(
            """
            - **M2M**: perangkat tangkap peristiwa → informasi.  
            - **RFID**: identifikasi & pelacakan via gelombang radio.  
            - **WSN**: jaringan sensor otonom untuk monitoring.  
            - **SCADA**: kendali peralatan di fasilitas industri.
            """
        )

    with st.expander("💡 Contoh Inovasi IoT Indonesia"):
        st.markdown(
            """
            - **HARA** : pertanian & pangan  
            - **Qlue** : smart city (traffic light, tong sampah)  
            - **Spekun** : bike sharing (NB‑IoT, RFID)  
            - **eFishery** : pakan ikan otomatis  
            - **Nodeflux** : computer vision untuk retail & properti
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Pilar IoT", "4 (M2M, RFID, WSN, SCADA)")
        st.metric("Elemen Konsep IoT", "3")
        st.metric("Inovasi Lokal", "≥5 contoh")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Hung, M. (2017), Gartner Research  
            - mobnasesemka.com  
            - Khan, H.M. (2018)  
            - Pratiwi, A. (2019)  
            - IoTlearners.com
            """
        )