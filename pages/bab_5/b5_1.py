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
    st.title("Definisi Komputasi Awan")

    # Definisi lengkap
    with st.container(border=True):
        st.markdown(
            """
            **Komputasi awan** adalah istilah umum untuk apa pun yang melibatkan pemberian layanan yang di-host melalui Internet. 
            Komputasi awan berarti menyimpan dan mengakses data dan program melalui jaringan internet sebagai pengganti yang selama ini menggunakan hard drive komputer lokal (*on premise*). 

            Aplikasi perangkat lunak anda akan berjalan di server yang dikelola oleh pusat data (*data centre*) dan akan terlihat sama seperti biasanya di komputer lokal anda (*on premise*). 
            Semua file anda disimpan di server di pusat data dan anda akan memiliki akses ke semua informasi ini dengan koneksi internet. 

            Nama *cloud computing* terinspirasi oleh simbol cloud yang sering digunakan untuk mewakili Internet dalam flowchart dan diagram.
            """
        )

    # Gambar referensi
    with st.container(border=True):
        st.markdown("### 🖼️ Ilustrasi Arsitektur Komputasi Awan")

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-5/fig1.png", use_container_width=True)

        st.caption("Gambar V.1 – Contoh arsitektur layanan komputasi awan (Sumber: datamation.com)")

    # Komponen lengkap
    with st.container(border=True):
        st.markdown("### 🧩 Komponen dalam Komputasi Awan")

        st.markdown(
            """
            **1. Cloud Server**  
            Cloud server merupakan layanan teknologi yang menggabungkan komputer dan jaringan yang berbasis internet. 
            Pada intinya, teknologi ini memanfaatkan media internet sebagai pusat server untuk pengelolaan data. 
            Sehingga data-data yang Anda perlukan dapat dengan mudah diakses dan tidak perlu lagi menyimpan data melalui alat penyimpanan seperti Flashdisk, Harddisk, CD maupun DVD. 

            Tentu hal ini akan sangat mempermudah bila seseorang memiliki data yang tersimpan di suatu perangkat penyimpanan dan perangkat itu hilang, maka data yang tersimpan pasti ikut hilang. 
            Namun, data di cloud server akan tetap aman.
            """
        )

        st.markdown(
            """
            **2. Virtual Desktop**  
            Virtual desktop merupakan hasil teknologi dengan konsep Virtual Desktop Infrastructure (VDI) yang sedang berkembang. 
            Dimana desktop adalah komputer kerja juga bisa disebut komputer meja yang dipakai untuk kerja sehari–hari dalam satu lokasi bisa di rumah maupun di kantor. 

            Dan lebih diperuntukkan kepada perusahaan dengan karyawan yang menggunakan komputer, sehingga desktop (komputer kerja) tidak lagi harus wujud fisik komputer yang besar tetapi sudah dalam bentuk virtual yang akan dapat diakses dengan model client-server.
            """
        )

        st.markdown(
            """
            **3. Platform Software (Perangkat Lunak)**  
            Platform software adalah platform yang digunakan dalam sesuatu yang berkaitan dengan software atau perangkat lunak. 
            Platform perangkat lunak ini lebih luas, namun lebih mudah untuk dihubungkan oleh pengguna. 

            Karena lebih masuk akal, mengingat bahwa kita berinteraksi lebih umum dengan perangkat lunak yang berupa aplikasi, meskipun perangkat keras (misalnya mouse, keyboard, monitor, layar sentuh) membantu menjembatani interaksi kita. 

            Kategori umum platform perangkat lunak termasuk dalam:  
            - Software system atau perangkat lunak sistem  
            - Software application atau aplikasi perangkat lunak
            """
        )

        st.markdown(
            """
            **4. Applications**  
            Applications berfungsi untuk melakukan tugas-tugas khusus yang tidak lepas dari beberapa macam program pembangunnya, yaitu terdiri dari software hiburan, pendidikan, bisnis, perangkat lunak khusus, serta produktivitas kerja. 

            Perangkat lunak penunjang produktivitas kerja memberikan peranan yang sangat bermanfaat untuk optimalisasi mutu kerja.
            """
        )

        st.markdown(
            """
            **5. Storage/Data**  
            Storage/data adalah layanan penyimpanan file di internet dimana file-file yang tersimpan bisa dikelola dari mana saja selama user masih terhubung dengan cloud storage tersebut melalui jaringan internet. 

            Konsep kerja cloud storage sama seperti pada konsep file server di suatu perusahaan, bedanya infrastruktur pada media storage tersebut dikelola oleh provider cloud, dan selanjutnya pemanfaatannya dijadikan sebagai layanan penyimpanan file yang bisa diakses dari internet.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi", expanded=True):
        st.markdown(
            """
            - Komputasi awan adalah layanan berbasis internet.
            - Data dan program diakses melalui internet, bukan hard drive lokal.
            - File tersimpan di data center dan bisa diakses kapan saja.
            """
        )

    with st.expander("🧩 Komponen"):
        st.markdown(
            """
            - Cloud server
            - Virtual desktop (VDI)
            - Platform software
            - Applications
            - Storage/data
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Akses Data", "Kapan saja via Internet")
        st.metric("Keamanan Data", "Tidak bergantung device lokal")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Modul Industri 4.0 Dasar  
            - https://www.datamation.com/cloudcomputing/what-is-cloud-computing.html
            """
        )