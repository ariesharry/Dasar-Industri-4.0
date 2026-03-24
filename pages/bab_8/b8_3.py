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
    st.title("Pembelajaran Mesin (Machine Learning)")

    with st.container(border=True):
        st.markdown(
            """
            Saat ini, AI didasarkan pada pembelajaran mesin, dan pembelajaran mesin pada dasarnya berbeda dari statistik. Pembelajaran mesin memiliki basis statistik, tetapi beberapa asumsi memiliki perbedaan dengan statistik karena tujuannya berbeda (Mueller, J. P. & Massaron, L., 2016). Sedangkan, Müller, A. C. & Guido, S. (2016) menjelaskan bahwa pembelajaran mesin adalah tentang mengekstraksi pengetahuan dari data. ML merupakan bidang penelitian antara ilmu statistik, kecerdasan buatan, dan ilmu komputer dan juga dikenal sebagai analitik prediktif atau pembelajaran statistik. Pembelajaran mesin (Machine Learning) adalah pemograman komputer untuk mencapai kriteria/performance tertentu dengan menggunakan sekumpulan data yang dilatih atau pengalaman masa lalu (Primartha, R., 2018). ML melibatkan berbagai disiplin ilmu seperti statistika, ilmu komputer, matematika, bahkan neurologi. Ilmu statistika digunakan untuk membuat model matematika baik bersifat prediksi maupun deskriptif atau gabungan keduanya. ML dianalogikan sebagai buku resep masakan dan algoritma dianalogikan sebagai pisau. Semakin sesuai ukuran dan tajam pisaunya maka semakin mudah koki untuk memotong bahan makanan. Pembelajaran mesin sangat penting karena memungkinkan dengan cepat dan otomatis menghasilkan model yang dapat menganalisis data yang lebih besar, lebih kompleks, dan memberikan hasil lebih cepat dan lebih akurat, bahkan dalam skala yang sangat besar. Dengan membangun model yang tepat, organisasi memiliki peluang yang lebih baik untuk mengidentifikasi peluang yang menguntungkan atau menghindari risiko yang tidak diketahui.
            """
        )
        st.image("https://via.placeholder.com/600x250?text=Gambar+VIII.5+-+Kategori+Machine+Learning", use_container_width=True)
        st.caption("Gambar VIII.5 Kategori Machine Learning (Sumber: data-flair.training)")

        st.markdown(
            """
            Secara umum, algoritma ML dikelompokkan menjadi tiga kategori seperti yang terlihat pada Gambar VII.5. Primartha, R. (2018) menjelaskan ketiga kategori tersebut sebagai berikut:

            ### a. Supervised Learning
            Algoritma supervised learning menggunakan sekumpulan data yang dilatih untuk memandu dan mengajari komputer sehingga menghasilkan keluaran yang sesuai harapan. Analogi algoritma ini adalah seperti seorang guru yang sedang mengajari anak-anak berhitung dimana data pelatihan bertindak sebagai guru, sedangkan algoritma bertindak sebagai murid. Permasalahan yang terkait dengan algoritma ini dikategorikan menjadi dua jenis, pertama mengenai klasifikasi (Classification), sebagai contoh keluaran yang diinginkan berbentuk kategori seperti : pria/wanita, sakit/sehat, tinggi/rendah, dll. Kedua mengenai regresi (regression) yang bertujuan untuk memprediksi outcome dari input (sampel yang diberikan), dimana variabel outputnya berbentuk nilai aktual, seperti tinggi badan, curah hujan, dan lain-lain.

            ### b. Unsupervised Learning
            Pada unsupervised learning persoalan diproses menggunakan data yang belum dilatih untuk memodelkan struktur data. Algoritma ini bermanfaat untuk kasus penemuan relasi implisit dari set data yang tidak berlabel. Permasalahan pada algoritma ini dikelompokkan menjadi tiga kategori. Pertama, association yang bertujuan untuk menemukan peluang berdasarkan keterkaitan dari item-item dalam sebuah kumpulan, sebagai contoh jika pelanggan membeli teh celup maka kemungkinan besar customer juga membeli gula. Kedua, clustering yang bertujuan untuk mengelompokan sampel dalam kluster yang sama berdasarkan kemiripan, sebagai contoh pengelompokan pelanggan berdasarkan perilaku pembelian. Ketiga, dimensionality reduction yang mengurangi sejumlah variabel dari set data akan tetapi dipastikan informasi yang penting masih tersedia.

            ### c. Reinforcement Learning (RL)
            Reinforcement Learning merupakan metode pembelajaran yang dipengaruhi oleh feedback dari lingkungan dengan teknik pembelajaran yang berulang-ulang dan menyesuaikan. Contoh penerapan RL adalah pada bidang robotic, dimana sebuah robot dapat belajar untuk menghindari tabrakan dengan cara menerima feedback negatif jika robot tersebut menabrak halangan tertentu. Robot akan dibiarkan berjalan tanpa dipandu. Robot akan belajar dari pengalaman sebelumnya untuk menentukan rute paling optimal.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi ML", expanded=True):
        st.markdown(
            """
            - Mengekstraksi pengetahuan dari data.
            - Pemrograman komputer untuk mencapai kinerja tertentu berdasarkan data latih.
            - Bidang antara statistik, AI, dan ilmu komputer.
            """
        )

    with st.expander("🔢 Tiga Kategori ML"):
        st.markdown(
            """
            **Supervised Learning**: data berlabel, klasifikasi & regresi.
            **Unsupervised Learning**: data tak berlabel, association, clustering, dimensionality reduction.
            **Reinforcement Learning**: belajar dari feedback lingkungan.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Kategori ML", "3 (Supervised, Unsupervised, Reinforcement)")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Mueller & Massaron (2016)
            - Müller & Guido (2016)
            - Primartha, R. (2018)
            """
        )