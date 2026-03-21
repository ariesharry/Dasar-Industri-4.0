import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .stColumn:first-child > div:first-child {
        background-color: #FBEFEF;
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

with cols[0].container(border=True):
    st.title("Business Intelligence, Data Visualization, dan Intelligent Dashboard")

    with st.container(border=True):
        st.markdown(
            """
            ### Business Intelligence

            Business intelligence (BI) dapat didefinisikan sebagai seperangkat model matematika dan metode analisis dalam mengeksploitasi data yang tersedia guna menghasilkan informasi dan pengetahuan yang berguna untuk proses pengambilan keputusan yang kompleks (Vercelis, 2009). Begitu juga menurut Bentley (2017) yang menyatakan bahwa Business Intelligence (BI) digambarkan sebagai seperangkat teknik dan alat untuk akuisisi dan transformasi data mentah menjadi informasi yang bermakna dan berguna untuk keperluan analisis bisnis. Teknologi BI memberikan pandangan historis, terkini, dan prediksi pada operasi bisnis. Fungsi umum dari teknologi BI adalah pelaporan, pemrosesan analitik secara online, penambangan data, penambangan proses, pemrosesan peristiwa kompleks, manajemen kinerja bisnis, pembandingan, penambangan teks, analitik prediktif, dan analitik preskriptif. BI dapat digunakan untuk mendukung berbagai keputusan bisnis mulai dari operasional hingga strategis. Keputusan pengoperasian dasar mencakup penentuan posisi atau harga produk. Keputusan bisnis yang strategis mencakup prioritas, sasaran, dan arahan pada tingkat terluas. Dalam semua kasus, BI paling efektif ketika menggabungkan data yang berasal dari pasar di mana perusahaan beroperasi (data eksternal) dengan data dari sumber-sumber internal perusahaan ke bisnis seperti data keuangan dan operasi (data internal). Ketika digabungkan, data eksternal dan internal dapat memberikan gambaran yang lebih lengkap yang pada dasarnya, menciptakan "kecerdasan" yang tidak dapat diturunkan oleh set data tunggal. Di antara banyak kegunaan, alat BI memberdayakan organisasi untuk mendapatkan wawasan tentang pasar baru, menilai permintaan dan kesesuaian produk dan layanan untuk segmen pasar yang berbeda dan mengukur dampak upaya pemasaran.
            """
        )

    with st.container(border=True):
        st.image("https://via.placeholder.com/600x200?text=Gambar+VI.7+-+Proses+Kerja+BI,+DW,+dan+DI", use_container_width=True)
        st.caption("Gambar VI.7 Proses Kerja BI, DW, dan DI (Sumber: Sherman, R., 2014)")

    with st.container(border=True):
        st.markdown(
            """
            Integrasi data (data integration) adalah fondasi data warehouse (DW), dan DW sendiri merupakan fondasi BI. BI sebenarnya meliputi beberapa aplikasi yang diintegrasikan dan dikustomisasi sesuai dengan kebutuhan. Aplikasi-aplikasi ini bekerja dengan cara mengumpulkan data yang dimiliki perusahaan dalam sebuah DW. Program BI harus mendukung strategi bisnis perusahaan seperti yang terlihat pada Gambar VI.8. Dapat disimpulkan bahwa BI mempunyai tiga tujuan utama. Pertama, memberikan informasi yang cepat dan akurat sehingga membantu proses pengambilan keputusan yang lebih baik. Kedua, membuat data perusahaan menjadi informasi yang bisa ditindaklanjuti. Dan ketiga, menjadikan proses pengambilan keputusan lebih transparan.
            """
        )

    with st.container(border=True):
        st.markdown(
            """
            ### Data Visualization

            Penelitian menunjukkan bahwa salah satu cara paling mendasar untuk membantu dalam mengatasi kelebihan informasi adalah dengan cara memvisualisasikannya. Dengan memetakan data secara visual, tidak hanya lebih mudah untuk mencerna dan memahami informasi penting, akan tetapi juga akan lebih mudah untuk menemukan kunci dari suatu pola, tren yang signifikan, dan korelasi kuat yang mungkin sulit untuk diungkapkan. Visualisasi data adalah metode grafis atau visual penyajian data. Teknik visualisasi data akan mengeksploitasi fakta dengan mengubah semua data menjadi gambar dengan menghadirkan data dalam format gambar atau grafik. Hal ini dapat memudahkan pembuat keputusan untuk mengambil data dalam jumlah besar dengan pandangan sekilas untuk "melihat" apa yang sedang terjadi dalam sebuah data. Fitur yang menentukan visualisasi Big data adalah skala.
            """
        )

    with st.container(border=True):
        st.markdown(
            """
            ### Business Intelligence Dashboard

            BI Dashboard adalah alat visualisasi data yang menampilkan matriks dan indikator kinerja utama/Key Performance Index (KPI) dalam sebuah organisasi. BI Dashboard mampu menggabungkan dan mengelola angka serta Performance Scorecard dalam satu layar. Kelebihan dari BI Dashboard adalah memiliki antarmuka yang dapat disesuaikan dan kemampuan untuk menarik data secara real time dari berbagai sumber (Setiawan, dkk., 2013). Tujuan BI dashboard adalah untuk membantu pengguna bisnis membuat keputusan dengan informasi yang lebih baik dengan mengumpulkan, mengkonsolidasikan, dan menganalisis data serta memvisualisasikannya dengan cara yang bermakna. Beberapa manfaat penggunaan BI dashboard adalah sebagai berikut:

            a. **Identifikasi tren** – BI dashboard secara dinamis memberdayakan bisnis lintas sektor untuk mengidentifikasi dan menganalisis tren positif terkait dengan banyak kegiatan bisnis sambil mengisolasi dan mengoreksi tren negatif guna meningkatkan efisiensi organisasi.

            b. **Peningkatan efisiensi** – Untuk hasil terbaik, pengambilan keputusan harus didasarkan pada data yang tepat. Dashboard analitik bisnis meningkatkan efisiensi dengan menyajikan data real-time yang relevan, memungkinkan dalam pembuatan keputusan yang tepat dan akurat sehingga menjadi katalisator kesuksesan bisnis.

            c. **Alat swalayan** – BI dashboard menawarkan akses ke seluruh perusahaan melalui wawasan yang didorong oleh data yang sangat berharga dan dapat dibagikan dengan cepat, memberikan tingkat kelincahan serta mobilitas yang tidak bisa ditandingi oleh proses data tradisional.

            d. **Kebebasan & fleksibilitas** – Sifat perangkat lunak BI dashboard yang terpusat dan sepenuhnya portabel memungkinkan untuk mengakses dan menganalisis wawasan bisnis yang tak ternilai dari banyak perangkat di mana pun berada. Tingkat kebebasan dan fleksibilitas tersebut meningkatkan produktivitas dan kecerdasan bisnis secara konsisten yang merupakan salah satu unsur utama kesuksesan.
            """
        )

with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📈 Business Intelligence", expanded=True):
        st.markdown(
            """
            - Model dan metode analisis untuk eksploitasi data.
            - Fungsi: pelaporan, OLAP, data mining, text mining, prediktif, preskriptif.
            - Tujuan: informasi cepat, data actionable, transparansi.
            """
        )

    with st.expander("📊 Data Visualization"):
        st.markdown(
            """
            - Metode grafis untuk menyajikan data.
            - Memudahkan identifikasi pola, tren, korelasi.
            - Fitur utama: skala.
            """
        )

    with st.expander("🖥️ BI Dashboard"):
        st.markdown(
            """
            - Menampilkan KPI dalam satu layar.
            - Manfaat: identifikasi tren, efisiensi, swalayan, fleksibilitas.
            """
        )

    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Tujuan BI", "3")
        st.metric("Manfaat Dashboard", "4")

    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Vercelis (2009)
            - Bentley (2017)
            - Sherman (2014)
            - Setiawan, dkk. (2013)
            """
        )