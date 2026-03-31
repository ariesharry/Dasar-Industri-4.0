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
        <h1 style='text-align: center;'>📘 BAB 8</h1>
        """,
        unsafe_allow_html=True
    )

    # Container isi
    with st.container(border=True):
        st.markdown(
            """
            ### 🎯 Capaian Pembelajaran
            
            Mahasiswa mampu memahami pengetahuan tentang **Kecerdasan Buatan (AI)**, meliputi:
            
            1. **Artificial Intelligence vs Machine Learning vs Deep Learning**  
            
            2. **Aplikasi AI yang potensial pada industri**  
            
            3. **Sejarah dan definisi Kecerdasan Buatan (Artificial Intelligence)**  
            """
        )
        
    st.title("Sejarah dan Definisi Kecerdasan Buatan (Artificial Intelligence)")

    with st.container(border=True):
        st.markdown(
            """
            Istilah kecerdasan buatan atau artificial intelligence (AI) mulai dikenal pada 1956 (www.sas.com) yang dirintis oleh John McCarthy, seorang profesor dari Massachusetts Institute of Technology. Pada saat ini, AI semakin populer menjadi alat yang berharga dan penting untuk mengatur teknologi digital dan mengelola operasi bisnis karena adanya peningkatan volume data, algoritma canggih, dan peningkatan daya serta penyimpanan komputasi. Salah satu contoh dari AI adalah kemampuan ponsel cerdas (smartphone) dalam mempelajari dan menafsirkan cara bicara pemiliknya. Berbicara dengan smartphone untuk mengetahui hal-hal seperti lokasi restoran terbaik yang ada di suatu kota atau untuk menemukan cara menuju suatu lokasi.
            """
        )

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-8/fig1.png", use_container_width=True)
        st.caption("Gambar VIII.1 Evolusi Artificial Intellegence (Sumber: sas.com)")

        st.markdown(
            """
            Perkembangan AI yang dimulai pada tahun 1950-an sampai dengan 1970-an, riset awal mengenai AI dilakukan dengan suatu pekerjaan menggunakan jaringan neural. Tahun 1980-an sampai dengan tahun 2010-an, AI populer dengan adanya pembelajaran mesin. Pada saat ini, AI berevolusi memberikan manfaat bagi suatu industri dengan menanamkan teknologi tersebut seperti pembelajaran mesin dan pembelajaran mendalam (deep learning) seperti yang terlihat pada Gambar VIII.1.

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
                            src="https://www.youtube.com/embed/c0m6yaGlZh4"
                            title="YouTube video"
                            frameborder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen>
                        </iframe>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.markdown(
            """

            Kecerdasan buatan (AI) berakar dari ilmu matematika dan statistik, dengan bantuan komputer menggunakan pembelajaran lebih dalam serta pemrosesan bahasa alamiah yang dilatih digunakan untuk menyelesaikan tugas-tugas tertentu dengan memproses sejumlah besar data dan mengenali pola dalam data. Dengan demikian, memungkinkan mesin untuk belajar dari pengalaman, menyesuaikan input-input baru dan melaksanakan tugas seperti manusia. Istilah kecerdasan buatan (AI) mengacu pada sistem komputasi yang melakukan tugas-tugas yang biasanya dipertimbangkan dalam bidang pengambilan keputusan manusia. Sistem yang digerakkan oleh perangkat lunak dan agen cerdas ini menggabungkan analitik data canggih dan aplikasi big data. Sistem AI memanfaatkan repositori pengetahuan untuk membuat keputusan dan mengambil tindakan yang mendekati fungsi kognitif, termasuk pembelajaran dan pemecahan masalah. Beberapa definisi mengenai kecerdasan buatan (AI) dikelompokkan menjadi empat kategori, yaitu berpikir secara manusiawi, berpikir secara rasional, bertindak manusiawi, dan bertindak rasional (Russell & Norvig, 2016). Namun, menurut Russell, & Norvig (dalam De Spiegeleire, S., dkk, 2017) menjelaskan bahwa secara konkret dan dalam sebagian besar aplikasi, AI didefinisikan sebagai kecerdasan non-manusia yang diukur dengan kemampuannya untuk meniru keterampilan mental manusia, seperti pengenalan pola, memahami bahasa alami, belajar adaptif dari pengalaman, menyusun strategi, atau alasan lainnya.
            """
        )


# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Sejarah AI", expanded=True):
        st.markdown(
            """
            - Istilah AI mulai dikenal pada 1956.
            - Dirintis oleh John McCarthy (MIT).
            - Perkembangan: neural network (1950-70), machine learning (1980-2010), deep learning (sekarang).
            """
        )

    with st.expander("📌 Definisi AI"):
        st.markdown(
            """
            - AI adalah sistem komputasi yang melakukan tugas seperti pengambilan keputusan manusia.
            - Menggabungkan analitik data canggih dan big data.
            - Empat kategori: berpikir manusiawi, berpikir rasional, bertindak manusiawi, bertindak rasional.
            - Kecerdasan non-manusia yang meniru keterampilan mental manusia.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Tahun AI mulai dikenal", "1956")
        st.metric("Pencetus", "John McCarthy")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - www.sas.com
            - Russell & Norvig (2016)
            - De Spiegeleire, S., dkk (2017)
            """
        )