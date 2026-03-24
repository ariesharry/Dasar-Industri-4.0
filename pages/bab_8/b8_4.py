import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .stColumn:first-child > div:first-child {
        background-color: #caf0f8;
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
    st.title("Deep Learning (DL)")

    with st.container(border=True):
        st.markdown(
            """
            Deep learning merupakan metode pembelajaran yang memanfaatkan artificial neural network yang berlapis-lapis (multilayer). DL sering juga disebut deep structured learning atau hierarchical learning atau deep neural merupakan metode pembelajaran yang memanfaatkan multiplenon linier transformation. Gambar VIII.6 menjelaskan bahwa DL adalah bidang kecerdasan buatan yang berdasarkan jaringan saraf tiruan, yaitu menggunakan struktur algoritma berlapis-lapis yang disebut jaringan saraf. Metode ini merupakan bagian dari machine learning yang algoritmanya membutuhkan data untuk belajar menyelesaikan tugas. Model Deep Learning cenderung meningkatkan akurasi dengan semakin banyaknya data pelatihan. X sebagai input data yang diproses secara berlapis dengan output dari layer sebelumnya akan menjadi input bagi layer sesudahnya dan Y sebagai outputnya.
            """
        )
        st.image("https://via.placeholder.com/600x250?text=Gambar+VIII.6+-+Ilustrasi+Multilayer+Artificial+Neural+Networks", use_container_width=True)
        st.caption("Gambar VIII.6 Ilustrasi Multilayer Artificial Neural Networks (Sumber: deeplearning-academy.com)")

        st.markdown(
            """
            DL sangat berdampak pada kemajuan perkembangan yang telah dicapai AI secara bertahap. Tidak hanya untuk perangkat lunak, namun para penggunanya juga telah merambah di berbagai bidang industri. Contohnya seperti Facebook dan Google yang menggunakan sistem DL.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi DL", expanded=True):
        st.markdown(
            """
            - Metode pembelajaran dengan artificial neural network berlapis-lapis (multilayer).
            - Bagian dari machine learning.
            - Akurasi meningkat dengan lebih banyak data.
            """
        )

    with st.expander("🏭 Contoh Penggunaan"):
        st.markdown(
            """
            - Facebook, Google menggunakan sistem DL.
            - Digunakan di berbagai bidang industri.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Jenis", "Subset ML dengan neural network multilayer")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - deeplearning-academy.com
            """
        )