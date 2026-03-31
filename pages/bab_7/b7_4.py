import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
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

# ================== KOLOM MATERI UTAMA ==================
with cols[0].container(border=True):
    st.title("Digital Twin")

    with st.container(border=True):
        st.markdown(
            """
            Salah satu bentuk simulasi dalam suatu sistem industri 4.0 yang paling terkenal adalah digital twin. Shaw, K. & Fruhlinger, J. (2019) mendefinisikan digital twin sebagai representasi digital dari obyek fisik atau sistem yang dapat digunakan oleh data scientist dan profesi TI untuk menjalankan simulasi sebelum perangkat yang sebenarnya dibangun dan digunakan. Digital twin bergerak melampaui bidang manufaktur, dan masuk ke dunia konvergensi IoT, kecerdasan data, dan analitik data. Bahkan sekarang cakupan teknologi digital twin ini semakin meluas dan dapat mencakup bangunan, pabrik, dan kota.

            Pada dasarnya, digital twin adalah sebuah model virtual yang dapat membantu manusia mengumpulkan informasi berbasis data dan prediksi yang akurat guna melakukan pengambilan keputusan yang berpengaruh pada produktivitas perusahaan. Digital twin akan menggunakan data yang disediakan oleh sensor untuk memahami keadaan sekitar, merespon setiap adanya perubahan, meningkatkan operasi, dan menambah nilai. Digital twin ini bertujuan untuk menciptakan kembaran mesin dalam bentuk digital untuk diambil datanya dengan lebih detail.

            Digital twin pertama kali diperkenalkan pada tahun 2003 di University of Michigan oleh Dr. Michael Grieves. Digital twin merupakan sebuah representasi visual (model 3-D) dari sebuah produk, proses, maupun layanan. Digital twin dapat digunakan dalam desain produk, simulasi, monitoring dan merupakan konsep penting dari Internet of Things. Perpaduan dari dunia nyata dan dunia virtual membuka jalan untuk memonitor sistem dan menganalisis data yang dapat membantu mencegah permasalahan sebelum terjadi. Manfaat lebih jauh dari digital twin ini dapat menemukan kesempatan-kesempatan baru dalam pengembangan sebuah teknologi di masa depan dengan memanfaatkan simulasi. Digital twin menjadi sangat penting untuk bisnis industri karena cara kerjanya yang efisien dengan menggunakan cloud-based virtual image dari produk yang sedang dikelola yang dapat dengan mudah diakses kapanpun.

            Menurut Michael Grieves, konsep dari digital twin membutuhkan tiga elemen yaitu :

            1. Benda fisik di dunia nyata.
            2. Digital twin dari benda fisik tersebut di ruang virtual.
            3. Informasi yang menghubungkan kedua elemen sebelumnya.

            Sebelum diperkenalkannya konsep digital twin ini, perusahaan manufaktur biasanya membuat model virtual dari sebuah produk baru yang akan di produksi (seperti mobil, sepeda, dll) terlebih dahulu menggunakan computer aided design (CAD) yang akan dilanjutkan dengan mengubah model virtual ini menjadi sebuah benda fisik yang sebenarnya, dan selanjutnya mereka akan membuang ataupun menyimpan model virtual tersebut karena sudah tidak lagi digunakan. Dengan konsep digital twin, virtual model yang sudah dibuat tidak lagi dibuang melainkan digunakan dengan dihubungkan ke benda fisik melalui sebuah cloud-based system. Selain itu, benda fisik tersebut juga tidak menggunakan komponen yang sama seperti pengembangan sebelumnya, melainkan dilengkapi dengan komponen pintar disertai dengan sensor. Sensor yang terhubung dengan benda fisik mengumpulkan data real-time mengenai status, kondisi kerja, atau posisi yang diintegrasikan dengan benda fisik dan mengirim data tersebut kembali ke digital twin. Sebagai contoh sensor mendeteksi ketika mesin mobil harus ganti oli, dan digital twin dari mobil tersebut akan memiliki gambar overlay yang mengindikasikan informasi baru tersebut, yang dapat tampil ke smartphone pemilik mobil.

            Digital twin bekerja pada 3 tahap, yaitu melihat, berpikir, dan melakukan.

            ### 1. Tahap Melihat
            Pada tahap pertama “melihat” dimana digital twin mengambil data untuk menciptakan kembaran virtual yang bisa bekerja secara bersamaan. Pada digital twin, perpaduan antara sebuah integritas sebuah software, hardware, fisika, dan pembelajaran mesin. Ini semua harus saling terintegrasi untuk menghasilkan sebuah keputusan yang dibutuhkan. Caranya dengan menghubungkan peralatan industri dengan internet untuk mendapatkan data. Kemudian data tersebut dimasukkan ke digital twin.

            ### 2. Tahap Berpikir
            Pada tahap kedua “berpikir” dimana digital twin dapat melihat korelasi dalam data yang diolah dengan machine learning. Apa saja yang sesungguhnya menyebabkan permasalahan. Dalam hal ini digital twin dapat merekomendasikan beberapa tindakan yang dapat dilakukan.

            ### 3. Tahap Melakukan
            Terakhir pada tahap ketiga yaitu “melakukan” maksudnya adalah bagian kegiatan pemeliharaan dan tindakan mengontrol mesin.

            Keakuratan digital twin dilakukan dengan dua cara yaitu yang pertama dengan melakukan pengumpulan dari semua data dari digital twin dan membangun template dari koleksi data tersebut. Dengan membuat template dari mesin mesin pada industri tersebut pelanggan dapat melihat data sehingga pelanggan dapat memanfaatkan data tersebut dengan cepat. Hal kedua yaitu dengan memprediksi. Ini berdasarkan platform cloud. Ketika anda menyimpan informasi di cloud, kemudian informasi tersebut dapat diakses pihak yang berkepentingan.
            """
        )
        st.image("https://via.placeholder.com/600x250?text=Gambar+VII.2+-+Digital+Twin", use_container_width=True)
        st.caption("Gambar VII.2 Digital Twin (Sumber: The Seebo Platform)")

        st.markdown(
            """
            Digital twin memiliki empat jenis, yaitu komponen (parts), mesin, proses, dan sistem. Digital twin digemari oleh pelanggan karena efisiensi harga dan juga dapat membantu pelanggan untuk meningkatkan produktifitas dan keuntungan sebuah perusahaan.

            ### Berikut ini contoh aplikasi dari digital twin :

            #### 1. Hara Agriculture
            Hara Agriculture merupakan solusi digital untuk meningkatkan produktivitas lahan pertanian dan perkebunan yang menggunakan platform Predix. Ini adalah terobosan mutakhir buatan anak negeri, yakni Dattabot, dan risetnya sejak 2014. Pengguna solusi ini adalah petani, petugas penyuluh, dan perusahaan pertanian. Hara Agriculture bekerja dengan cara mengumpulkan data lahan melalui aplikasi bergerak, sensor Predix, nano satelit, dan pesawat nirawak, dan kemudian melakukan pengolahan data dan analisis. Solusi tersebut sudah dipakai di lahan pertanian padi dan jagung seluas 1.500 hektar di Lampung dan Merauke untuk mendapatkan hasil perbandingan. Melalui nano satelit, dengan memperoleh data citra satelit setiap hari, seperti indeks vegetasi dan kadar air akan dianalisis. Data tersebut akan menunjukkan riwayat lahan. Dari sana bisa diperoleh rekomendasi mengenai volume penggunaan pestisida dan pupuk yang tepat. Data hasil analisis dipakai tim dan pengurus pertanian untuk mengambil keputusan dalam pengelolaan lahan.

            #### 2. e-Fishery
            eFishery merupakan teknologi pemberi pakan ikan otomatis buatan Indonesia, eFishery menggabungkan pemberian pakan otomatis dengan algoritma dan sensor untuk meningkatkan efisiensi pakan dalam bisnis perikanan. Fitur-fitur yang terdapat di eFishery adalah smart feeder dan real time monitoring. Dengan smart feeder pengguna dapat memberikan pakan ikan pada waktu penjadwalan yang teratur dan dengan jumlah yang tepat sesuai kebutuhan ikan. Sementara itu dengan real time monitoring pengguna dapat melihat laporan pemberian pakan secara langsung, kapanpun dan dimanapun melalui smartphone.

            eFishery dilengkapi dengan sensor pendeteksi ikan yang memungkinkan pengguna untuk melakukan pemberian pakan pada waktu yang tepat. Alat ini juga dilengkapi dengan teknologi mobile sehingga pengguna dapat mengontrol alat ini menggunakan smartphone.

            #### 3. ElectRx
            ElectRx merupakan sebuah teknologi atau sistem yang dapat memonitor dan mengontrol proses biologis dalam tubuh melalui sistem saraf. Proses kerja ElectRx yaitu dengan memantau serta mencatat proses biologis dalam tubuh, kemudian dilakukan diagnosa yaitu proses evaluasi untuk menentukan kesehatan, selanjutnya dilakukan perawatan yaitu proses pengobatan yang diperlukan. Dengan adanya teknologi pengontrol saraf akan membantu kita dalam pemulihan kesehatan tanpa diperlukannya operasi atau obat-obatan.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi Digital Twin", expanded=True):
        st.markdown(
            """
            - Representasi digital objek fisik.
            - Digunakan untuk simulasi sebelum implementasi.
            """
        )

    with st.expander("🧩 Tiga Elemen"):
        st.markdown(
            """
            1. Benda fisik.
            2. Digital twin di ruang virtual.
            3. Informasi penghubung.
            """
        )

    with st.expander("🔄 Tiga Tahap"):
        st.markdown(
            """
            - **Melihat**: ambil data.
            - **Berpikir**: analisis ML.
            - **Melakukan**: tindakan.
            """
        )

    with st.expander("🌱 Contoh Aplikasi"):
        st.markdown(
            """
            - Hara Agriculture (pertanian).
            - eFishery (pakan ikan otomatis).
            - ElectRx (kesehatan).
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Tahapan Digital Twin", "3 (lihat, pikir, lakukan)")
        st.metric("Jenis Digital Twin", "4 (parts, mesin, proses, sistem)")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Shaw, K. & Fruhlinger, J. (2019)
            - Grieves, M. (2003)
            """
        )