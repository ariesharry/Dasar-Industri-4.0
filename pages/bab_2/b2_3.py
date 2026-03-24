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
    st.title("Machine to Machine (M2M) dan Internet of Things (IoT)")

    # Bagian 1: Pengantar M2M dan IoT
    with st.container(border=True):
        st.markdown(
            """
            Koneksi data internet umumnya digunakan untuk *browsing*, menonton video, 
            komunikasi media sosial, dan lainnya. Namun, kini koneksi ini juga berfungsi 
            sebagai penghubung antar peralatan yang sebelumnya tidak dapat dilakukan, 
            misalnya dalam konsep **smart home**: perangkat keamanan, lampu, dan kulkas 
            dapat dioperasikan serta dipantau melalui *handphone* dari jarak jauh.

            Oleh karena itu, muncul istilah dan produk seperti **Internet of Things (IoT)** 
            dan **Machine to Machine (M2M)**.
            """
        )

    # Bagian 2: Definisi M2M
    with st.container(border=True):
        st.markdown(
            """
            ### 🔧 Definisi Machine to Machine (M2M)

            **Ajah, S., et al (2015)** mendefinisikan M2M sebagai paradigma baru yang 
            memungkinkan perangkat elektronik untuk **mandiri melaksanakan tugas** 
            dengan atau tanpa intervensi manusia.

            **www.smartlintas.com (2017)** mendefinisikan M2M sebagai komunikasi antar 
            peralatan – bukan hanya perangkat TIK, tetapi segala jenis mesin yang memiliki 
            **sensor dan aktuator**.

            Solusi M2M (bagian dari IoT) menggunakan jaringan nirkabel untuk menghubungkan 
            perangkat satu sama lain dan internet dengan **intervensi manusia minimal**, 
            melayani berbagai kebutuhan industri. Integrasi M2M dan IoT melahirkan 
            **"Pabrik Cerdas"** (*Smart Factory*) yang terhubung untuk meningkatkan produktivitas.
            """
        )

    # Bagian 3: Hubungan WSN, M2M, dan IoT
    with st.container(border=True):
        st.markdown(
            """
            ### 🔗 Hubungan WSN, M2M, dan IoT
            """
        )
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-2/fig7.png", use_container_width=True)
        st.caption("Gambar II.7 – Hubungan WSN, M2M, dan IoT")

        st.markdown(
            """
            Dari gambar dapat diketahui:
            - **M2M merupakan bagian dari IoT**. 
            - IoT berevolusi dari komunikasi **mesin‑ke‑mesin (M2M)**, yaitu mesin yang terhubung 
              satu sama lain melalui jaringan tanpa interaksi manusia.
            - **M2M** mengacu pada menghubungkan perangkat ke cloud, mengelola dan mengumpulkan data.
            - **IoT** adalah jaringan sensor miliaran perangkat pintar yang menghubungkan orang, 
              sistem, dan aplikasi lain untuk mengumpulkan dan berbagi data.
            - **WSN** (Wireless Sensor Network) merupakan salah satu pilar yang juga mendasari IoT.

            *Sumber: majapahit.id*
            """
        )

    # Bagian 4: Perbedaan M2M dan IoT
    with st.container(border=True):
        st.markdown(
            """
            ### 🔍 Perbedaan M2M dan IoT

            Berdasarkan penjelasan di atas, dapat disimpulkan:
            """
        )

        perbedaan_data = {
            "Aspek": ["Fokus Utama", "Konektivitas", "Intervensi Manusia", "Cakupan", "Contoh"],
            "M2M": [
                "Komunikasi antar mesin/perangkat",
                "Point‑to‑point, sering menggunakan koneksi seluler atau kabel",
                "Sangat minimal (otomatis penuh)",
                "Terbatas pada komunikasi mesin‑ke‑mesin",
                "Palang pintu kereta otomatis, sensor industri"
            ],
            "IoT": [
                "Jaringan perangkat pintar yang terhubung ke internet",
                "Berbasis IP, terhubung ke internet dan cloud",
                "Bisa melibatkan manusia untuk monitoring/kontrol",
                "Luas: menghubungkan orang, sistem, aplikasi",
                "Smart home, smart city, wearable devices"
            ]
        }
        df_perbedaan = pd.DataFrame(perbedaan_data)
        st.table(df_perbedaan)

        st.markdown(
            """
            **IoT** lebih menekankan keterhubungan perangkat ke jaringan internet, 
            sehingga memungkinkan campur tangan/manajemen jarak jauh.  
            **M2M** adalah teknologi yang menghubungkan mesin secara nirkabel 
            (termasuk IP dan SMS) dengan sedikit campur tangan manusia.  
            **M2M merupakan bagian integral dari IoT**.
            """
        )

    # Bagian 5: Aplikasi M2M
    with st.container(border=True):
        st.markdown(
            """
            ### 🏭 Aplikasi M2M di Berbagai Bidang

            1. **Pengelolaan Infrastruktur**  
               - Kereta api: mendeteksi kondisi keamanan jalur.  
               - Palang pintu kereta otomatis terbuka tanpa perlu penjaga.

            2. **Monitoring Lingkungan**  
               - Memantau kondisi air waduk secara *real‑time*.  
               - Informasi debit air untuk irigasi petani.  
               - Mitigasi bencana bagi pelaut dan nelayan di laut.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi M2M", expanded=True):
        st.markdown(
            """
            - Komunikasi antar peralatan/mesin dengan sensor & aktuator.  
            - Mandiri, minim intervensi manusia.  
            - Menghubungkan perangkat ke cloud, mengelola & mengumpulkan data.
            """
        )

    with st.expander("🔗 Hubungan WSN, M2M, IoT"):
        st.markdown(
            """
            - **M2M** adalah bagian dari **IoT**.  
            - **IoT** = jaringan miliaran perangkat pintar (orang, sistem, aplikasi).  
            - **WSN** (Wireless Sensor Network) mendukung keduanya.
            """
        )

    with st.expander("⚖️ M2M vs IoT"):
        st.markdown(
            """
            | Aspek | M2M | IoT |
            |-------|-----|-----|
            | Fokus | Mesin ke mesin | Jaringan perangkat pintar |
            | Konektivitas | Point‑to‑point | Berbasis IP, cloud |
            | Intervensi | Minimal | Bisa melibatkan manusia |
            | Cakupan | Terbatas | Luas (orang, sistem) |
            """
        )

    with st.expander("🚂 Contoh Aplikasi M2M"):
        st.markdown(
            """
            - **Infrastruktur**: palang pintu kereta otomatis.  
            - **Lingkungan**: monitoring waduk, debit air irigasi, mitigasi bencana laut.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Hubungan", "M2M ⊂ IoT")
        st.metric("Sumber Definisi", "Ajah 2015, smartlintas 2017")
        st.metric("Contoh Aplikasi", "Smart Factory, Smart Home, Smart Grid")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Ajah, S., et al (2015)  
            - www.smartlintas.com (2017)  
            - www.majapahit.id  
            - Gambar II.7: diolah dari berbagai sumber
            """
        )