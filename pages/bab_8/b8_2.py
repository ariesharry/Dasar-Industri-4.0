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
    st.title("Klasifikasi dan Mekanisme Kerja Kecerdasan Buatan (Artificial Intelligence)")

    with st.container(border=True):
        st.markdown(
            """
            Bidang AI telah berkembang ke berbagai bidang yang memiliki tujuan untuk menciptakan mesin cerdas yang mampu menalar, merencanakan, memecahkan masalah, berpikir secara abstrak, memahami ide-ide kompleks, belajar dengan cepat dan belajar dari pengalaman. Pada praktiknya, kecerdasan yang ditiru secara artifisial ini adalah untuk mencerminkan kemampuan yang luas dan mendalam untuk memahami lingkungannya sehingga dapat mengetahui apa yang harus dilakukan dalam situasi yang tak terbatas. Proses yang terjadi dalam AI mencakup learning, reasoning, dan self-correction.

            Gambar VIII.2 menggambarkan inti masalah kecerdasan buatan mencakup pemrograman komputer dengan kriteria atau klasifikasi sebagai berikut (Martin, 2015):

            """
        )
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-8/fig2.png", use_container_width=True)

        st.caption("Gambar VIII.2 Inti masalah kecerdasan buatan")

        st.markdown(
            """

            1. Deduction, reasoning, and problem solving
            Pada awal penelitian AI, proses penalaran diinduksi melalui langkah-langkah meniru proses manusia dalam menyelesaikan teka-teki atau deduksi logis. Namun,

            2. Knowledge presentation
            Untuk meniru manusia, AI perlu menggabungkan banyak sekali pengetahuan tentang objek, sifat- sifatnya, kategori-kategori dan hubungan antar satu sama lain. Selain itu, harus menerapkan situasi dan keadaan, sebab, akibat dan ide yang abstrak. Bidang AI menggunakan pendekatan ontologis untuk representasi pengetahuan, yaitu pengetahuan dipostulatkan dalam set konsep yang hubungannya didefinisikan dalam suatu domain.

            3. Planning
            AI harus mampu membangun solusi yang kompleks dan dioptimalkan dalam ruang multidimensi dan melakukan

            4. Perception: Computer Vision
            Persepsi mesin mewakili kemampuan interpretasi input yang menyerupai proses persepsi manusia melalui indera. Masalah-masalah penting yang dicoba untuk diatasi adalah masalah persepsi yang komprehensif, transmisi ke inti entitas yang cerdas dan sistem respons (yaitu, persepsi mesin menghadapi kesulitan dalam fitur teknik dan komputasi).

            5. Machine Learning
            Pembelajaran mesin adalah konstruksi dan studi algoritma yang memungkinkan sistem AI untuk membuat prediksi dan keputusan berdasarkan input data dan pengetahuan.

            6. Robotics: Motion and Manipulation
            Tujuan dalam robotika menggabungkan rekayasa dengan studi kecerdasan buatan dan berputar di sekitar pertanyaan: manipulasi objek; navigasi; lokalisasi; pemetaan; perencanaan gerak.

            7. Natural Language Processing
            Pemrosesan Bahasa Alamiah (Natural Language Processing/NLP) merupakan cabang kecerdasan buatan yang membantu komputer memahami, menafsirkan, dan memanipulasi bahasa manusia. NLP menarik dari banyak disiplin ilmu, termasuk ilmu komputer dan linguistik komputasional, dalam usahanya untuk mengisi kesenjangan

            8. Social Intelligence
            Kecerdasan sosial (Social Intelligence) adalah istilah umum antara berbagai disiplin ilmu termasuk filsafat, ilmu sosial / sosiologi, ekonomi, ilmu hukum, psikologi, dll, dan ilmu komputer. Secara umum, kecerdasan sosial adalah kemampuan untuk memahami orang lain dan bertindak secara rasional dan emosional dalam hubungan dengan orang lain. Ini adalah kemampuan yang tidak hanya dimiliki oleh manusia tetapi juga agen buatan, sebagaimana dimodelkan dalam kecerdasan buatan dan penelitian berbasis agen pada khususnya (Herzig, A., dkk, 2017).

            """
        )
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-8/fig3.png", use_container_width=True)
        st.caption("Gambar VIII.3 Mekanisme Kerja Kecerdasan Buatan (Artificial Intelligence)")

        st.markdown(
            """
            Berdasarkan klasifikasi AI di atas dapat diketahui bahwa AI bekerja dengan cara menggabungkan sejumlah besar data, baik dari data yang terstruktur maupun tak terstuktur yang disimpan pada database dan server dengan pemrosesan yang cepat, berulang dan mengunakan algoritma cerdas, memungkinkan perangkat lunak untuk belajar secara otomatis dari pola atau fitur dalam data. Hasil transformasi data tersebut menjadi wawasan yang ditindaklanjuti guna pengambilan keputusan bagi suatu perusahaan. Deskripsi secara visual mengenai mekanisme kerja kecerdasan buatan dapat dilihat pada Gambar VIII.3. Sebagai salah satu contoh, adanya data penggunaan listrik dari konsumen yang terdapat pada database akan dikelola lebih lanjut menggunakan algoritma untuk melihat pola beban penggunaan listrik pada pagi, siang dan malam hari sehingga didapatkan hasil prediksi beban listrik yang digunakan oleh pelanggan pada waktu tersebut.

            Artificial intelligence, Machine Learning dan Deep Learning menjadi trending topik dunia dalam berbagai unit aspek bisnis. Hubungan antara ketiga istilah tersebut diibaratkan AI sebagai payung yang lebih luas di mana ML dan DL berada dalam lingkupnya. Primartha, R. (2018) menjelaskan bahwa AI berbicara tentang konsep umum, bagaimana melakukannya, metode apa yang digunakan, dan hal-hal teknis lainnya yang belum dapat didefiniskan secara detail. Gambar VIII.4. memperlihatkan bahwa ML dan DL merupakan cabang atau bagian dari AI. Tugas machine learning adalah melatih mesin untuk belajar menggunakan algoritma yang umum dengan memberi data, lalu algoritma itu akan mencari hal-hal yang menarik dalam data yang kita berikan, hingga akhirnya sistem AI akan membangun pengetahuan berdasarkan data tersebut. Sedangkan DL merupakan subset dari ML yang membuat komputasi jaringan saraf multi layer yang layak.
            """
        )
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-8/fig4.png", use_container_width=True)
        st.caption("Gambar VIII.4 Keterkaitan antara AI, ML, dan DL")

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Klasifikasi AI (Martin, 2015)", expanded=True):
        st.markdown(
            """
            1. Deduction, reasoning, problem solving
            2. Knowledge presentation
            3. Planning
            4. Perception (Computer Vision)
            5. Machine Learning
            6. Robotics (motion, manipulation)
            7. Natural Language Processing
            8. Social Intelligence
            """
        )

    with st.expander("⚙️ Mekanisme Kerja AI"):
        st.markdown(
            """
            - Menggabungkan data terstruktur & tidak terstruktur.
            - Pemrosesan cepat dengan algoritma cerdas.
            - Menghasilkan wawasan untuk pengambilan keputusan.
            """
        )

    with st.expander("🔗 Hubungan AI, ML, DL"):
        st.markdown(
            """
            - AI sebagai payung besar.
            - ML adalah cabang AI.
            - DL adalah subset dari ML (jaringan saraf multilayer).
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Klasifikasi AI", "8 bidang")
        st.metric("Proses AI", "Learning, Reasoning, Self-correction")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Martin (2015)
            - Herzig, A., dkk (2017)
            - Primartha, R. (2018)
            """
        )