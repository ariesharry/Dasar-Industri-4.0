import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

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

with cols[0].container(border=True):
    st.title("Prinsip Kerja Manufaktur Aditif")

    with st.container(border=True):
        st.markdown(
            """
            ### X.2 Prinsip Kerja Manufaktur Aditif

            1. **Proses dimulai dengan file 3D** yang dapat berasal dari aplikasi CAD 3D apa pun, yang kemudian dikonversi ke format standar 3D, misal format .STL.
            2. **Komponen tersebut dapat menghasilkan beberapa ketidakakuratan atau karakteristik yang mencegah pembuatan AM** (misalnya geometri dengan risiko tinggi terkulai (drooping) ketika dicetak 3D, simpul tidak-tertutup, kesalahan yang timbul dari proses konversi STL, dll.). Untuk itu diperlukan proses perbaikan untuk menjamin hasil manufaktur berikutnya yang lebih baik.
            3. **Setelah dipastikan bahwa komponen tersebut dapat diproduksi**, proses pengirisan diterapkan ke file 3D. Proses ini mungkin merupakan tahap yang paling penting dari proses manufaktur aditif karena pembagian model 3D ini memungkinkan dapat diproduksi lapis demi lapis.
            4. **File yang dihasilkan kemudian siap dikirim ke mesin AM**. Tergantung pada spesifikasi yang diperlukan, berbagai parameter mesin dapat dipilih (misalnya, lebar lapisan) dan setelah file tersebut diperbaiki, pembuatan dapat dimulai. Waktu produksi akan tergantung pada teknologi AM, jumlah komponen yang diproduksi secara bersamaan (concurrent), kompleksitas komponen dan lebar lapisan.
            5. **Setelah komponen tersebut selesai diproduksi**, mungkin perlu dilakukan tahap berikutnya yaitu paska-pemrosesan. Namun masing-masing teknologi dapat membutuhkan metode yang berbeda-beda. Sebagai contoh, pada paska pemrosesan diperlukan penghilangan penopang struktur, dibutuhkan pengangkatan hasil produksi dengan alat mekanis, diperlukan perawatan lebih lanjut tergantung pada teknologi AM yang digunakan (misal fine machining, perawatan panas, pemolesan, dll.).
            """
        )
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-10/fig1.png", use_container_width=True)
        st.caption("Gambar X.1 Prinsip kerja manufaktur aditif (Sumber: researchgate.net)")

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Tahapan Utama", expanded=True):
        st.markdown(
            """
            1. File CAD → format STL.
            2. Perbaikan model jika perlu.
            3. Pengirisan (slicing).
            4. Pengaturan parameter mesin.
            5. Produksi.
            6. Paska-pemrosesan.
            """
        )

    with st.expander("⚙️ Parameter Produksi"):
        st.markdown(
            """
            - Lebar lapisan.
            - Jumlah komponen bersamaan.
            - Kompleksitas geometri.
            """
        )

    with st.expander("🔧 Paska-pemrosesan"):
        st.markdown(
            """
            - Penghilangan penopang.
            - Fine machining, heat treatment, polishing.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Tahapan", "5 (persiapan data + produksi + paska)")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Gonzales dkk (2018)
            """
        )