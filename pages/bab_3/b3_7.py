import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (5)
# =========================

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Apa yang menjadi dasar terbukanya gerbang menuju revolusi industri 4.0 menurut teks?",
    "pilihan": [
        "Penemuan listrik",
        "Perkembangan teknologi dan internet",
        "Penemuan robot pertama",
        "Revolusi digital",
        "Kecerdasan buatan"
    ],
    "jawaban_benar": "Perkembangan teknologi dan internet"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Robot otonom adalah robot yang ...",
    "pilihan": [
        "Bekerja dengan kontrol langsung manusia",
        "Bekerja mandiri tanpa kontrol langsung manusia",
        "Bekerja hanya dengan perintah suara",
        "Tidak memerlukan sensor",
        "Hanya digunakan di industri militer"
    ],
    "jawaban_benar": "Bekerja mandiri tanpa kontrol langsung manusia"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Komponen utama yang digunakan robot otonom untuk memproses data dari sensor adalah ...",
    "pilihan": [
        "Aktuator",
        "Komputer pusat",
        "Transmitter",
        "Roda",
        "Lengan robot"
    ],
    "jawaban_benar": "Komputer pusat"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Berikut ini adalah keunggulan autonomous robot dibandingkan AGV, KECUALI:",
    "pilihan": [
        "Navigasi otonom tanpa track",
        "Dapat bermanuver di sekitar rintangan",
        "Membutuhkan perubahan infrastruktur untuk memperluas jalur",
        "Menavigasi secara dinamis menggunakan peta fasilitas",
        "Lebih fleksibel"
    ],
    "jawaban_benar": "Membutuhkan perubahan infrastruktur untuk memperluas jalur"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Contoh robot otonom yang disebutkan dalam teks adalah ...",
    "pilihan": [
        "Robot pembersih lantai di bandara",
        "Robot pengelasan",
        "Robot pengecatan mobil",
        "Robot SCARA",
        "Robot CNC"
    ],
    "jawaban_benar": "Robot pembersih lantai di bandara"
},

# =========================
# SHORT ANSWER (5)
# =========================

{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa kepanjangan dari AGV?",
    "jawaban_benar": "Automated Guided Vehicle"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan dua fitur yang memungkinkan robot otonom memahami lingkungan fisiknya!",
    "jawaban_benar": "sensor dan peralatan fungsional"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Bagaimana cara robot otonom menentukan tindakan yang harus diambil?",
    "jawaban_benar": "dengan komputer pusat memproses data sensor menggunakan algoritma"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa perbedaan utama dalam hal navigasi antara AGV dan autonomous robot?",
    "jawaban_benar": "AGV butuh track dan jalur tetap, autonomous robot navigasi otonom tanpa track dan dinamis dengan peta"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Mengapa robot otonom masih perlu dipelihara secara fisik meskipun bekerja secara otonom?",
    "jawaban_benar": "karena tetap memerlukan perawatan seperti penggantian komponen, pembersihan, perbaikan"
}

]

# Inisialisasi session state untuk menyimpan status koreksi
if "cek_dilakukan" not in st.session_state:
    st.session_state.cek_dilakukan = False

st.title("Latihan Soal: Robot Otonom")

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
                # Perbandingan sederhana, bisa dikembangkan lebih lanjut
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