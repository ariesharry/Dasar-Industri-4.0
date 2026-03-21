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
    st.title("Klasifikasi Internet of Things")

    # Bagian pengantar: dua klasifikasi utama
    with st.container(border=True):
        st.markdown(
            """
            IoT dapat dikelompokkan menjadi dua bagian utama:
            - **Industrial IoT (IIoT)** – segmen B2B (Business to Business)
            - **Consumer IoT (CIoT)** – segmen B2C (Business to Consumer)
            """
        )

    # Penjelasan CIoT dan IIoT
    with st.container(border=True):
        st.markdown(
            """
            ### 🏭 Consumer IoT (CIoT) vs Industrial IoT (IIoT)

            **Consumer Internet of Things (CIoT)** adalah segmen B2C dari IoT. Solusi CIoT dibuat 
            untuk **pengguna akhir** dan biasanya didedikasikan untuk penggunaan individual 
            non‑komersial.

            **Industrial Internet of Things (IIoT)** terdiri dari produk yang dibuat untuk 
            **perusahaan, pabrik, dll.**, mewakili segmen B2B. Tidak seperti CIoT, IIoT memberikan 
            nilai baik bagi perusahaan yang memanfaatkan solusi maupun pengguna akhir. Perusahaan 
            dapat meningkatkan produktivitas, kualitas, menurunkan harga melalui inovasi teknologi, 
            dan sebagai hasilnya meningkatkan kepuasan pelanggan.
            """
        )

    # Perbedaan teknologi (Chuprina, R., 2019)
    with st.container(border=True):
        st.markdown(
            """
            ### 🔧 Perbedaan Teknologi CIoT dan IIoT (Chuprina, R., 2019)

            1. **Ketahanan perangkat**  
               Perangkat industri harus lebih tahan terhadap kondisi ekstrem (tahan air, tekanan tinggi, dll.), sedangkan perangkat konsumen mungkin tidak memerlukan ketahanan seketat itu.

            2. **Skalabilitas**  
               Sistem IIoT harus dirancang dengan skalabilitas tinggi, memungkinkan penambahan perangkat, fasilitas, jalur produksi, dan pemrosesan data tambahan dengan mudah.

            3. **Keamanan cyber**  
               IIoT selalu berurusan dengan informasi komersial sensitif yang harus dilindungi kuat karena potensi kerugian besar jika dikompromikan. CIoT juga perlu keamanan, tetapi risikonya berbeda.

            4. **Pelabelan dan merek**  
               Produk industri biasanya mengalami *white labeling* (tanpa merek tertentu), sementara solusi konsumen selalu diproduksi di bawah merek tertentu.

            5. **Penampilan dan harga**  
               Perangkat konsumen memiliki persyaratan lebih ketat untuk penampilan (menarik, ringan, antarmuka keren) dan harga yang kompetitif.
            """
        )

    # Contoh sektor penerapan
    with st.container(border=True):
        st.markdown(
            """
            ### 📋 Contoh Sektor Penerapan

            **IIoT** dimanfaatkan antara lain pada sektor:
            - Manufaktur
            - Logistik
            - Kesehatan
            - Utilitas (listrik, air, gas)
            - Transportasi
            - Alat-alat berat

            **CIoT** digunakan antara lain pada sektor:
            - Otomasi rumah (smart home)
            - Peralatan rumah tangga pintar
            - Pemantauan rumah (keamanan)
            - Ponsel
            - Perangkat *wearable* (jam tangan pintar, fitness tracker)
            - Televisi pintar
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 CIoT vs IIoT – Dasar", expanded=True):
        st.markdown(
            """
            - **CIoT**: B2C, untuk pengguna akhir, penggunaan individual non‑komersial.  
            - **IIoT**: B2B, untuk perusahaan/pabrik, meningkatkan produktivitas, kualitas, efisiensi.
            """
        )

    with st.expander("🔐 Perbedaan Teknologi (Chuprina, 2019)"):
        st.markdown(
            """
            1. **Ketahanan** : IIoT > CIoT (lingkungan ekstrem)  
            2. **Skalabilitas** : IIoT harus sangat skalabel  
            3. **Keamanan** : IIoT lebih ketat (data sensitif)  
            4. **Merek** : IIoT sering *white label*, CIoT bermerek  
            5. **Desain & Harga** : CIoT lebih memperhatikan estetika dan harga kompetitif
            """
        )

    with st.expander("🏭 Contoh Sektor IIoT"):
        st.markdown(
            "Manufaktur, Logistik, Kesehatan, Utilitas, Transportasi, Alat berat"
        )

    with st.expander("🏠 Contoh Sektor CIoT"):
        st.markdown(
            "Smart home, peralatan rumah tangga, monitoring rumah, ponsel, wearable, smart TV"
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Klasifikasi Utama", "2 (IIoT & CIoT)")
        st.metric("Perbedaan Teknologi", "5 poin")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Chuprina, R. (2019)  
            - Berbagai sumber literatur IoT
            """
        )