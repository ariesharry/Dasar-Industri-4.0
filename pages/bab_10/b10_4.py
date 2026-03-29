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
    st.title("Kelebihan dan Kekurangan Manufaktur Aditif")

    with st.container(border=True):
        st.markdown(
            """
            ### X.4 Kelebihan dan Kekurangan Teknologi Manufaktur Aditif

            Menurut Singamneni S, (2019), dinyatakan bahwa konversi langsung material menjadi bentuk 3D yang kompleks berdasarkan pada data digital yang dihasilkan dengan mengiris dan meraster file CAD memungkinkan penghematan waktu dan biaya yang signifikan. Sehingga teknologi ini cocok untuk memproduksi komponen produk akhir.

            Menurut K. V. Wong and A. Hernandez, (2012) di antara keuntungan dari proses manufaktur aditif dalam pengembangan produk adalah di samping pengurangan waktu dan biaya, juga adanya interaksi manusia, siklus pengembangan produk yang lebih pendek, dan kemungkinan untuk membuat hampir semua bentuk produk yang sulit dilakukan dengan menggunakan mesin (misal CNC machining).

            Namun demikian rapid prototyping masih belum merupakan solusi terbaik untuk semua kasus. Dalam beberapa kasus proses pemesinan CNC masih dibutuhkan, dimana dimensi komponen yang dibuat bisa lebih besar dari printer manufaktur aditif. Di samping itu bahan untuk rapid prototyping juga masih terbatas.

            Menurut Mehrpouya (2019) berbagai teknologi AM yang telah dikembangkan sampai saat ini tidak untuk menggantikan semua metode manufaktur tradisional (CNC machining) yang selama masih digunakan, tetapi untuk memperluas rentang proses seleksi untuk produsen dan pelanggan. Setiap proses memiliki kelebihan/kekurangannya sendiri dan pilihannya tergantung pada aplikasi.

            Menurut Singamneni S, (2019), dan Mehrpouya (2019), karakteristik yang khas dari AM bila dibandingkan dengan metode manufaktur tradisional adalah konsumsi energi lebih rendah, efisiensi mekanis lebih baik, pemborosan material lebih sedikit, dan waktu desain serta “manufacturing lead time” lebih pendek. Studi kasus menunjukkan bahwa limbah material yang diperoleh dari proses AM berkurang 40% dibandingkan dengan metode tradisional, dan 95% hingga 98% dari limbahnya dapat didaur ulang.

            Di samping itu, konsolidasi titik atau lapisan juga memungkinkan fleksibilitas desain yang lebih baik, tingkat kustomisasi yang lebih tinggi, “lead time” yang lebih rendah dan kemungkinan solusi rantai pasokan yang lebih baik.

            Keuntungan lainnya adalah kebutuhan fixtures, cutting tools, jigs, dan coolants dan gerakan-gerakan kerja khusus dapat ditiadakan, karena proses AM mampu memproduksi bentuk-bentuk 3D yang kompleks langsung dari data digital.
            """
        )

    with st.container(border=True):
        st.markdown("### Tabel X.2 Kelebihan dan kekurangan teknologi AM")
        data_kk = {
            "Kelebihan": [
                "1. Kompleksitas komponen. Teknologi AM yang merupakan proses fabrikasi lapis demi lapis mampu membuat geometri komponen dengan kompleksitas besar, dengan rongga (cavity) dan bentuk yang tidak mungkin diperoleh dengan teknologi tradisional.",
                "2. Lead time (First part/short series). Kemampuan untuk menghasilkan komponen dari file 3D membuat teknologi ini tidak terkalahkan ketika memproduksi komponen pertama (first part), karena kebutuhan alat (tool) atau cetakan (mold) ditiadakan.",
                "3. Customization. Karena tidak ada 'tooling' tambahan yang diperlukan, pembuatan komponen yang dimodifikasi sama mudahnya dengan pembuatan desain aslinya.",
                "4. Biaya tetap lebih rendah untuk pengembangan produk dan seri produk pertama. Karena tidak ada investasi tambahan yang diperlukan untuk 'tooling', 'mold', dll., maka dimungkinkan penurunan biaya awal pada pembuatan prototype dan seri produk pertama."
            ],
            "Kekurangan": [
                "1. Rinci/presisi. Teknologi tradisional (manufaktur subtraktif) memiliki keakuratan lebih signifikan daripada teknologi manufaktur aditif. Secara umum, ± 0,X00 mm (AM) vs kurang dari 0,XX0 mm (tradisional).",
                "2. Long batches. Meskipun aspek-aspek seperti kecepatan dan biaya bahan baku terus diperbaiki, ketika untuk memproduksi komponen/produk dalam jumlah besar, teknologi AM cenderung lebih lambat dan lebih mahal daripada yang tradisional.",
                "3. Ketersediaan berbagai material. Meskipun berbagai material yang tersedia untuk proses AM terus meningkat (terutama plastik dan logam dan, baru-baru ini, keramik), tapi jumlahnya masih terbatas dibandingkan dengan material yang tersedia untuk teknologi lainnya.",
                "4. Kualitas dan sertifikasi. Teknologi AM masih merupakan teknologi yang relatif baru, oleh karena itu masih terdapat ketidakpastian dan kurangnya standar untuk memastikan kualitas jangka panjang dari komponen yang diproduksi."
            ]
        }
        df_kk = pd.DataFrame(data_kk)
        st.table(df_kk)
        st.caption("Sumber: Gonzales dkk (2018)")

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-10/fig2.png", use_container_width=True)
        st.caption("Gambar X.2 Perbedaan Antara Manufaktur Subtraktif dan Manufaktur Aditif (Sumber: cmac.com.au)")

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("✅ Kelebihan AM", expanded=True):
        st.markdown(
            """
            - Kompleksitas geometri tinggi.
            - Lead time pendek untuk part pertama.
            - Kustomisasi mudah.
            - Biaya awal rendah.
            - Konsumsi energi lebih rendah, limbah lebih sedikit (40%).
            """
        )

    with st.expander("❌ Kekurangan AM"):
        st.markdown(
            """
            - Presisi lebih rendah.
            - Lambat dan mahal untuk produksi massal.
            - Material terbatas.
            - Kualitas dan sertifikasi belum matang.
            """
        )

    with st.expander("🔄 AM vs Subtraktif"):
        st.markdown(
            """
            - AM: aditif, kompleks, hemat material.
            - Subtraktif: presisi tinggi, material beragam.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Pengurangan Limbah", "40%")
        st.metric("Daur Ulang Limbah", "95-98%")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Singamneni S (2019)
            - K. V. Wong & A. Hernandez (2012)
            - Mehrpouya (2019)
            - Gonzales dkk (2018)
            """
        )