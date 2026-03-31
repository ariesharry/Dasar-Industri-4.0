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
    st.markdown(
        """
        <h1 style='text-align: center;'>📘 BAB 10</h1>
        """,
        unsafe_allow_html=True
    )

    # Container isi
    with st.container(border=True):
        st.markdown(
            """
            ### 🎯 Capaian Pembelajaran
            
            Mahasiswa mampu mengetahui dan memahami pengetahuan tentang **manufaktur aditif**, meliputi:
            
            1. **Definisi manufaktur aditif**  
            
            2. **Prinsip kerja manufaktur aditif**  
            
            3. **Teknologi manufaktur aditif**  
            
            4. **Kelebihan dan kekurangan teknologi manufaktur aditif**  
            
            5. **Aplikasi manufaktur aditif**  
            """
        )

    st.title("Definisi Manufaktur Aditif")

    with st.container(border=True):
        st.markdown(
            """
            Sejarah terbentuknya ide/konsep additive manufacturing pertama adalah pembuatan lapisan demi lapisan objek tiga dimensi menggunakan CAD (Computer Aided Design) yang dikenal sebagai “rapid prototyping”, dan dikembangkan pada 1980-an pada pembuatan model dan prototipe komponen. (K. V.Wong and A. Hernandez, 2012). Jadi rapid prototyping adalah salah satu proses awal terbentuknya manufaktur aditif (Additive Manufacturing–AM), yang memungkinkan pembuatan komponen yang dicetak secara massal dengan bahan baku dari plastik/polimer atau logam, tidak hanya untuk pembuatan model saja.

            Teknologi ini juga memiliki nama lain seperti 3D printing, dan sebagainya, tetapi semuanya berasal dari konsep pembuatan “rapid prototyping”.

            ### X.1 Definisi Manufaktur Aditif

            Manufaktur aditif (Additive Manufacturing–AM) adalah istilah standar industri resmi (ASTM F2792 - Standard Terminology for Additive Manufacturing Technologies) untuk semua aplikasi teknologi. Ini didefinisikan sebagai proses penggabungan bahan untuk membuat objek dari data model 3D, biasanya lapisan demi lapisan, sebagai kebalikan dari metode manufaktur subtraktif (seperti CNC machining).
            """
        )
    
    with st.container():
        # Buat 3 kolom untuk center (kiri - tengah - kanan)
        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])

        with col2:
            # Embed video
            st.markdown(
                """
                <div style="
                    border-radius: 10px;
                    overflow: hidden;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                    margin-bottom: 30px;
                ">
                    <iframe 
                        width="100%" 
                        height="400" 
                        src="https://www.youtube.com/embed/EHvO-MlzAIM"
                        title="YouTube video"
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen>
                    </iframe>
                </div>
                """,
                unsafe_allow_html=True
            )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Sejarah", expanded=True):
        st.markdown(
            """
            - Konsep awal: rapid prototyping (1980-an).
            - Menggunakan CAD untuk membuat objek lapis demi lapis.
            """
        )

    with st.expander("📌 Definisi AM"):
        st.markdown(
            """
            - Istilah resmi ASTM F2792.
            - Proses menggabungkan bahan dari data model 3D.
            - Lawan dari manufaktur subtraktif.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Tahun Awal", "1980-an")
        st.metric("Nama Lain", "3D printing, rapid prototyping")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - K. V. Wong and A. Hernandez (2012)
            - ASTM F2792
            """
        )