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
    st.title("Making Indonesia 4.0")

    # Pengantar: Inisiatif Making Indonesia 4.0
    with st.container(border=True):
        st.markdown(
            """
            Pada bulan April 2018, saat diselenggarakan **Indonesia Industrial Summit (IIS) 2018**, 
            Kementerian Perindustrian menyusun inisiatif **"Making Indonesia 4.0"** untuk 
            mengimplementasikan strategi dan Peta Jalan Revolusi Industri 4.0 di Indonesia.

            Penyusunan Peta Jalan ini melibatkan berbagai pemangku kepentingan: institusi pemerintah, 
            asosiasi industri, pelaku usaha, penyedia teknologi, serta lembaga riset dan pendidikan. 
            Peta Jalan "Making Indonesia 4.0" memberikan arah dan strategi yang jelas bagi pergerakan 
            industri Indonesia di masa depan.
            """
        )

    # Fokus 5 sektor industri
    with st.container(border=True):
        st.markdown(
            """
            ### 🎯 Fokus Awal: 5 Sektor Industri Utama

            Untuk penerapan teknologi Industri 4.0 (AI, IoT, robotika otonom, 3D printing), 
            Indonesia pada tahap awal berfokus pada lima sektor industri utama:
            """
        )
        # Tampilkan 5 sektor dalam grid
        sektor_cols = st.columns(5)
        sektor_list = ["🍲 Makanan & Minuman", "👕 Tekstil & Pakaian", "🚗 Otomotif", "🧪 Kimia", "📱 Elektronik"]
        for i, sektor in enumerate(sektor_list):
            with sektor_cols[i]:
                st.markdown(f"**{sektor}**")

        st.markdown(
            """
            Sektor lain tetap didorong melakukan transformasi digital. Pemilihan kelima sektor ini 
            berdasarkan evaluasi dampak ekonomi dan kriteria kelayakan implementasi: ukuran PDB, 
            perdagangan, potensi dampak antar industri, investasi, dan kecepatan penetrasi pasar.
            Setiap 3–4 tahun strategi setiap sektor akan dievaluasi.
            """
        )

    # 10 Inisiatif Nasional Lintas Sektoral
    with st.container(border=True):
        st.markdown(
            """
            ### 🔗 10 Inisiatif Nasional Lintas Sektoral

            Faktor penghambat transformasi digital sering bersifat lintas sektoral. 
            "Making Indonesia 4.0" memuat inisiatif nasional sebagai prasyarat percepatan transformasi:
            """
        )
        inisiatif_list = [
            "1. Perbaikan alur aliran barang",
            "2. Desain ulang zona industri",
            "3. Mengakomodasi standar keberlanjutan (sustainability)",
            "4. Memberdayakan UMKM",
            "5. Membangun infrastruktur digital nasional",
            "6. Menarik minat investasi asing",
            "7. Peningkatan kualitas SDM",
            "8. Pembangunan ekosistem inovasi",
            "9. Insentif untuk investasi teknologi",
            "10. Harmonisasi aturan dan kebijakan"
        ]
        for inisiatif in inisiatif_list:
            st.markdown(f"- {inisiatif}")

    # Peluang dan target PDB
    with st.container(border=True):
        st.markdown(
            """
            ### 📈 Peluang dan Target

            Revolusi Industri 4.0 memberi peluang merevitalisasi manufaktur Indonesia dan 
            mempercepat pencapaian visi menjadi **10 ekonomi terbesar dunia**.

            - **2016**: Industri manufaktur berkontribusi **20% PDB**, membuka **>14 juta lapangan kerja**.
            - Implementasi "Making Indonesia 4.0" yang sukses diperkirakan mendorong pertumbuhan PDB riil 
              **1–2% per tahun**, sehingga pertumbuhan PDB tahunan naik dari **5% (baseline) menjadi 6–7%** 
              pada periode **2018–2030**.
            - Pada **2030**, industri manufaktur ditargetkan berkontribusi **21–26% PDB**.
            """
        )

    # Timeline implementasi
    with st.container(border=True):
        st.markdown(
            """
            ### 📅 Implementasi Bertahap

            - **Semester I 2018**: Mulai menyusun satuan tugas untuk 5 sektor fokus dan 10 inisiatif lintas sektor.
            - **Semester II 2018**: Satuan tugas menyusun rencana utama, merinci rencana aksi, dan menjalankan inisiatif 
              dengan koordinasi antar satuan tugas.
            """
        )

    # INDI 4.0 dan perbandingan dengan Jerman
    with st.container(border=True):
        st.markdown(
            """
            ### 📊 INDI 4.0 – Indonesia Industry 4.0 Readiness Index

            Pada **April 2019**, Kemenperin meluncurkan **INDI 4.0** di IIS 2019. 
            INDI 4.0 adalah indikator penilaian mandiri (self-assessment) tingkat kesiapan industri 
            dalam menerapkan teknologi Industri 4.0, sebagai bagian dari "Making Indonesia 4.0".

            **Lima pilar yang diukur:**
            - Manajemen dan organisasi
            - Orang dan budaya
            - Produk dan layanan
            - Teknologi
            - Operasi pabrik

            **Perbandingan dengan negara lain:**
            Di Jerman, **VDMA** (Asosiasi Pembuat Mesin Jerman) mengembangkan *Industrie 4.0 Readiness* 
            dengan empat dimensi: (1) *Smart Factory*, (2) *Smart Product*, (3) *Smart Operation*, 
            (4) *Data-driven Service* – menggabungkan dunia fisik dan virtual.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("🇮🇩 Making Indonesia 4.0", expanded=True):
        st.markdown(
            """
            - Inisiatif Kemenperin (April 2018)  
            - Peta jalan Industri 4.0 Indonesia  
            - Melibatkan banyak pemangku kepentingan
            """
        )

    with st.expander("🎯 5 Sektor Fokus"):
        st.markdown(
            """
            - Makanan & Minuman  
            - Tekstil & Pakaian  
            - Otomotif  
            - Kimia  
            - Elektronik  
            Dipilih berdasar dampak ekonomi & kelayakan
            """
        )

    with st.expander("🔟 10 Inisiatif Lintas Sektor"):
        st.markdown(
            """
            - Perbaikan alur barang  
            - Desain ulang zona industri  
            - Standar keberlanjutan  
            - Pemberdayaan UMKM  
            - Infrastruktur digital nasional  
            - Investasi asing  
            - Peningkatan SDM  
            - Ekosistem inovasi  
            - Insentif teknologi  
            - Harmonisasi aturan
            """
        )

    with st.expander("📈 Target PDB"):
        st.markdown(
            """
            - Kontribusi manufaktur 20% PDB (2016)  
            - Tambahan 1-2% pertumbuhan PDB per tahun  
            - Target pertumbuhan 6-7% (2018-2030)  
            - Kontribusi manufaktur 21-26% di 2030
            """
        )

    with st.expander("📊 INDI 4.0"):
        st.markdown(
            """
            - Diluncurkan April 2019  
            - Self-assessment kesiapan Industri 4.0  
            - 5 pilar: Manajemen, SDM, Produk, Teknologi, Operasi  
            - Jerman (VDMA): 4 dimensi (Smart Factory, Smart Product, Smart Operation, Data-driven Service)
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📈 Fakta Singkat")
        st.metric("Tahun Peluncuran Making 4.0", "2018")
        st.metric("Sektor Fokus", "5")
        st.metric("Inisiatif Lintas Sektor", "10")
        st.metric("INDI 4.0 Diluncurkan", "2019")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Kementerian Perindustrian RI  
            - Indonesia Industrial Summit 2018, 2019  
            - VDMA (Jerman)
            """
        )