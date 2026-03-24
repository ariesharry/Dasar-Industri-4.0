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
    st.title("Definisi Robot")

    # Bagian 1: Pengantar Robot di Era Industri
    with st.container(border=True):
        st.markdown(
            """
            Teknologi robot muncul pada era **revolusi industri 3.0**. Kemudian pada era 
            **revolusi industri 4.0** muncul robot otonom yang memiliki kemampuan lebih 
            dibandingkan robot tradisional. Namun demikian, penting untuk memahami definisi 
            dan jenis-jenis robot yang sudah beredar di pasar.
            """
        )

    # Bagian 2: Definisi Robot
    with st.container(border=True):
        st.markdown(
            """
            ### 📌 Definisi Robot

            Robot dapat didefinisikan sebagai **perangkat yang dapat diprogram oleh komputer** 
            dan dapat dikendalikan sendiri yang terdiri dari unit elektronik, listrik, atau mekanik. 
            Robot mampu melakukan serangkaian tindakan kompleks secara otomatis, yang dapat dipandu 
            oleh perangkat kontrol eksternal atau kontrol yang tertanam (*embedded*) di dalamnya.

            Robot dapat bersifat:
            - **Stasioner** atau **mobile**
            - **Otonom** atau seperti serangga (dengan pemrograman sederhana)
            - Dilengkapi pemrograman canggih, pengenalan ucapan, sintesis suara, dan fitur-fitur lainnya
            """
        )

    # Bagian 3: Peran AI dalam Robot
    with st.container(border=True):
        st.markdown(
            """
            ### 🧠 Peran Artificial Intelligence (AI)

            **AI** memungkinkan robot untuk **memahami kondisi** dan **memutuskan tindakan** 
            berdasarkan kondisi tersebut. Dengan AI, robot dapat beradaptasi dengan lingkungan 
            dan menjalankan tugas secara lebih cerdas.
            """
        )

    # Bagian 4: Aplikasi Robot di Industri
    with st.container(border=True):
        st.markdown(
            """
            ### 🏭 Aplikasi Robot di Dunia Industri

            Dalam dunia industri, khususnya pada proses **otomasi**, penggunaan robot sangat 
            dibutuhkan karena dapat meningkatkan **efisiensi** dan **produktivitas**. Robot 
            industri digunakan untuk berbagai tugas, antara lain:
            - Pengecatan
            - *Line tracking*
            - *Palletizing*
            - Penanganan material
            - Pengelasan
            - Perakitan
            - Dan lain sebagainya

            Dengan penggunaan robot, semua pekerjaan yang sudah terprogram akan dijalankan 
            secara otomatis.
            """
        )

    # Bagian 5: Robot Era 3.0 vs 4.0
    with st.container(border=True):
        st.markdown(
            """
            ### 🔄 Robot Era Industri 3.0 dan 4.0

            Pada **revolusi industri 3.0**, robot bekerja berdasarkan program tetap dan masih 
            membutuhkan tenaga manusia sebagai operator yang mengontrol tiap-tiap bagian agar 
            berjalan sesuai keinginan. Sistem tidak sepenuhnya mandiri.

            Sedangkan pada **revolusi industri 4.0**, robot otonom mampu bekerja mandiri dengan 
            intervensi manusia minimal, menggunakan sensor, AI, dan konektivitas untuk beradaptasi 
            dengan lingkungan.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi Robot", expanded=True):
        st.markdown(
            """
            - Perangkat yang dapat diprogram komputer.
            - Terdiri dari unit elektronik, listrik, mekanik.
            - Mampu melakukan tindakan kompleks otomatis.
            - Dapat stasioner atau mobile, otonom atau sederhana.
            """
        )

    with st.expander("🧠 Peran AI"):
        st.markdown(
            """
            AI memungkinkan robot memahami kondisi dan mengambil keputusan secara mandiri.
            """
        )

    with st.expander("🏭 Aplikasi Industri"):
        st.markdown(
            """
            Pengecatan, line tracking, palletizing, material handling, pengelasan, perakitan, dll.
            """
        )

    with st.expander("🔄 Robot 3.0 vs 4.0"):
        st.markdown(
            """
            - **3.0**: Butuh operator, program tetap.
            - **4.0**: Otonom, AI, sensor, adaptif.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Kemunculan Robot", "Era Industri 3.0")
        st.metric("Robot Otonom", "Era Industri 4.0")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Materi kuliah robotika
            - Sumber industri 4.0
            """
        )