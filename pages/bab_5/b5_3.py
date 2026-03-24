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
    st.title("Cloud Computing Deployment Model")

    # Pengantar
    with st.container(border=True):
        st.markdown(
            """
            Cloud Computing Deployment Model dapat dilihat pada gambar berikut:
            """
        )

    # Gambar
    with st.container(border=True):
        st.markdown("### 🖼️ Jenis-jenis Komputasi Awan")

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-5/fig3.png", use_container_width=True)

        st.caption("Gambar V.3 – Jenis-jenis komputasi awan (Sumber: blog.bookmyidentity.com)")

    # Public Cloud
    with st.container(border=True):
        st.markdown(
            """
            **1. Public Cloud** merupakan model komputasi awan di mana penyedia pihak ketiga membuat sumber daya 
            komputasi tersedia untuk masyarakat umum melalui internet. Dengan cloud publik, perusahaan tidak perlu 
            mengatur dan mengelola sendiri server cloud mereka sendiri.

            Karakteristik Public Cloud : Multi-tenant architecture; pay-as-you-go pricing model

            Vendor utama antara lain: AWS, Microsoft Azure, Goggle Cloud Platform
            """
        )

    # Private Cloud
    with st.container(border=True):
        st.markdown(
            """
            **2. Private Cloud** merupakan model komputasi awan di mana perusahaan menggunakan arsitektur 
            berpemilik (proprietary) dan menjalankan server cloud dalam pusat datanya sendiri.

            Karakteristik Private Cloud: Single-tenant architecture; on premise hardware; kontrol langsung 
            infrastruktur cloud yang mendasarinya.

            Vendor Utama: HPE, VMwave, Dell EMC, IBM, Red Hat, Microsoft, OpenStack.
            """
        )

    # Hybrid Cloud
    with st.container(border=True):
        st.markdown(
            """
            **3. Hybrid Cloud** merupakan model komputasi awan yang mencakup perpaduan layanan public cloud, 
            private cloud, dan pihak ketiga dengan orkestrasi antara kedua platform.

            Karakteristik Hybrid Cloud: kemampuan cloud bursting; banyak manfaat pada lingkungan publik dan privat.

            Vendor Utama : Kombinasi dari penyedia public cloud dan private cloud.
            """
        )

    # Penjelasan deployment
    with st.container(border=True):
        st.markdown(
            """
            Penerapan cloud (cloud deployment) menjelaskan cara platform cloud diimplementasikan, bagaimana hostnya, 
            dan siapa yang memiliki akses ke sana. Semua penerapan komputasi awan beroperasi dengan prinsip yang sama 
            dengan memvirtualisasikan daya komputasi server ke dalam aplikasi tersegmentasi dan berbasis perangkat 
            lunak yang menyediakan kemampuan pemrosesan dan penyimpanan.
            """
        )

    # Manfaat cloud
    with st.container(border=True):
        st.markdown(
            """
            Cloud computing menawarkan banyak peluang bagi Lanner untuk meningkatkan kinerja, jangkauan, dan penggunaan 
            teknologi kami. Secara tradisional, sebuah teknologi terbatas pada pemodel dan analis, kembar digital prediktif, 
            dan kemampuan simulasi mereka sekarang dapat secara langsung berada di tangan mereka yang membuat keputusan 
            bisnis, di mana mereka dapat memperoleh akses ke wawasan melalui perangkat apa pun kapan saja. 

            Ini berarti bahwa simulasi prediksi sekarang digunakan untuk perencanaan dan penjadwalan sumber daya operasional 
            selain perencanaan bisnis strategis, investasi dan keputusan kebijakan.
            """
        )

    # Industri 4.0
    with st.container(border=True):
        st.markdown(
            """
            Cloud adalah dasar untuk semua solusi dan penawaran inovatif di industri 4.0. Membangun di atas teknologi cloud, 
            kami mengembangkan dan menawarkan produk-produk standar seperti solusi ujung ke ujung kami untuk pemantauan 
            mesin industri, pelacakan aset atau pemantauan pengiriman.
            """
        )

    # Daftar pustaka
    with st.container(border=True):
        st.markdown("### 📚 Daftar Pustaka")
        st.markdown(
            """
            1. https://www.datamation.com/cloud-computing/what-is-cloud-computing.html  
            2. http://blog.bookmyidentity.com/cloud-hosting/what-is-cloud-computing-2/  
            3. https://www.bmc.com/blogs/saas-vs-paas-vs-iaas-whats-the-difference-and-how-to-choose/  
            """
        )

# ================== KOLOM SAMPING ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("☁️ Deployment Model", expanded=True):
        st.markdown(
            """
            - Public Cloud
            - Private Cloud
            - Hybrid Cloud
            """
        )

    with st.expander("⚙️ Karakteristik"):
        st.markdown(
            """
            - Public: multi-tenant, pay-as-you-go  
            - Private: kontrol penuh, single-tenant  
            - Hybrid: kombinasi keduanya  
            """
        )

    with st.expander("🏢 Vendor"):
        st.markdown(
            """
            - AWS, Azure, Google Cloud  
            - IBM, Dell EMC, Red Hat  
            """
        )

    with st.container(border=True):
        st.markdown("### 📊 Fakta")
        st.metric("Model Fleksibel", "Hybrid Cloud")
        st.metric("Akses", "Any device, anytime")