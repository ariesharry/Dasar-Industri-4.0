import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

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

with cols[0].container(border=True):
    st.title("Historian Data, Real Time Database dan Data Lake")

    with st.container(border=True):
        st.markdown(
            """
            ### Data Historis

            Data historis adalah data yang tersimpan dari waktu ke waktu untuk menggambarkan suatu perkembangan atau kecenderungan suatu kejadian. Data historis banyak digunakan pada berbagai industri, minyak dan gas, manufaktur, dan segala jenis rekayasa proses. Data tersebut, khususnya di industri manufaktur dirancang untuk mengukur proses produksi tertentu, seperti: total cacat untuk perubahan tertentu, getaran kipas motor pada jalur produksi, tingkat pH untuk instalasi pengolahan air, dan lain-lain. Data historis adalah cara yang efisien untuk mengumpulkan dan menyimpan data deret waktu (time series). Data historis juga dapat berasal dari jalur produksi, rute transportasi, perangkat jaringan, satelit, dan perangkat lainnya. Data disimpan dengan cap waktu dan informasi identitas lainnya seperti ID perangkat dan lokasi. Informasi data tersebut dapat digunakan secara real-time atau disimpan untuk analisis offline.

            Data historis memiliki kelemahan dalam beberapa kasus, data ini tidak pernah digunakan oleh staf operasi dan pemeliharaan karena pengolahannya membutuhkan keterampilan dan perangkat lunak khusus yang menjadikannya mahal dan sulit untuk dibobol. Kelemahan lain dari data historis adalah lisensi perangkat lunak dan biaya yang besar untuk mendapatkan semua jumlah data yang dibutuhkan. Kemudian teknologi data historis yang tidak berubah selama beberapa dekade terakhir berarti sulit untuk mengintegrasikan data ini ke dalam aplikasi berbasis web modern.
            """
        )

    with st.container(border=True):
        st.markdown(
            """
            ### Realtime Database

            Database merupakan kumpulan data berupa file, arsip, atau tabel yang tersusun sedemikian rupa menurut aturan tertentu, saling terhubung dan tersimpan dalam media elektronik yang mana pengguna mudah dalam mengelolanya serta mudah dalam mendapatkan informasi. Real-time Database adalah sistem pengolahan yang pemrosesannya menggunakan waktu nyata dan dirancang untuk menangani beban kerja dimana kondisinya dapat berubah terus-menerus (Bunchmann, 2005), berbeda dengan database tradisional yang mengandung data yang terus-menerus, sebagian besar tidak terpengaruh oleh waktu. Sebagai contoh, pasar saham berubah dengan cepat dan dinamis. Real-time database berguna untuk akuntansi, perbankan, hukum, catatan medis, multimedia, kontrol proses, sistem reservasi, dan analisis data ilmiah.
            """
        )

    with st.container(border=True):
        st.markdown(
            """
            ### Data Lake

            Data lake (danau data) adalah gudang penyimpanan yang menyimpan sejumlah besar data mentah dalam format aslinya, termasuk data terstruktur, semi-terstruktur, dan tidak terstruktur. Tujuan paling sederhana dari data lake adalah menggunakan setiap data yang dihasilkan oleh suatu organisasi untuk memberikan wawasan yang berharga dengan rincian lebih dalam (Khine dan Wang, 2018). Sekarang ini, konsep data lake sedang mencoba untuk menantang gudang data tradisional yang andal guna menyimpan data kompleks yang heterogen. Konsep data lake adalah mengkonsolidasikan semua set jenis data apapun yang terdapat pada suatu organisasi guna dapat dianalisis dan diintegrasikan menjadi data baru sehingga memberikan fleksibilitas, skalabilitas dan ketangkasan yang dibutuhkan oleh perusahaan untuk mengelola volume, jenis, dan ketersediaan data waktu nyata yang dihasilkan saat ini. Dengan kata lain, data yang terdapat dalam data lake adalah data mentah yang belum diproses atau dianalisis.

            Data lake dicirikan oleh tiga atribut utama: **kumpulkan semuanya** (collecting everything), **menyelam di mana saja** (dive in anywhere), dan **akses fleksibel** (flexible access).

            Data lake sangat penting karena komponen-komponennya menyediakan berbagai fungsi yang membantu perusahaan untuk mendapatkan lebih banyak konsumen, meningkatkan produktivitas, dan membuat keputusan. Semuanya berkontribusi untuk meningkatkan pertumbuhan bisnis dengan pesat. Keuntungan tersebut dapat diperoleh melalui cara kerja berikut:

            a. **Mengindeks data** – Jenis data dan database disimpan, termasuk diantaranya data operasional, data dari aplikasi bisnis, atau data yang bersifat non-relasional seperti data yang diperoleh dari aplikasi mobile dan media sosial. Meskipun ini merupakan data mentah, kita bisa memahami isi data dengan adanya katalog, crawling, dan indeks data.

            b. **Machine learning** – Perusahaan dapat memperoleh gambaran operasional dan marketing melalui data yang diperoleh dari data lake. Data-data ini menggambarkan tren serta pola perilaku konsumen. Kemudian, perusahaan dapat menerapkan machine learning untuk membuat model prediksi dan perkiraan dari data-data tersebut.

            c. **Mengembangkan interaksi dengan konsumen** – Data lake mampu menggabungkan data konsumen dari platform CRM dengan hasil analisis media sosial. Penggabungan tersebut juga dapat dilakukan dengan platform marketing yang menggambarkan riwayat pembelian konsumen. Hal ini berguna agar perusahaan dapat mengidentifikasi mana konsumen yang paling menguntungkan, apa yang melatarbelakangi pola perilaku konsumen, serta reward seperti apa yang dapat meningkatkan kesetiaan konsumen.

            d. **Analisis** – Keberadaan data lake memungkinkan para data scientist, pengembang data, serta siapa pun yang bergelut dalam bidang terkait untuk mengakses data sesuai kerangka dan perangkat analisis yang mereka miliki. Hal ini dapat dilakukan analisis tanpa perlu memindahkan data dari satu sistem ke sistem yang lain.

            Data lake adalah fondasi utama yang dibutuhkan oleh alat analisis untuk proses analisisnya. Data lake merupakan tempat penyimpanan utama dari big data yang dikumpulkan. Akurasi dalam pengambilan keputusan hanya bisa diperoleh ketika organisasi memiliki fondasi yang kuat dengan data lake berkualitas tinggi.
            """
        )

with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Data Historis", expanded=True):
        st.markdown(
            """
            - Data time series untuk analisis kecenderungan.
            - Digunakan di industri manufaktur, migas.
            - Kelemahan: mahal, sulit diintegrasi.
            """
        )

    with st.expander("⚡ Real-time Database"):
        st.markdown(
            """
            - Pemrosesan data secara waktu nyata.
            - Cocok untuk sistem dinamis (saham, kontrol proses).
            - Contoh aplikasi: perbankan, reservasi.
            """
        )

    with st.expander("🌊 Data Lake"):
        st.markdown(
            """
            - Menyimpan data mentah dalam format asli.
            - Atribut: collecting everything, dive in anywhere, flexible access.
            - Mendukung machine learning dan analisis lanjutan.
            - Fondasi utama big data.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Atribut Data Lake", "3")
        st.metric("Kegunaan Data Lake", "Analisis, ML, interaksi konsumen")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Bunchmann (2005)
            - Khine & Wang (2018)
            """
        )