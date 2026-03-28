import streamlit as st

st.set_page_config(layout="wide")

# ========== CSS ==========
st.markdown(
    """
    <style>
    .stColumn:first-child > div:first-child {
        background-color: #caf0f8;
        border-radius: 20px;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

cols = st.columns([0.7, 0.3])

# ================== KOLOM UTAMA ==================
with cols[0].container(border=True):
    st.title("Layanan Komputasi Awan")

    # Definisi layanan
    with st.container(border=True):
        st.markdown(
            """
            Layanan komputasi awan secara luas dibagi menjadi tiga kategori: 
            Infrastruktur sebagai Layanan (Infrastructure as a Service - IaaS), 
            platform sebagai layanan (Platform as Service - PaaS) dan perangkat 
            lunak sebagai layanan (Software as a Service - SaaS).
            """
        )

    # Penjelasan istilah
    with st.container(border=True):
        st.markdown(
            """
            **On premise (di tempat)** : perangkat lunak yang diinstal di gedung yang sama dengan bisnis Anda  

            **IaaS** : layanan berbasis cloud, pay-as-you-go untuk layanan seperti penyimpanan, jaringan, server, dan virtualisasi.  

            **PaaS** : perangkat keras dan perangkat lunak yang tersedia melalui internet  

            **SaaS** : perangkat lunak yang tersedia melalui pihak ketiga melalui internet
            """
        )

    # Gambar
    with st.container(border=True):
        st.markdown("### 🖼️ Perbandingan Layanan Cloud dan On-Premise")

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-5/fig2.png", use_container_width=True)

        st.caption("Gambar V.2 – Perbedaan Layanan Komputasi Awan dengan On-premise (Sumber: bmc.com)")

    # Kelebihan cloud
    with st.container(border=True):
        st.markdown(
            """
            Penggunaan cloud menawarkan kelebihan. Pertama, dari segi biaya. Jika memilih menggunakan pusat data on premise 
            perusahaan akan memerlukan investasi besar di awal untuk penyediaan hardware, software, network, ruang server, 
            pendingin yang cukup, dan listrik yang stabil. Menggunakan cloud, biaya besar di awal bisa dipangkas. Semua 
            infrastruktur fisik sudah disediakan oleh vendor penyedia layanan cloud. Begitu juga dengan pemeliharaannya. 

            Kelebihan kedua adalah skalabilitas yang tidak terbatas. Perusahaan dapat melakukan penambahan atau pengurangan 
            kapasitas dan spesifikasi server-nya sesuai kebutuhan.
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
                        src="https://www.youtube.com/embed/mxT233EdY5c"
                        title="YouTube video"
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen>
                    </iframe>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Kekurangan cloud
    with st.container(border=True):
        st.markdown(
            """
            Kekurangannya, perusahaan yang menggunakan cloud akan sangat bergantung pada kualitas koneksi internet. 
            Saat ini belum semua area di Indonesia terkoneksi dengan jaringan internet yang memadai. Hal ini bisa menjadi 
            pertimbangan perusahaan karena tanpa koneksi internet memadai akses ke server, aplikasi, atau data-data yang 
            tersimpan dalam cloud akan sulit. 

            Kontrol terhadap data yang disimpan juga sangat bergantung pada provider. Kerja sama antara perusahaan sebagai 
            user dan provider cloud terbatas pada service level agreement, misalnya dalam hal maintenance. Selain itu, ada 
            juga risiko downtime. Provider cloud mengurusi banyak klien setiap harinya. Sewaktu-waktu bukan tidak mungkin 
            provider mengalami masalah teknis yang menyebabkan akses ke layanan cloud terhambat. Bisnis perusahaan bisa 
            jadi ikut terhambat oleh karena hal ini. Ketika hal ini terjadi perusahaan tidak bisa berbuat banyak selain 
            menunggu perbaikan dari provider. 

            Menggunakan cloud biaya di awal akan lebih sedikit, tetapi perlu diingat bahwa kustomisasi kapasitas dan 
            spesifikasi server pada cloud juga memerlukan biaya. Begitu juga soal isu keamanan data. Biaya untuk memastikan 
            keamanan data ini sangat besar.
            """
        )

    # On-premise
    with st.container(border=True):
        st.markdown(
            """
            Sedangkan pusat data on premise, menawarkan otoritas lebih dalam hal penyimpanan data kepada perusahaan. 
            Data dan aplikasi dilindungi firewall dan hanya dapat diakses oleh perusahaan. Perusahaan dapat membuat 
            private cloud untuk menyimpan data yang bersifat sensitif dan rahasia, sementara data-data yang tidak bersifat 
            sensitif dapat dipindahkan ke public cloud. 

            Kustomisasi server dapat dilakukan hingga benar-benar sesuai dengan kebutuhan bisnis. Kekurangannya, pusat 
            data on premise memerlukan investasi besar serta tenaga IT untuk mengoperasikan dan memelihara pusat data baik 
            hardware maupun software-nya. Biaya investasi tersebut memang hanya besar di awal, sementara biaya operasional 
            ke depannya bisa dikatakan akan lebih minim dibandingkan dengan menggunakan layanan cloud. 

            Namun, ada satu hal yang tidak bisa diperoleh dari pusat data on premise yaitu kepraktisan dan fleksibilitas 
            dalam hal meningkatkan skalabilitas.
            """
        )

    # Kombinasi layanan
    with st.container(border=True):
        st.markdown(
            """
            Sebagian besar bisnis menggunakan kombinasi model layanan cloud computing SaaS dan IaaS, dan banyak pengembang 
            yang terlibat untuk membuat aplikasi menggunakan PaaS juga.
            """
        )

    # Contoh SaaS
    with st.container(border=True):
        st.markdown(
            """
            ### 📦 Contoh Layanan SaaS
            BigCommerce, Google Apps, Salesforce, Dropbox, MailChimp, ZenDesk, DocuSign, Slack, Hubspot
            """
        )

    # Contoh PaaS
    with st.container(border=True):
        st.markdown(
            """
            ### 📦 Contoh Layanan PaaS
            AWS Elastic Beanstalk, Heroku, Windows Azure (kebanyakan digunakan sebagai PaaS), 
            Force.com, OpenShift, Apache Stratos, Magento Commerce Cloud
            """
        )

    # Contoh IaaS
    with st.container(border=True):
        st.markdown(
            """
            ### 📦 Contoh Layanan IaaS
            AWS EC2, Rackspace, Google Compute Engine (GCE), Digital Ocean, Magento 1 Edisi Enterprise
            """
        )

    # Penutup
    with st.container(border=True):
        st.markdown(
            """
            Meningkatnya popularitas penggunaan layanan komputasi awan IaaS, PaaS, dan SaaS mengurangi kebutuhan untuk 
            hosting di tempat (on premise). Masing-masing model server komputasi awan tersebut memberikan pilihan, 
            fleksibilitas, dan opsi kepada pengguna yang tidak dapat disediakan oleh hosting lokal (on premise). 
            Beberapa model server komputasi awan lebih rumit daripada yang lain.

            Tingkat pengetahuan administrasi sistem berkurang mengikuti urutan layanan komputasi awan berikut ini:  
            **On-premise > IaaS > PaaS > SaaS**
            """
        )

# ================== SIDEBAR / KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("☁️ Model Layanan", expanded=True):
        st.markdown(
            """
            - IaaS
            - PaaS
            - SaaS
            """
        )

    with st.expander("✅ Kelebihan Cloud"):
        st.markdown(
            """
            - Biaya awal lebih kecil
            - Infrastruktur disediakan vendor
            - Skalabilitas tinggi
            """
        )

    with st.expander("⚠️ Kekurangan"):
        st.markdown(
            """
            - Bergantung internet
            - Risiko downtime
            - Kontrol data terbatas
            """
        )

    with st.expander("🏢 On-Premise"):
        st.markdown(
            """
            - Kontrol penuh data
            - Aman (firewall internal)
            - Tapi biaya awal besar
            """
        )

    with st.container(border=True):
        st.markdown("### 📊 Fakta")
        st.metric("Model Populer", "SaaS + IaaS")
        st.metric("Urutan Kompleksitas", "On-premise → SaaS")