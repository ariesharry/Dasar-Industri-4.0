import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
st.markdown(
    """
    <style>
    /* Target container utama di kolom pertama */
    .stColumn:first-child > div:first-child {
        background-color: #7FA8FF;   /* biru muda */
        border-radius: 20px;
        padding: 20px;
          /* efek bayangan ringan */
    }
    /* Agar container di dalamnya tetap memiliki background putih jika perlu */
    .stColumn:first-child .stContainer {
        background-color: transparent;  /* biar transparan mengikuti induk */
    }
    </style>
    """,
    unsafe_allow_html=True
)

cols = st.columns([0.7, 0.3])

# ================== KOLOM MATERI UTAMA ==================
with cols[0].container(border=True):   # container utama dengan background biru muda
    st.title("Definisi Industri 4.0")
    
    # Bagian 1: Asal Usul
    with st.container(border=True):
        st.markdown(
            """
            **Istilah Industri 4.0** lahir dari ide *revolusi industri keempat* dan mulai 
            dicetuskan pertama kali oleh sekelompok perwakilan tenaga ahli berbagai bidang 
            asal **Jerman**, pada tahun **2011** dalam acara **Hannover Messe**.
            
            Kemudian untuk menindaklanjuti ide tersebut, pada **2015**, Kanselir Jerman 
            **Angela Merkel** mengenalkan gagasan *Revolusi Industri 4.0* di acara 
            **World Economic Forum (WEF)**. Jerman sendiri menggelontorkan modal 
            **ratusan juta Euro** untuk mendukung kalangan akademisi, pemerintah, dan 
            dunia usaha untuk melakukan penelitian lintas akademis mengenai konsep Industri 4.0.
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
                        src="https://www.youtube.com/embed/b9mJrzdlfR8"
                        title="YouTube video"
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen>
                    </iframe>
                </div>
                """,
                unsafe_allow_html=True
            )
    # Dua kolom untuk informasi penting
    col1, col2 = st.columns(2)
    
    with col1.container(border=True):
        st.markdown(
            """
            ### 🎯 Inisiatif Strategis Jerman
            
            **"Industri 4.0"** merupakan inisiatif strategis nasional dari pemerintah Jerman 
            melalui **Kementerian Pendidikan dan Penelitian (BMBF)** dan 
            **Kementerian untuk Urusan Ekonomi dan Energi (BMWi)** yang melibatkan 
            berbagai tenaga ahli baik dari kalangan pemerintah, dunia usaha dan kalangan akademisi.
            
            *(European Commission, Digital Transformation Monitor, 2017)*
            """
        )
    
    with col2.container(border=True):
        st.markdown(
            """
            ### 🎯 Tujuan Utama
            
            Tujuan dari inisiatif Pemerintah Jerman tersebut adalah melakukan 
            **transformasi industri manufaktur** melalui **digitalisasi** dan eksploitasi 
            potensi teknologi baru dalam rangka menghadapi tantangan global yang semakin 
            ketat dan memenuhi kebutuhan untuk adaptasi produksi yang cepat terhadap 
            permintaan pasar yang selalu berubah.
            
            *(Andreja Rojko, 2017)*
            """
        )
    
    # Bagian 2: Istilah Lain di Berbagai Negara
    with st.container(border=True):
        st.markdown(
            """
            ### 🌍 Istilah Lain di Berbagai Negara
            
            Beberapa negara lain juga turut serta dalam mewujudkan konsep industri 4.0 
            namun menggunakan istilah yang berbeda seperti:
            
            - **Smart Factories**
            - **Industrial Internet of Things**
            - **Smart Industry** 
            - **Advanced Manufacturing**
            
            Meski memiliki penyebutan istilah yang berbeda, semuanya memiliki 
            **tujuan yang sama** yaitu untuk meningkatkan daya saing industri 
            tiap negara dalam menghadapi pasar global yang dinamis.
            
            *(Hoedi Prasetyo dkk, 2018)*
            """
        )
    
    # Bagian 3: Ragam Definisi
    with st.container(border=True):
        st.markdown(
            """
            ### 🔍 Ragam Definisi
            
            Perlu diketahui bahwa definisi mengenai industri 4.0 saat ini mengalami 
            **keanekaragaman**, hal ini disebabkan konsepnya masih dalam tahap 
            penelitian dan pengembangan. **Sung Ing Tay dkk (2018)** telah melakukan 
            kompilasi dari berbagai sumber mengenai definisi industri 4.0 sebagaimana 
            tabel berikut:
            """
        )
    
    # Tabel Definisi
    st.subheader("📊 Tabel I.1 Definisi (Pengertian) Industri 4.0")
    
    # Data untuk tabel
    data = {
        "Penulis": [
            "Kagermann, Wahlster & Johannes (2013)",
            "Qin, Liu & Grosvenor (2016)",
            "Schumacher, Erol & Sihn (2016)",
            "Schwab (2016)",
            "Wang dkk (2016)",
            "Mrugalska & Magdalena (2017)"
        ],
        "Definisi (Pengertian)": [
            "Industri 4.0 memanfaatkan kekuatan teknologi informasi & komunikasi dan penemuan inovatif untuk mendorong pengembangan industri manufaktur.",
            "Industri 4.0 mendorong terjadinya peningkatan efisiensi produksi dengan mengumpulkan data secara cerdas, yang dapat menghasilkan keputusan yang benar dan tanpa keraguan dengan bantuan kecerdasan buatan.",
            "Industri 4.0 dikelilingi oleh jaringan teknologi canggih di sepanjang rantai nilai. Layanan berorientasi pelanggan, otomasi, robotika, kecerdasan buatan, Internet of Thing (IOT) dan manufaktur aditif membawa era baru dalam proses manufaktur.",
            "Industri 4.0 mengintegrasikan beberapa karakteristik teknologi baru, misalnya: dunia fisik, digital, dan biologis. Peningkatan penggunaan teknologi era industri 4.0 memberikan dampak signifikan terhadap industri, ekonomi dan rencana pembangunan pemerintah.",
            "Industri 4.0 memanfaatkan sepenuhnya emerging technologies dan pengembangan mesin/peralatan yang mempunyai respon cepat untuk mengatasi tantangan global dalam rangka meningkatkan daya saing industri.",
            "Pada industri 4.0, mesin/peralatan modern dan canggih yang didukung oleh perangkat lunak canggih dan jaringan sensor dapat digunakan untuk merencanakan, memprediksi, menyesuaikan, dan mengendalikan produksi dan pembentukan model bisnis baru sepanjang rantai nilai dan siklus kehidupan produk."
        ]
    }
    
    # Tampilkan tabel
    df = pd.DataFrame(data)
    st.table(df)
    st.caption("Sumber: Sung Ing Tay dkk, 2018")
    
    # Bagian 4: Teknologi Enabler
    with st.container(border=True):
        st.markdown(
            """
            ### 📈 Teknologi Enabler Industri 4.0
            
            Berdasarkan tabel diatas hampir semua penulis menyatakan bahwa pengertian 
            **industri 4.0** adalah terkait dengan topik: **Cyber-Physical System (CPS)**, 
            **Internet of Thing (IoT)**, **industrial Internet**, dan sebagainya. 
            Teknologi "enabler" lainnya meliputi antara lain:
            
            - **Big Data Analytics**
            - **Augmented Reality**
            - **Additive Manufacturing**
            - **Simulation**
            - **Horizontal & Vertical System Integration**
            - **Autonomous Robot**
            - **Cloud Computing**
            """
        )
    
    # Bagian 5: Definisi Platform dan Proses Produksi Cerdas
    col3, col4 = st.columns(2)
    
    with col3.container(border=True):
        st.markdown(
            """
            ### 🌐 Definisi Platform Industri 4.0
            
            Secara singkat dari sumber platform industri 4.0 (www.plattform-i40.de) 
            dapat dikatakan bahwa **industri 4.0** adalah industri yang mengacu pada 
            kombinasi antara **jaringan mesin dan proses yang cerdas** dengan 
            **teknologi informasi dan komunikasi**.
            """
        )
    
    with col4.container(border=True):
        st.markdown(
            """
            ### 🏭 Proses Produksi Cerdas
            
            Beberapa kemungkinan proses produksi cerdas meliputi antara lain:
            
            - Produksi fleksibel (flexible production)
            - Pabrik konversibel (convertible factory)
            - Solusi berorientasi pelanggan
            - Logistik teroptimasi
            - Penggunaan data
            - Ekonomi sirkular efisien
            """
        )
    
    # Bagian 6: Definisi Komprehensif
    with st.container(border=True):
        st.markdown(
            """
            ### 🎯 Definisi Komprehensif Industri 4.0
            
            Berdasarkan berbagai kajian definisi industri 4.0, maka **industri 4.0** 
            dapat didefinisikan sebagai berikut yaitu: suatu industri yang cerdas 
            dengan memanfaatkan hasil konvergensi **teknologi informasi dan teknologi 
            operasional** untuk mendapatkan data **"real time"**, melakukan integrasi 
            secara vertikal dan horizontal dari keseluruhan aspek produksi meliputi 
            sepanjang daur kehidupan produk dan rantai nilai, memanfaatkan jaringan 
            **"internet of thing (IoT) dan internet of services (IOS)"**, serta 
            **komputasi awan dan "big data analytics"** dalam rangka meningkatkan 
            **efisiensi, produktivitas dan daya saing**.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")
    
    with st.expander("📅 Asal-usul Konsep", expanded=True):
        st.markdown(
            """
            - **2011**: Dicetuskan di Hannover Messe, Jerman
            - **2015**: Diperkenalkan di World Economic Forum
            - **Inisiatif strategis nasional** Jerman
            - Didanai **ratusan juta Euro**
            """
        )
    
    with st.expander("🎯 Tujuan Utama"):
        st.markdown(
            """
            - Transformasi industri manufaktur
            - Digitalisasi proses produksi
            - Adaptasi cepat terhadap pasar
            - Integrasi rantai nilai
            """
        )
    
    with st.expander("🌍 Istilah Global"):
        st.markdown(
            """
            - Smart Factories
            - Industrial Internet of Things
            - Smart Industry
            - Advanced Manufacturing
            - Tujuan sama: **daya saing global**
            """
        )
    
    with st.expander("🔧 Teknologi Kunci"):
        st.markdown(
            """
            - Cyber-Physical Systems (CPS)
            - Internet of Things (IoT)
            - Big Data Analytics
            - Cloud Computing
            - Artificial Intelligence
            """
        )
    
    with st.expander("📊 Karakteristik Utama"):
        st.markdown(
            """
            - Data real-time
            - Integrasi vertikal & horizontal
            - Jaringan IoT dan IoS
            - Produksi fleksibel
            - Efisiensi dan produktivitas tinggi
            """
        )
    
    # Statistik singkat
    with st.container(border=True):
        st.markdown("### 📈 Fakta Singkat")
        st.metric("Tahun Peluncuran", "2011")
        st.metric("Negara Pelopor", "Jerman")
        st.metric("Jumlah Definisi", "6+ versi")
    
    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - European Commission (2017)
            - Andreja Rojko (2017)
            - Hoedi Prasetyo dkk (2018)
            - Sung Ing Tay dkk (2018)
            - Berbagai ahli 2013-2017
            """
        )