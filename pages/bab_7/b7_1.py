import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
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

# ================== KOLOM MATERI UTAMA ==================
with cols[0].container(border=True):

    st.markdown(
        """
        <h1 style='text-align: center;'>📘 BAB 7</h1>
        """,
        unsafe_allow_html=True
    )

    # Container isi
    with st.container(border=True):
        st.markdown(
            """
            ### 🎯 Capaian Pembelajaran
            
            Mahasiswa mampu memahami pengetahuan tentang **simulasi**, meliputi:
            
            1. **Pengertian simulasi**  
            
            2. **Jenis-jenis simulasi**  
            
            3. **Simulasi dalam Industri 4.0**  
            
            4. **Digital Twin**  
            """
        )
        
    st.title("Pengertian dan Tujuan Simulasi")

    with st.container(border=True):
        st.markdown(
            """
            Simulasi (simulation) merupakan sekumpulan metode dan aplikasi yang digunakan untuk meniru perilaku dari suatu sistem nyata. Simulasi dilakukan saat hubungan variabel yang ada pada suatu sistem sangat rumit. Simulasi pada umumnya dilakukan menggunakan bantuan komputer atau software tertentu (Kelton dkk, 2010). Simulasi merupakan salah satu metode di bidang operations research dan management science yang paling sering digunakan dalam menganalisis suatu sistem. Umumnya hasil dari analisis akan digunakan sebagai pertimbangan untuk pengambilan keputusan yang bersifat strategis untuk meningkatkan kinerja sistem, misalkan dari sisi kapasitas, produktivitas, efisiensi, dan variabel keputusan sistem lainnya. Untuk dapat mencapai hal ini maka perlu dibangun dulu suatu model yang merepresentasikan sistem nyata, kemudian dilakukan verifikasi dan validasi terhadap model tersebut. Apabila model sudah dipastikan valid, maka selanjutnya dapat dilakukan eksperimen pada model simulasi tersebut dengan melakukan perubahan pada parameter sistem untuk melihat pengaruhnya terhadap variabel keputusan yang diamati. Logika dari metodologi simulasi ini ditampilkan pada Gambar VII.1:
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
                            src="https://www.youtube.com/embed/7QU769TkTfE"
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
            st.markdown("### 🖼️ Ilustrasi Arsitektur Komputasi Awan")

            col1, col2, col3 = st.columns([1, 2, 1])

            with col2:
                st.image("assets/bab-7/fig1.png", use_container_width=True)
        st.caption("Gambar VII.1 Metodologi Simulasi (Sumber: diadaptasi dari Gallien, 2003)")

        st.markdown(
            """
            Terdapat beragam kelebihan yang dapat dijadikan alasan digunakannya metode simulasi dalam suatu analisis sistem. Siswanto dkk (2017) menerangkan beberapa alasan tersebut antara lain:

            • Simulasi mampu memodelkan keterkaitan dan ketergantungan antar elemen pada suatu sistem yang tidak mampu diperoleh dari metode analitis
            • Simulasi bersifat fleksibel untuk berbagai jenis model sistem walaupun belum tentu merupakan pendekatan yang efektif
            • Output simulasi dapat menunjukkan perilaku sistem dari waktu ke waktu
            • Menawarkan penghematan waktu dan biaya, terutama untuk permasalahan skala besar
            • Tidak merusak atau mengganggu sistem yang sebenarnya
            • Menyediakan informasi untuk beberapa ukuran performansi sekaligus
            • Hasil dari simulasi mudah untuk dimengerti dan dikomunikasikan sehingga orang yang tidak memahami teorinya pun dapat memahami dengan baik
            • Menekankan pada detail sistem

            Law (2015) menyebutkan sejumlah proses dan sistem nyata dimana simulasi dapat menjadi alat analisis yang sangat berguna, diantaranya:

            • Desain dan analisis dari suatu sistem manufaktur seperti pabrik otomotif, garmen/tekstil, kimia, dan lain-lain;
            • Desain dan analisis dari suatu sistem transportasi seperti bandara, pelabuhan, stasiun kereta, dan lain-lain;
            • Evaluasi desain dari organisasi jasa seperti call centers, restoran cepat saji, rumah sakit, kantor pos, dan lain-lain;
            • Rekayasa ulang proses bisnis perusahaan;
            • Analisis rantai pasokan;
            • Penentuan kebijakan pemesanan dari sistem persediaan; dan
            • Analisis operasi pertambangan
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Pengertian Simulasi", expanded=True):
        st.markdown(
            """
            - Metode meniru perilaku sistem nyata.
            - Digunakan saat hubungan variabel rumit.
            - Membantu pengambilan keputusan strategis.
            """
        )

    with st.expander("⚙️ Kelebihan Simulasi"):
        st.markdown(
            """
            - Memodelkan ketergantungan antar elemen.
            - Fleksibel, hemat waktu & biaya.
            - Tidak mengganggu sistem nyata.
            - Mudah dikomunikasikan.
            """
        )

    with st.expander("🏭 Contoh Penerapan"):
        st.markdown(
            """
            - Manufaktur, transportasi, layanan jasa.
            - Rekayasa ulang bisnis, rantai pasok.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Tujuan Utama", "Pengambilan keputusan strategis")
        st.metric("Sumber", "Kelton dkk (2010), Law (2015), Siswanto dkk (2017)")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Kelton, W.D., Sadowski, R.P., Swets, N.B. (2010)
            - Law, Averill M. (2015)
            - Siswanto, Nurhadi., Latiffianti, Effi., Wiratno, S.E. (2017)
            """
        )