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
    st.title("Aplikasi Artificial Intelligence pada Industri")

    with st.container(border=True):
        st.markdown(
            """
            Pada saat ini, AI merambah ke berbagai dunia bisnis guna membantu suatu pekerjaan menjadi lebih cepat dan efisien. Contoh nyata aplikasi AI dapat dilihat dari berbagai bidang sebagai berikut:

            1. **Kesehatan**, dengan menggunakan teknologi pengenalan gambar, pemrosesan data besar, dan pembelajaran mendalam memungkinkan para profesional kesehatan memahami faktor risiko dan penyakit pada tingkat yang lebih dalam mendiagnosis dan memberikan wawasan tentang risikonya, mengelola rekam medis.

            2. **Pertanian**, AI sekarang banyak digunakan untuk pemantauan tanaman. Ini membantu petani menerapkan air, pupuk, dan zat lain pada tingkat optimal.

            3. **Keuangan**, memungkinkan konsumen untuk memindai cek kertas dan melakukan setoran menggunakan smartphone.

            4. **Perjalanan**, transportasi dan perhotelan menggunakan AI untuk memperkirakan permintaan dan menyesuaikan harga secara dinamis.

            5. **Pendidikan**, melalui algoritma, AI memasukkan analisis data siswa ke basis pengetahuan yang ada. Menyesuaikan kursus dan latihan yang sesuai.

            6. **Retail**, pelanggan, terutama generasi milenial sudah merangkul teknologi digital. Mereka mengharapkan pengalaman yang sangat pribadi yang mengikat saluran suara, video dan film. AI telah mengubah pembelanjaan dengan memberikan rekomendasi pribadi berdasarkan preferensi pelanggan sebelumnya. AI juga dapat membantu manajemen toko dalam hal stok, analisis tata letak, prediksi penjualan, dan lainnya.

            7. **Manufaktur**, Aplikasi AI yang inovatif saat ini dapat dilihat pada kegiatan manufaktur untuk mengoptimalkan proses validasi desain, melakukan otomatisasi pergerakan material, mendukung pemeliharaan prediktif, melakukan otomatisasi kondisi pertumbuhan tanaman, mengontrol rantai pasokan yang kompleks.

            8. **Keamanan**, AI menjadi komponen penting dalam keselamatan publik. Untuk kamera keamanan dan pengawasan, AI dapat menjadi mata digital, dan menganalisis gerakan. Ini dapat membantu polisi mendeteksi kejahatan dan memantau ruang publik untuk kecelakaan serta gangguan. Keamanan pengenal wajah kini juga digunakan hampir di mana saja dari smartphone dan membangun sistem akses ke kartu kredit dan lisensi pengemudi.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("🏭 Bidang Aplikasi AI", expanded=True):
        st.markdown(
            """
            - Kesehatan
            - Pertanian
            - Keuangan
            - Perjalanan & transportasi
            - Pendidikan
            - Retail
            - Manufaktur
            - Keamanan
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Jumlah Bidang", "8")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - De Spiegeleire, S., dkk (2017)
            - Berbagai sumber
            """
        )