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
    st.title("Manfaat Industri 4.0")

    # Pengantar
    with st.container(border=True):
        st.markdown(
            """
            Tujuan penting dari Industri 4.0 adalah untuk membuat industri manufaktur - dan industri 
            terkaitnya seperti logistik - menjadi **lebih cepat, lebih efisien, dan lebih berpusat pada 
            pelanggan**. Pada saat yang sama, Industri 4.0 juga dapat melampaui kinerja otomatisasi dan 
            optimisasi seperti pada revolusi industri sebelumnya, serta mendeteksi peluang munculnya 
            **model bisnis baru**.

            Ada **enam kategori utama potensi manfaat** Industri 4.0:
            """
        )

    # Enam manfaat dalam dua kolom (kiri-kanan)
    col_left, col_right = st.columns(2)

    with col_left:
        with st.container(border=True):
            st.markdown("### ⚡ 1. Efisiensi")
            st.markdown(
                """
                Dengan meningkatnya otomatisasi (robot, alat bantu) serta simulasi/optimisasi 
                berbasis kecerdasan buatan, perusahaan dapat membuat keputusan **real-time** 
                lebih cepat, menjaga efisiensi, dan mencapai kualitas lebih tinggi.
                """
            )

        with st.container(border=True):
            st.markdown("### 💡 3. Inovasi")
            st.markdown(
                """
                Lini produksi dirancang untuk mengakomodasi campuran material tinggi (*high-mix*) 
                dan volume rendah, memungkinkan inovasi produk baru dan eksperimen desain lebih cepat. 
                IIoT menciptakan produk dan mesin lebih cerdas, sehingga pemahaman desain dan proses 
                semakin mendalam.
                """
            )

        with st.container(border=True):
            st.markdown("### 💰 5. Biaya")
            st.markdown(
                """
                Meski investasi awal diperlukan, setelah pabrik menjadi cerdas, biaya turun drastis. 
                Masalah kualitas berkurang karena limbah produksi menurun, kebutuhan tenaga kerja 
                berkualifikasi rendah berkurang, dan biaya operasi menurun.
                """
            )

    with col_right:
        with st.container(border=True):
            st.markdown("### 🏃 2. Lincah (Agility)")
            st.markdown(
                """
                Untuk merespon permintaan campuran material tinggi, lot kecil, dan manufaktur satu kali, 
                Industri 4.0 meningkatkan kelincahan. Sensor dan kecerdasan buatan mendeteksi kondisi 
                mesin/produk secara cepat, sehingga pengambilan keputusan berlangsung cepat dan mandiri.
                """
            )

        with st.container(border=True):
            st.markdown("### 😊 4. Pengalaman Pelanggan")
            st.markdown(
                """
                Data rinci dan responsif memungkinkan produsen memberikan layanan dengan fitur lebih baik. 
                *Self-service* pelanggan dapat diintegrasikan ke proses produksi. Data MES membantu 
                menyelesaikan masalah antara pelanggan dan produsen dengan cepat.
                """
            )

        with st.container(border=True):
            st.markdown("### 📈 6. Pendapatan")
            st.markdown(
                """
                Kualitas lebih baik, biaya rendah, campuran tinggi, dan layanan unggul menjadikan produsen 
                sebagai pemasok pilihan. Industri 4.0 membuka pasar lebih besar, menawarkan kustomisasi 
                produk dengan margin tinggi, serta produk dan operasi yang lebih cerdas.
                """
            )

    # Dampak positif dan tantangan
    with st.container(border=True):
        st.markdown(
            """
            ### 🌍 Dampak Positif dan Tantangan

            Terwujudnya potensi manfaat tersebut pada gilirannya memberi dampak positif terhadap 
            perekonomian suatu negara, antara lain peningkatan **daya saing nasional** dan 
            **Produk Domestik Bruto (PDB)**.

            Namun, Industri 4.0 juga memiliki tantangan yang harus dihadapi, seperti:
            - Resistansi terhadap perubahan
            - Kesenjangan teknologi antara kondisi saat ini dengan kondisi yang diharapkan
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("⚡ 1. Efisiensi", expanded=True):
        st.markdown(
            """
            - Otomatisasi dan AI mempercepat keputusan real-time  
            - Kualitas tinggi dan efisiensi terjaga
            """
        )
    with st.expander("🏃 2. Lincah (Agility)"):
        st.markdown(
            """
            - Respon cepat terhadap high-mix, low-volume  
            - Sensor dan AI memungkinkan keputusan mandiri
            """
        )
    with st.expander("💡 3. Inovasi"):
        st.markdown(
            """
            - Lini produksi adaptif untuk high-mix  
            - Eksperimen desain lebih cepat  
            - IIoT meningkatkan pemahaman produk dan proses
            """
        )
    with st.expander("😊 4. Pengalaman Pelanggan"):
        st.markdown(
            """
            - Layanan lebih baik dengan data rinci  
            - Self-service pelanggan terintegrasi  
            - Resolusi masalah cepat berbasis data MES
            """
        )
    with st.expander("💰 5. Biaya"):
        st.markdown(
            """
            - Investasi awal, namun biaya turun drastis  
            - Limbah berkurang, tenaga kerja rendah berkurang  
            - Biaya operasi menurun
            """
        )
    with st.expander("📈 6. Pendapatan"):
        st.markdown(
            """
            - Kualitas dan layanan unggul meningkatkan daya saing  
            - Pasar lebih besar, kustomisasi margin tinggi  
            - Operasi cerdas membuka peluang baru
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📈 Fakta Singkat")
        st.metric("Kategori Manfaat", "6")
        st.metric("Dampak Makro", "Daya Saing & PDB")
        st.metric("Tantangan Utama", "Resistansi & Kesenjangan Teknologi")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Mabkhot dkk (2018)  
            - Hermann dkk (2015)  
            - Publikasi Industri 4.0 terkait
            """
        )