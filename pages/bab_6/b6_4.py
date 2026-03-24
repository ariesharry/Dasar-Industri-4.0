import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
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

# ================== KOLOM MATERI UTAMA ==================
with cols[0].container(border=True):
    st.title("Data Warehouse, Data Mart, dan Data Mining")

    with st.container(border=True):
        st.markdown(
            """
            ### Data Warehouse

            William H. Inmon yang terdapat pada buku Data Mining : concepts and techniques karangan Han, Pei, & Kamber (2011) menjelaskan bahwa data warehouse merupakan kumpulan dari data yang berorientasi subjek, terintegrasi, non-volatile, dan mempunyai variansi waktu untuk mendukung pengambilan keputusan manajemen. Data warehouse adalah gudang pusat besar untuk semua data historis organisasi yang disimpan dari perspektif sejarah. Data ini dikumpulkan dari berbagai departemen dan unit perusahaan. Ada empat tugas yang bisa dilakukan dengan adanya data warehouse, yaitu pembuatan laporan, On-Line Analytical Processing (OLAP), data mining, dan proses informasi eksekutif. Data warehouse memiliki beberapa karakteristik yaitu: Subject Oriented (Berorientasi subjek), Integrated (Terintegrasi), Time-variant (Rentang Waktu), dan Non-Volatile. Gambar VI.4 merupakan kerangka konseptual data warehouse yang digunakan untuk mendukung pengambilan keputusan, bukan untuk melaksanakan pemrosesan transaksi.
            """
        )

    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-6/fig4.png", use_container_width=True)
        st.caption("Gambar VI.4 Kerangka konseptual data warehouse (Sumber: Aryuni, M., 2016)")

    with st.container(border=True):
        st.markdown(
            """
            ### Data Mart

            Data mart adalah subset dari data warehouse yang berorientasi pada lini bisnis tertentu. Data mart berisi repositori dari data yang dirangkum yang dikumpulkan untuk menganalisis pada bagian atau unit tertentu dalam suatu organisasi, misalnya, departemen penjualan. Beberapa implementasi data warehouse, data mart adalah miniatur data warehouse. Data mart sering digunakan untuk memberikan informasi kepada segmen fungsional organisasi. Contoh umum data mart adalah untuk departemen penjualan, departemen persediaan dan pengiriman, departemen keuangan, manajemen tingkat atas, dan seterusnya. Data mart juga dapat digunakan sebagai gudang segmen data untuk mencerminkan letak bisnis secara geografis di mana masing-masing daerah relatif otonom. Sebagai contoh, sebuah organisasi layanan yang besar mungkin memperlakukan pusat operasi regional sebagai unit usaha perorangan, masing-masing unit memiliki data mart yang akan memberikan kontribusi pada master gudang data.
            """
        )

    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-6/fig5.png", use_container_width=True)
        st.caption("Gambar VI.5 Contoh Penggunaan Data Mart (Sumber: panoply.io)")

    with st.container(border=True):
        st.markdown(
            """
            Gambar VI.5 merupakan contoh penggunaan data mart yang dikumpulkan dari beberapa sumber data dan dianggap sebagai bagian dari data warehouse. Data mart adalah gudang data yang dimaksudkan untuk melayani komunitas tertentu dan dirancang untuk memenuhi kebutuhan kelompok pengguna tertentu karena data mart dioptimalkan untuk melihat data dengan cara yang unik, proses desain cenderung dimulai dengan analisis kebutuhan pengguna. Data mart biasanya dikendalikan oleh satu departemen organisasi seperti penjualan, keuangan, dll.

            ### Data Mining

            Data mining merupakan salah satu cabang ilmu komputer yang relatif baru dan telah banyak diaplikasikan dalam bidang bisnis maupun sains. Pada dasarnya data mining merupakan kombinasi metode analisis data dengan algoritma untuk memproses data yang berukuran besar. Hasilnya akan ditemukan pola atau model baru yang bermanfaat dan mudah dimengerti sehingga didapatkan pengetahuan baru yang dapat dijadikan referensi untuk membuat sistem keputusan bagi para pelaku penggunanya. Menurut Bill Palace (1996) yang terdapat pada penelitian Koo dkk. (2014) menyatakan bahwa data mining adalah proses menganalisis data dari perspektif yang berbeda dan meringkasnya menjadi informasi yang berguna. Istilah lain data mining dikemukakan oleh Han & Kamber (2011) adalah Knowledge Discovery from Data (KDD). Data mining juga merupakan proses untuk menggali pengetahuan dan informasi baru dari data yang berjumlah banyak pada data warehouse, dengan menggunakan kecerdasan buatan (Artificial Intelligence), statistik dan matematika. Data mining merupakan teknologi yang diharapkan dapat menjembatani komunikasi antara data dan pemakainya. Tahapan data mining adalah sebagai berikut:

            1. **Pembersihan data (Data cleaning)** – tahap dilakukan pengisian nilai-nilai yang hilang, mengidentifikasi atau membuang outlier, dan menyelesaikan data yang tidak konsisten. Tahap ini penting dilakukan karena data yang "kotor" dapat menghasilkan keluaran yang tidak benar atau tidak bisa diandalkan kebenarannya.
            2. **Integrasi Data (Data integration)** – tahap apabila pengguna ingin menggabungkan data dari beberapa sumber. Proses penggabungan data tidak mudah karena dalam melakukannya bisa terjadi permasalahan baru, seperti: adanya atribut memiliki nama yang berbeda pada database yang menyebabkan inkonsistensi dan redundansi data. Konsep data integration bisa dilakukan untuk menyelesaikan masalah tersebut.
            3. **Seleksi Data (Data selection)** – tahap dilakukannya proses pemilihan data yang cocok terhadap proses penemuan pengetahuan yang akan dilakukan.
            4. **Transformasi Data (Data transformation)** – tahap proses mengubah data agar sesuai karakteristiknya dengan data yang diperlukan untuk proses penggalian data.
            5. **Penggalian Data (Data mining)** – tahap proses ekstraksi data sehingga menemukan suatu pola dari data tersebut.
            6. **Evaluasi Pola (Pattern evaluation)** – tahap proses evaluasi terhadap pola yang merepresentasikan pengetahuan.
            7. **Representasi pengetahuan (Knowledge representation)** – tahap untuk menampilkan pengetahuan yang telah dihasilkan dalam berbagai bentuk visual. Bentuk visual bertujuan agar representasi pengetahuan tersebut mudah dipahami.
            """
        )

    with st.container(border=True):
        st.markdown(
            """
            Data mining sangat penting digunakan dalam berbisnis, kegiatan ilmiah dalam bidang tertentu, atau kegiatan-kegiatan lainnya yang menghasilkan data dalam jumlah sangat besar. Hal ini ditunjang dengan peningkatan pemakaian komputer, kemampuan komputer, pemakaian teknologi internet dan transaksi online. Banyak keputusan bisnis dipengaruhi dari hasil pengolahan data. Dalam bidang kesehatan, pertanian atau biologi juga sering diterapkan teknik-teknik untuk memprediksi jenis kanker, memisahkan apel yang bagus, atau mengelompokkan gen misalnya. Dalam contoh diatas, jelaslah bahwa data mining tidak terbatas dipakai untuk keperluan bisnis. Bidang lain seperti astronomi, meteorologi, mikrobiologi, manufaktur adalah contoh dimana data mining diterapkan.

            Bagi perusahaan besar yang memerlukan informasi dari data yang dimilikinya, dibutuhkan suatu cara pengolahan data secara lebih cepat dan lebih bisa dipercaya dengan adanya jumlah data yang semakin besar. Data mining melibatkan penggunaan metode atau tool untuk mendeteksi pola dan melakukan tugas prediksi. Ketepatan prediksi inilah memberikan keuntungan yang diharapkan dalam bisnis. Walaupun sulit didapatkan prediksi yang sempurna, akan tetapi prediksi yang cukup bagus pun sudah bisa digunakan untuk meningkatkan profit bagi perusahaan. Sebagai contoh retail bisa membuat segmentasi kostumernya berdasarkan beberapa informasi yang dimiliki perusahaan. Segmentasi ini bisa digunakan oleh perusahaan untuk melakukan penawaran produknya agar tepat sasaran. Sudah seharusnya perusahaan mengirim tawarannya hanya ke calon customer yang potensial, tidak semua customernya ditawari. Perusahaan perbankan bisa menggunakan customer relationship management (CRM) untuk memperkirakan value dari customer tertentu ataupun memprediksi tentang kemungkinan apakah peminjam kreditnya akan membayar tepat waktu. Dalam hal ini, CRM akan mempergunakan teknik data mining untuk melakukan beberapa fungsi:

            1. **Klastering** – Mengelompokkan obyek ke dalam beberapa kelompok berdasarkan kemiripan antar obyek, dimana dalam satu klaster harus berisi obyek yang saling mirip dan antar klaster obyek saling tidak mirip. Klastering ini tidak memerlukan data pelatihan yang sudah diberi label.
            2. **Klasifikasi** – Melakukan pengelompokkan obyek berdasarkan kelompok yang sudah ada. Berbeda dengan klastering, klasifikasi ini memerlukan data pelatihan yang sudah diberi label kelompok/kelas. Prediksi pengelompokkan dilakukan dengan membangun model terlebih dahulu melalui proses pelatihan menggunakan data yang sudah kita siapkan. Setelah model terbentuk dari proses pelatihan, data baru bisa dikelompokkan menggunakan model tersebut.
            3. **Regresi/estimasi** – Regresi pada dasarnya mirip dengan klasifikasi, yakni memerlukan data pelatihan yang sudah diberi label. Bedanya, output klasifikasi adalah nilai diskrit, sedangkan output regresi adalah nilai kontinyu. Regresi ini mencari hubungan antara atribut predictor dan atribut dependen, dimana atribut dependennya juga berupa nilai kontinyu. Contoh regresi adalah memprediksi nilai kurs rupiah terhadap dolar.
            4. **Asosiasi** – Melakukan asosiasi antar obyek dalam satu set data, biasanya data transaksional. Asosiasi dilakukan dengan menghitung berapa kali dalam suatu set transaksi yang mengandung dua item atau lebih yang berhubungan. Sering ada yang menyebut Market Basket Analysis.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("🏛️ Data Warehouse", expanded=True):
        st.markdown(
            """
            - Kumpulan data berorientasi subjek, terintegrasi, non‑volatile, time‑variant.
            - Mendukung pengambilan keputusan.
            - Empat tugas: laporan, OLAP, data mining, informasi eksekutif.
            """
        )

    with st.expander("📦 Data Mart"):
        st.markdown(
            """
            - Subset data warehouse untuk unit bisnis tertentu (misal: sales, finance).
            - Dirancang untuk memenuhi kebutuhan spesifik pengguna.
            - Dapat berdiri sendiri atau menyumbang ke data warehouse.
            """
        )

    with st.expander("⛏️ Data Mining"):
        st.markdown(
            """
            - Menemukan pola baru dari data besar.
            - 7 tahapan: cleaning, integration, selection, transformation, mining, evaluation, representation.
            - 4 teknik utama: clustering, klasifikasi, regresi, asosiasi.
            """
        )

    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Tahapan Data Mining", "7")
        st.metric("Teknik Utama", "4")

    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Han, Pei & Kamber (2011)
            - Palace (1996)
            - Koo dkk (2014)
            - Aryuni (2016)
            """
        )