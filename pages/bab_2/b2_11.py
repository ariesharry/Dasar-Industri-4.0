import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (10)
# =========================

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Siapa yang dikenal sebagai pelopor gagasan Internet of Things (IoT) dari laboratorium MIT's AutoID?",
    "pilihan": [
        "Steve Jobs",
        "Bill Gates",
        "Kevin Ashton",
        "Mark Zuckerberg",
        "Elon Musk"
    ],
    "jawaban_benar": "Kevin Ashton"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Menurut Hung (2017) dari Gartner Research, IoT adalah jaringan objek fisik khusus yang mengandung ...",
    "pilihan": [
        "teknologi nirkabel dan sensor",
        "teknologi tertanam (embedded technology) untuk berkomunikasi dan merasakan",
        "sistem operasi dan aplikasi",
        "koneksi internet berkecepatan tinggi",
        "big data dan cloud computing"
    ],
    "jawaban_benar": "teknologi tertanam (embedded technology) untuk berkomunikasi dan merasakan"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Berikut ini yang BUKAN merupakan tiga elemen utama konsep kerja IoT menurut mobnasesemka.com adalah ...",
    "pilihan": [
        "Barang fisik yang dilengkapi modul IoT",
        "Perangkat koneksi ke internet (modem, router)",
        "Cloud Data Center",
        "Sensor dan aktuator pada setiap perangkat",
        "Aplikasi mobile untuk kontrol"
    ],
    "jawaban_benar": "Aplikasi mobile untuk kontrol"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Empat pilar IoT menurut Khan (2018) meliputi M2M, RFID, WSN, dan ...",
    "pilihan": [
        "CPS",
        "SCADA",
        "AI",
        "IIoT",
        "AR/VR"
    ],
    "jawaban_benar": "SCADA"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Produk IoT karya anak bangsa yang bergerak di bidang pemberian pakan ikan otomatis adalah ...",
    "pilihan": [
        "HARA",
        "Qlue",
        "Spekun",
        "eFishery",
        "Nodeflux"
    ],
    "jawaban_benar": "eFishery"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Manakah pernyataan yang paling tepat mengenai perbedaan IoT dan M2M?",
    "pilihan": [
        "IoT lebih menekankan komunikasi antar mesin, M2M fokus pada konektivitas internet",
        "M2M adalah bagian dari IoT dan berfokus pada komunikasi mesin-ke-mesin dengan intervensi manusia minimal",
        "IoT tidak membutuhkan internet, sedangkan M2M selalu menggunakan internet",
        "M2M hanya digunakan di industri, IoT hanya untuk konsumen",
        "IoT dan M2M adalah dua istilah yang sama persis"
    ],
    "jawaban_benar": "M2M adalah bagian dari IoT dan berfokus pada komunikasi mesin-ke-mesin dengan intervensi manusia minimal"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Karakteristik IoT yang memungkinkan perangkat menyesuaikan diri secara otomatis dengan perubahan lingkungan disebut ...",
    "pilihan": [
        "Konfigurasi diri",
        "Protokol interoperable",
        "Dinamis dan beradaptasi dengan sendiri",
        "Identifikasi otomatis",
        "Virtualisasi"
    ],
    "jawaban_benar": "Dinamis dan beradaptasi dengan sendiri"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Klasifikasi IoT yang ditujukan untuk segmen bisnis ke bisnis (B2B) dan digunakan di pabrik, perusahaan, dll. disebut ...",
    "pilihan": [
        "Consumer IoT (CIoT)",
        "Industrial IoT (IIoT)",
        "Commercial IoT",
        "Enterprise IoT",
        "Manufacturing IoT"
    ],
    "jawaban_benar": "Industrial IoT (IIoT)"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Menurut Chuprina (2019), salah satu perbedaan teknologi antara IIoT dan CIoT adalah ...",
    "pilihan": [
        "IIoT lebih murah dan lebih kecil ukurannya",
        "IIoT harus tahan terhadap lingkungan berbahaya dan memiliki keamanan cyber yang kuat",
        "CIoT selalu menggunakan protokol yang sama, IIoT menggunakan protokol yang berbeda-beda",
        "IIoT tidak memerlukan skalabilitas, CIoT harus sangat skalabel",
        "CIoT lebih sering menggunakan white label, IIoT selalu bermerek"
    ],
    "jawaban_benar": "IIoT harus tahan terhadap lingkungan berbahaya dan memiliki keamanan cyber yang kuat"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Arsitektur IoT menurut Zhang dan Yu (dalam Soumyalatha & Hegde, 2016) terdiri dari berapa lapisan?",
    "pilihan": [
        "2",
        "3",
        "4",
        "5",
        "6"
    ],
    "jawaban_benar": "4"
},

# =========================
# SHORT ANSWER (5)
# =========================

{
    "tipe": "isian_singkat",
    "pertanyaan": "Siapa tokoh yang mencetuskan ide IoT saat bekerja di Proctor & Gamble dengan menghubungkan informasi RFID ke internet?",
    "jawaban_benar": "Kevin Ashton"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Aplikasi smart city yang diluncurkan Pemprov DKI Jakarta pada tahun 2015 sebagai platform warga menyampaikan keluhan adalah ...",
    "jawaban_benar": "Qlue"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan salah satu teknologi dalam pilar IoT yang menggunakan gelombang radio untuk transfer data dari tag elektronik (singkatan)!",
    "jawaban_benar": "RFID"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa perbedaan utama antara Augmented Reality (AR) dan Virtual Reality (VR)? (Jawab singkat)",
    "jawaban_benar": "AR menambahkan objek virtual ke dunia nyata, VR menciptakan dunia maya sepenuhnya"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa kepanjangan dari AIDC? (dalam bahasa Inggris)",
    "jawaban_benar": "Automatic Identification and Data Capture"
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