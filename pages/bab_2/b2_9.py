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
    st.title("Augmented Reality (AR) dan Virtual Reality (VR)")

    # Pengantar IoT dan AR/VR
    with st.container(border=True):
        st.markdown(
            """
            **Internet of Things (IoT)** telah muncul sebagai kerangka kerja infrastruktur yang menjanjikan, 
            di mana sejumlah besar perangkat yang saling terhubung mengumpulkan data dan menyediakan layanan 
            cerdas seperti kontrol otomatis, optimisasi proses, dan deteksi anomali. Salah satu cara bermanfaat 
            untuk memanfaatkan sistem IoT adalah melalui teknologi **Virtual Reality (VR)** dan **Augmented Reality (AR)**. 
            Keduanya mendapat perhatian besar, terutama di perusahaan teknologi dan platform gaming.

            AR dan VR adalah teknologi yang bertujuan merangsang persepsi dan indera penggunanya. Pengguna dapat 
            merasakan berada di "dunia lain" dan berinteraksi di dalamnya.
            """
        )

    # Perbedaan AR dan VR menurut Fikrinugraha (2019)
    with st.container(border=True):
        st.markdown(
            """
            ### 🔍 Perbedaan AR dan VR (Fikrinugraha, 2019)
            """
        )

        # VR
        st.markdown(
            """
            **1. Virtual Reality (VR)**  
            VR adalah teknologi intuitif yang berdampak setidaknya pada dua dari lima indera (terlihat dan terdengar). 
            Teknologi ini menciptakan persepsi berada di tempat yang sama sekali berbeda.  
            Contoh: Menggunakan *head-mounted display* (HMD) atau *headset*, pengguna merasakan dunia gambar dan suara 
            yang dihasilkan komputer, dapat memanipulasi objek dan bergerak menggunakan pengontrol *haptic* yang terhubung 
            ke konsol atau PC.
            """
        )
        st.image("https://via.placeholder.com/500x250?text=Gambar+II.14+-+Contoh+Virtual+Reality", use_container_width=True)
        st.caption("Gambar II.14 – Contoh Virtual Reality (Sumber: anandtech.com)")

        # AR
        st.markdown(
            """
            **2. Augmented Reality (AR)**  
            AR tidak membawa pengguna ke dunia maya sepenuhnya, melainkan **meningkatkan objek di sekitar** dengan 
            melapiskan gambar virtual ke lingkungan nyata. AR menempatkan objek virtual ke dunia nyata.  
            Contoh: Melihat buku di meja melalui *smartphone*, atau game populer **PokemonGo**. Di bidang militer, AR 
            digunakan untuk simulasi perang di mana prajurit masuk ke dalam dunia game dan merasakan pengalaman tempur.
            """
        )
        st.image("https://via.placeholder.com/500x250?text=Gambar+II.15+-+Contoh+Augmented+Reality", use_container_width=True)
        st.caption("Gambar II.15 – Contoh Augmented Reality")

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi Singkat", expanded=True):
        st.markdown(
            """
            - **VR**: Menciptakan dunia maya sepenuhnya, pengguna tenggelam (*immersive*) dalam lingkungan simulasi.  
            - **AR**: Menambahkan elemen virtual ke dunia nyata, tidak menggantikan lingkungan.
            """
        )

    with st.expander("🆚 Perbedaan Utama (Fikrinugraha, 2019)"):
        st.markdown(
            """
            | Aspek | VR | AR |
            |-------|----|----|
            | Lingkungan | Sepenuhnya maya | Nyata + overlay virtual |
            | Indera | Minimal 2 (visual, audio) | Visual (biasanya) |
            | Contoh | HMD, game simulasi | PokemonGo, buku interaktif |
            """
        )

    with st.expander("📱 Contoh Penerapan"):
        st.markdown(
            """
            - **VR**: Pelatihan militer, simulasi medis, game imersif.  
            - **AR**: Game (PokemonGo), navigasi, perbaikan mesin (petunjuk overlay), militer.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Teknologi", "VR & AR")
        st.metric("Sumber Perbedaan", "Fikrinugraha, 2019")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Fikrinugraha (2019)  
            - anandtech.com (gambar VR)
            """
        )