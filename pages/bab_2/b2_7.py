import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
st.markdown(
    """
    <style>
    /* Target container utama di kolom pertama */
    .stColumn:first-child > div:first-child {
        background-color: #FBEFEF;   /* pink muda */
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
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
    st.title("Cyber Physical System (CPS)")

    # Bagian 1: Definisi dan karakteristik CPS
    with st.container(border=True):
        st.markdown(
            """
            ### 📘 Definisi dan Karakteristik CPS

            Tinjauan dari **31 definisi CPS** (Greer dkk, 2019) mengungkapkan enam karakteristik umum:
            - Sistem fisik dan logis hibrid
            - Metode analitik dan pengukuran hibrid
            - Kontrol
            - Kelas komponen
            - Waktu
            - Kepercayaan
            """
        )

    # Bagian 2: Perbedaan IoT dan CPS
    with st.container(border=True):
        st.markdown(
            """
            ### 🔍 Perbedaan IoT dan CPS

            - **Internet of Things (IoT)**: Menghubungkan "things" (objek dan mesin) ke internet dan akhirnya satu sama lain.
            - **Cyber Physical Systems (CPS)**: Integrasi komputasi, jaringan, dan proses fisik. CPS melibatkan pendekatan multidisiplin (sibernetika, mekatronik, desain, ilmu proses). Tujuan utamanya adalah mengendalikan proses fisik dan, melalui umpan balik, menyesuaikan diri dengan kondisi baru secara *real time*.
            """
        )

    # Gambar II.9
    with st.container(border=True):
        st.image("https://via.placeholder.com/600x250?text=Gambar+II.9+-+Perkembangan+dari+Internet+of+Service+menjadi+Cyber+Physical+System", use_container_width=True)
        st.caption("Gambar II.9 – Perkembangan dari Internet of Service menjadi Cyber Physical System (Sumber: Oztemel & Gursev, 2018)")

    # Bagian 3: Framework Sangmahachai
    with st.container(border=True):
        st.markdown(
            """
            Menurut **Sangmahachai** (dalam Oztemel, E., & Gursev, S., 2018), kerangka pada Gambar II.9 menunjukkan bahwa 
            **Revolusi Industri 4.0** memfokuskan perhatian pada:
            - Sistem fisik‑siber (CPS)
            - Internet of Things
            - Virtualisasi
            - Modularitas
            - Operasi waktu nyata
            - Interoperabilitas layanan
            """
        )

    # Gambar II.10
    with st.container(border=True):
        st.image("https://via.placeholder.com/600x250?text=Gambar+II.10+-+Hubungan+Dunia+Fisik+dengan+Dunia+Virtual+pada+CPS", use_container_width=True)
        st.caption("Gambar II.10 – Hubungan Dunia Fisik dengan Dunia Virtual pada CPS")

    # Bagian 4: Penjelasan CPS dan dunia fisik-virtual
    with st.container(border=True):
        st.markdown(
            """
            Adanya CPS akan menghubungkan antara **dunia nyata** dengan **dunia maya** (Gambar II.10). 
            Penggabungan ini terwujud melalui integrasi proses fisik dan komputasi. Teknologi CPS 
            memonitor proses fisik produksi, menampilkannya secara virtual, dan melakukan desentralisasi 
            pengambilan keputusan. Melalui IoT, CPS mampu saling berkomunikasi dan bekerja sama secara 
            *real time*, termasuk dengan manusia.
            """
        )

    # Gambar II.11
    with st.container(border=True):
        st.image("https://via.placeholder.com/600x250?text=Gambar+II.11+-+Pilar+Teknologi+yang+Mendukung+CPS", use_container_width=True)
        st.caption("Gambar II.11 – Pilar Teknologi yang Mendukung CPS (M2M, IoT, dll.)")

    # Bagian 5: Pilar teknologi
    with st.container(border=True):
        st.markdown(
            """
            Pilar teknologi yang mendukung CPS (Gambar II.11) meliputi konsep **M2M**, **IoT**, dan lainnya, 
            yang memungkinkan dunia fisik terhubung dengan dunia maya sebagai pondasi teknologi.
            """
        )

    # Gambar II.12
    with st.container(border=True):
        st.image("https://via.placeholder.com/600x250?text=Gambar+II.12+-+CPS+dalam+Smart+Manufacturing", use_container_width=True)
        st.caption("Gambar II.12 – CPS dalam Smart Manufacturing")

    # Bagian 6: Masa depan CPS
    with st.container(border=True):
        st.markdown(
            """
            ### 🔮 Masa Depan CPS dan Smart Manufacturing

            Di masa depan, CPS akan hadir di semua sektor industri dan dalam paradigma **Industri 4.0** atau 
            **manufaktur cerdas** (*smart manufacturing*). CPS akan membuka metodologi produksi baru yang 
            menjadi standar masa depan bagi industri. Lingkungan produksi akan:
            - Mengatur sendiri
            - Menyesuaikan diri
            - Mengoptimalkan diri

            Hal ini mengarah pada kelincahan, fleksibilitas, dan efektivitas biaya yang lebih besar. 
            Seperti diilustrasikan pada Gambar II.12, setiap aspek fungsional rantai produksi akan terpengaruh:
            - Desain
            - Manufaktur
            - Rantai pasokan
            - Layanan dan dukungan pelanggan

            **Smart manufacturing** memungkinkan produsen mengoptimalkan produksi dan jaringan pasokan 
            dengan memanfaatkan teknologi informasi dan manufaktur canggih. Peningkatan pelatihan tenaga kerja 
            diperlukan untuk fleksibilitas dan penggunaan teknologi, berbeda dengan tugas khusus pada 
            manufaktur tradisional.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi CPS", expanded=True):
        st.markdown(
            """
            - Integrasi komputasi, jaringan, dan proses fisik.  
            - Mengendalikan proses fisik, beradaptasi secara *real time* via umpan balik.  
            - Multidisiplin: sibernetika, mekatronik, desain, ilmu proses.
            """
        )

    with st.expander("🔁 Perbedaan IoT vs CPS"):
        st.markdown(
            """
            - **IoT**: konektivitas "things" ke internet.  
            - **CPS**: integrasi komputasi dengan proses fisik, fokus pada kontrol dan umpan balik.
            """
        )

    with st.expander("🧩 Karakteristik CPS (Greer dkk, 2019)"):
        st.markdown(
            """
            1. Sistem fisik & logis hibrid  
            2. Metode analitik & pengukuran hibrid  
            3. Kontrol  
            4. Kelas komponen  
            5. Waktu  
            6. Kepercayaan
            """
        )

    with st.expander("🏭 CPS dalam Industri 4.0"):
        st.markdown(
            """
            - Mendukung virtualisasi, modularitas, operasi real‑time, interoperabilitas.  
            - Memungkinkan produksi self‑organizing, adaptive, self‑optimizing.  
            - Mempengaruhi desain, manufaktur, rantai pasok, layanan pelanggan.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Karakteristik CPS", "6 (Greer dkk)")
        st.metric("Pilar Pendukung", "M2M, IoT, dll.")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Greer dkk (2019)  
            - Oztemel, E., & Gursev, S. (2018)  
            - Sangmahachai (dalam Oztemel & Gursev, 2018)
            """
        )