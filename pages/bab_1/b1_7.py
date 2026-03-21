import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (10)
# =========================
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Di negara mana dan tahun berapa istilah Industri 4.0 pertama kali dicetuskan?",
    "pilihan": [
        "Amerika Serikat, 2015",
        "Jerman, 2011",
        "Jepang, 2010",
        "Inggris, 2012",
        "China, 2013"
    ],
    "jawaban_benar": "Jerman, 2011"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Apa tujuan utama dari inisiatif Industri 4.0 menurut Pemerintah Jerman?",
    "pilihan": [
        "Meningkatkan produksi massal dengan tenaga listrik",
        "Mengembangkan teknologi mekanisasi tenaga air dan uap",
        "Transformasi industri manufaktur melalui digitalisasi dan teknologi baru",
        "Memperkenalkan otomatisasi dengan teknologi informasi",
        "Menciptakan pasar global yang terpusat"
    ],
    "jawaban_benar": "Transformasi industri manufaktur melalui digitalisasi dan teknologi baru"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Istilah lain yang digunakan oleh negara lain untuk konsep Industri 4.0 adalah …",
    "pilihan": [
        "Industrial Internet of Things",
        "Cyber-Physical Production",
        "Digital Manufacturing",
        "Advanced Robotics",
        "Cloud Factory"
    ],
    "jawaban_benar": "Industrial Internet of Things"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Menurut definisi komprehensif, Industri 4.0 memanfaatkan konvergensi antara …",
    "pilihan": [
        "Teknologi mekanik dan listrik",
        "Teknologi informasi dan teknologi operasional",
        "Teknologi uap dan tenaga air",
        "Teknologi otomatisasi dan robotika",
        "Teknologi elektronik dan telekomunikasi"
    ],
    "jawaban_benar": "Teknologi informasi dan teknologi operasional"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Berapa jumlah lapisan (layer) dalam dimensi arsitektur RAMI 4.0?",
    "pilihan": [
        "4",
        "5",
        "6",
        "7",
        "8"
    ],
    "jawaban_benar": "6"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Prinsip desain Industri 4.0 yang memungkinkan mesin dari berbagai produsen saling berkomunikasi disebut …",
    "pilihan": [
        "Virtualisasi",
        "Desentralisasi",
        "Interoperabilitas",
        "Modularitas",
        "Orientasi layanan"
    ],
    "jawaban_benar": "Interoperabilitas"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Manakah yang termasuk dalam sembilan teknologi kunci Industri 4.0 menurut BCG?",
    "pilihan": [
        "Virtual Reality, Blockchain, 5G",
        "Big Data Analytics, Autonomous Robot, Additive Manufacturing",
        "Machine Learning, Edge Computing, Digital Twin",
        "Biotechnology, Nanotechnology, Smart Grid",
        "Quantum Computing, Neural Networks, Holography"
    ],
    "jawaban_benar": "Big Data Analytics, Autonomous Robot, Additive Manufacturing"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Salah satu manfaat Industri 4.0 adalah kemampuan bereaksi cepat terhadap kegagalan mesin dan mengubah rute produksi. Manfaat ini termasuk dalam kategori …",
    "pilihan": [
        "Efisiensi",
        "Kelincahan (agility)",
        "Inovasi",
        "Pengalaman pelanggan",
        "Pendapatan"
    ],
    "jawaban_benar": "Kelincahan (agility)"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Berapa jumlah sektor industri yang menjadi fokus utama dalam Making Indonesia 4.0 tahap awal?",
    "pilihan": [
        "3",
        "4",
        "5",
        "6",
        "7"
    ],
    "jawaban_benar": "5"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Apa nama indeks yang diluncurkan Kementerian Perindustrian pada 2019 untuk mengukur kesiapan industri Indonesia dalam menerapkan Industri 4.0?",
    "pilihan": [
        "IDI 4.0",
        "INDI 4.0",
        "I4.0 Readiness",
        "Smart Industry Index",
        "Manufacturing 4.0 Index"
    ],
    "jawaban_benar": "INDI 4.0"
},

# =========================
# SHORT ANSWER (5)
# =========================
{
    "tipe": "isian_singkat",
    "pertanyaan": "Negara yang pertama kali mencetuskan konsep Industri 4.0 adalah ...",
    "jawaban_benar": "Jerman"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Tahun pertama kali istilah Industri 4.0 diperkenalkan dalam acara Hannover Messe adalah ...",
    "jawaban_benar": "2011"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Jumlah prinsip desain Industri 4.0 menurut Mabkhot dkk dan Hermann dkk adalah ...",
    "jawaban_benar": "6"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Berdasarkan laporan BCG 2015, jumlah teknologi kunci yang mendukung Industri 4.0 adalah ...",
    "jawaban_benar": "9"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Singkatan dari sistem yang menggabungkan dunia fisik dan virtual dalam Industri 4.0 adalah ...",
    "jawaban_benar": "CPS"
}

]

# Inisialisasi session state untuk menyimpan status koreksi
if "cek_dilakukan" not in st.session_state:
    st.session_state.cek_dilakukan = False

# Tampilkan setiap soal
for i, soal in enumerate(soal_list):
    with st.container():
        st.markdown(f"**Soal {i+1}**")
        st.markdown(f"{soal['pertanyaan']}")
        
        # Input berdasarkan tipe soal
        if soal["tipe"] == "pilihan_ganda":
            jawaban_user = st.radio(
                "Pilih jawaban:",
                options=soal["pilihan"],
                key=f"mc_{i}",
                index=None,
                label_visibility="collapsed"
            )
        else:  # isian
            jawaban_user = st.text_input(
                "Masukkan jawaban:",
                key=f"sa_{i}",
                label_visibility="collapsed"
            ).strip()
        
        # Jika sudah dicek, tampilkan feedback
        if st.session_state.cek_dilakukan:
            # Ambil jawaban user dari session state
            if soal["tipe"] == "pilihan_ganda":
                jawaban = st.session_state.get(f"mc_{i}")
            else:
                jawaban = st.session_state.get(f"sa_{i}", "").strip()
            
            # Pastikan jawaban tidak None untuk pilihan ganda
            if jawaban is None:
                jawaban = ""
            
            # Bandingkan dengan jawaban benar (case insensitive untuk isian)
            if soal["tipe"] == "isian_singkat":
                benar = jawaban.lower() == soal["jawaban_benar"].lower()
            else:
                benar = jawaban == soal["jawaban_benar"]
            
            if benar:
                st.success("✅ Jawaban Anda benar!")
            else:
                st.error(f"❌ Jawaban Anda salah. Jawaban yang benar: {soal['jawaban_benar']}")
        
        st.markdown("---")

# Tombol untuk mengecek jawaban
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔍 Cek Jawaban", use_container_width=True):
        st.session_state.cek_dilakukan = True
        st.rerun()

# Tombol untuk mengulang (reset)
if st.session_state.cek_dilakukan:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Coba Lagi", use_container_width=True):
            # Hapus semua jawaban dari session state
            for key in list(st.session_state.keys()):
                if key.startswith("mc_") or key.startswith("sa_"):
                    del st.session_state[key]
            st.session_state.cek_dilakukan = False
            st.rerun()

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Selamat belajar! 🌟</p>", unsafe_allow_html=True)