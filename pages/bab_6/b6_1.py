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
    st.title("Pengertian, Karakteristik dan Manfaat Big Data")

    with st.container(border=True):
        st.markdown(
            """
            Menurut pendapat beberapa ahli, big data memiliki berbagai pengertian antara lain:

            1. Big data adalah istilah yang menggambarkan volume data yang besar, baik data yang terstruktur maupun data yang tidak terstruktur (Permana, 2016).

            2. Big data adalah data yang memiliki skala (volume), distribusi (velocity), keragaman (variety) yang sangat besar, dan atau abadi, sehingga membutuhkan penggunaan arsitektur teknikal dan metode analitik yang inovatif untuk mendapatkan wawasan yang dapat memberikan nilai bisnis baru atau informasi yang bermakna (McKinsey Global, 2011 dalam Cholissodin dkk, 2016).

            3. Big data adalah sekumpulan data yang begitu besar atau kompleks dimana tidak bisa ditangani lagi dengan sistem teknologi komputer konvensional (Hurwitz, dkk., 2013).

            4. Big data adalah proses menyampaikan wawasan pengambilan keputusan secara cepat dengan menggunakan orang dan teknologi agar dapat menganalisis data dari berbagai jenis dan sumber dalam jumlah yang besar guna menghasilkan aliran pengetahuan yang selanjutnya akan ditindaklanjuti (Kalivas dan Overly, 2015).

            Berdasarkan beberapa pengertian diatas dapat disimpulkan bahwa big data adalah sekumpulan data yang memiliki volume yang besar yang dianalisis dengan bantuan teknologi untuk memberikan nilai tambah terhadap proses bisnis.
            """
        )
    
    with st.container():
        # Buat 3 kolom untuk center (kiri - tengah - kanan)
        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])

        with col2:
            # Embed video
            st.markdown(
                """
                <div style="
                    border-radius: 10px;
                    overflow: hidden;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                    margin-bottom: 30px;
                ">
                    <iframe 
                        width="100%" 
                        height="400" 
                        src="https://www.youtube.com/embed/aC2CmTTZTVU"
                        title="YouTube video"
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen>
                    </iframe>
                </div>
                """,
                unsafe_allow_html=True
            )

    with st.container(border=True):
        st.markdown(
            """
            ### 📊 Karakteristik Big Data (5V)

            Big data memiliki 5 karakteristik utama yang dikenal dengan 5Vs yaitu volume, velocity, variety, veracity dan value.

            1. **Volume (jumlah data)**  
            Volume dari big data mengacu pada besarnya data yang dihasilkan atau diperoleh. Big data memiliki jumlah data yang sangat besar sehingga dalam proses pengolahannya dibutuhkan suatu penyimpanan yang besar.

            2. **Velocity (kecepatan data)**  
            Velocity mengacu pada peningkatan kecepatan di mana data ini dibuat, dan peningkatan kecepatan di mana data dapat diproses, disimpan, dan dianalisis oleh hubungan database.

            3. **Variety (keragaman data)**  
            Variety mengacu pada bentuk format data yang beragam baik terstruktur maupun tidak terstruktur yang tergantung banyaknya sumber data.

            4. **Veracity (ketidakakuratan data)**  
            Veracity mengacu pada sulitnya memastikan kebenaran suatu data akibat banyaknya data yang ada dan dari berbagai sumber.

            5. **Value (Nilai data)**  
            Value mengacu pada kemampuan data dapat diolah menjadi sesuatu yang memiliki nilai.
            """
        )

    with st.container(border=True):
        st.markdown(
            """
            Dengan perkembangan teknologi yang ada saat ini, dimungkinkan untuk menganalisis data yang ada dan mendapatkan jawaban dengan segera. Kemampuan untuk bekerja lebih cepat dan tetap tangkas memberi organisasi keunggulan kompetitif yang tidak mereka miliki sebelumnya. Pengambilan keputusan berbasis data telah menjadi salah satu kemampuan paling mendasar yang tidak hanya menghasilkan kinerja pendapatan yang kuat dan pengalaman pelanggan yang unggul tetapi juga mendorong inovasi (Shi‑Nash & Hardoon, 2017). Big data yang dimanfaatkan secara optimal akan membuka peluang analitis yang belum pernah terjadi sebelumnya mengingat tersedianya sumber data baru. Pada era ini, semua data yang terkumpul digunakan untuk meningkatkan bisnis saat ini maupun di masa mendatang. Sebagai akibatnya, baik perusahaan, pemerintah, dan organisasi nirlaba mengalami perubahan perilaku. Pergeseran perilaku ini menciptakan lingkaran yang baik, dimana data disimpan dan dari data tersebut, orang-orang ditugaskan untuk menemukan nilai yang terdapat di dalamnya yang berguna bagi kepentingan perusahaan.
            """
        )

    with st.container(border=True):
        st.markdown(
            """
            Banyak sekali contoh di sekitar kita yang menunjukkan bagaimana big data dikelola dan dimanfaatkan untuk kepentingan bisnis. Setiap pencarian yang dilakukan seseorang di Google akan disimpan oleh Google dan akan dimanfaatkan oleh entitas bisnis lainnya untuk menawarkan produk mereka. Berbagai aplikasi yang ada di smartphone juga memungkinkan untuk menyimpan aktivitas pengguna smartphone terutama aktivitas yang berhubungan dengan jaringan internet. Aktivitas atau jejak digital tersebut dapat meliputi data produk atau layanan yang dicari/dipilih oleh pengguna hingga data lokasi dimana pengguna smartphone tersebut berada. Film dan program acara yang dipilih pengguna pada aplikasi Netflix atau Spotify, e-book yang dibeli melalui amazon.com dan lokasi yang teridentifikasi pada aplikasi berbasis GPS seperti Google Maps dan Waze akan disimpan dan dianalisis untuk dimanfaatkan lebih lanjut oleh para perusahaan pengguna data. Jika proses analisis terhadap big data dilakukan secara optimal, maka akan mendatangkan berbagai manfaat bagi perusahaan antara lain perusahaan akan memiliki metode-metode yang lebih inovatif dalam memanfaatkan data, menjadikan perusahaan memiliki data dengan volume yang tinggi, meningkatkan jumlah data yang dimiliki, meningkatkan pengolahan data yang lebih presisi, memaksimalkan analisis terhadap data, mengurangi Barrier to Entry, dan pengurangan biaya yang selama ini dikeluarkan untuk mendapatkan data terutama data konsumen sebagaimana terlihat pada Gambar VI.1.
            """
        )

    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-6/fig1.png", use_container_width=True)
        st.caption("Gambar VI.1 Manfaat Big Data")

    with st.container(border=True):
        st.markdown(
            """
            Elemen yang penting dalam Big Data terdiri dari data, informasi, dan pengetahuan, antara lain:

            1. **Data**  
            Data adalah hasil observasi langsung terhadap suatu kejadian, yang merupakan perlambangan yang mewakili objek atau konsep dalam dunia nyata. Menurut Ralston dan Reily (Chamidi, 2004: 314), data didefinisikan sebagai fakta atau apa yang dikatakan sebagai hasil dari suatu observasi terhadap fenomena alam.

            2. **Informasi**  
            Dalam hubungannya dengan sistem informasi, informasi dapat kita definisikan sebagai kumpulan data yang terstruktur yang kita komunikasikan melalui bahasa lisan, surat kabar, video dan lain sebagainya yang bermanfaat dalam mengambil keputusan pada saat ini atau masa mendatang.

            3. **Pengetahuan**  
            Pengetahuan adalah sesuatu yang digunakan manusia untuk memahami dunia, yang dapat diubah-ubah berdasarkan informasi yang diterima.

            Hubungan antara ketiga elemen di atas dapat dijelaskan bahwa hasil data dari IoT dan sensor akan menghasilkan data dalam jumlah yang besar atau big data. Data tersebut merupakan hasil observasi langsung terhadap suatu kejadian dan merupakan entitas yang dilengkapi dengan nilai tertentu. Sementara itu, kumpulan data yang terstruktur atau telah diolah akan memperlihatkan hubungan entitas di atas sehingga menghasilkan informasi. Hasil informasi yang telah diproses tersebut akan menghasilkan suatu pemahaman dan pembelajaran serta merefleksikan pengalaman masa lampau akan menjadi suatu pengetahuan. Hasil dari pengetahuan yang diperoleh dapat digunakan untuk membuat suatu keputusan atau kebijakan.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi Big Data", expanded=True):
        st.markdown(
            """
            - Data dengan volume sangat besar, kompleks.
            - Tidak dapat ditangani sistem konvensional.
            - Membutuhkan teknologi analitik inovatif untuk menghasilkan nilai bisnis.
            """
        )

    with st.expander("🧩 5V Karakteristik"):
        st.markdown(
            """
            - **Volume**: ukuran data besar.
            - **Velocity**: kecepatan data dibuat/diproses.
            - **Variety**: keragaman format data.
            - **Veracity**: ketidakpastian kebenaran data.
            - **Value**: nilai yang dapat diekstrak.
            """
        )

    with st.expander("📈 Manfaat Big Data"):
        st.markdown(
            """
            - Metode inovatif dalam pemanfaatan data.
            - Peningkatan presisi pengolahan data.
            - Pengurangan biaya akuisisi data.
            - Keunggulan kompetitif melalui keputusan berbasis data.
            """
        )

    with st.expander("🔁 Elemen Big Data"):
        st.markdown(
            """
            - **Data**: fakta mentah.
            - **Informasi**: data terstruktur yang bermakna.
            - **Pengetahuan**: pemahaman dari informasi.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Jumlah Karakteristik", "5V")
        st.metric("Elemen Utama", "3 (Data, Informasi, Pengetahuan)")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Permana (2016)
            - McKinsey Global (2011)
            - Hurwitz dkk (2013)
            - Kalivas & Overly (2015)
            - Shi‑Nash & Hardoon (2017)
            """
        )