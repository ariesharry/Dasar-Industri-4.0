import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (10)
# =========================

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Menurut Kelton dkk (2010), simulasi adalah ...",
    "pilihan": [
        "Metode analisis matematis untuk sistem sederhana",
        "Sekumpulan metode dan aplikasi untuk meniru perilaku sistem nyata",
        "Teknik pengambilan keputusan tanpa memerlukan data",
        "Proses membangun sistem fisik sebelum produksi",
        "Alat untuk menggantikan sistem nyata"
    ],
    "jawaban_benar": "Sekumpulan metode dan aplikasi untuk meniru perilaku sistem nyata"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Berikut ini adalah kelebihan simulasi menurut Siswanto dkk (2017), KECUALI:",
    "pilihan": [
        "Mampu memodelkan keterkaitan antar elemen yang rumit",
        "Output menunjukkan perilaku sistem dari waktu ke waktu",
        "Memerlukan biaya besar dan waktu lama",
        "Tidak merusak sistem nyata",
        "Hasil mudah dimengerti"
    ],
    "jawaban_benar": "Memerlukan biaya besar dan waktu lama"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Law (2015) menyebutkan bahwa simulasi berguna untuk analisis sistem berikut, KECUALI:",
    "pilihan": [
        "Desain sistem manufaktur",
        "Evaluasi desain organisasi jasa",
        "Analisis rantai pasokan",
        "Peramalan cuaca jangka panjang",
        "Penentuan kebijakan pemesanan persediaan"
    ],
    "jawaban_benar": "Peramalan cuaca jangka panjang"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Simulasi statis adalah simulasi yang ...",
    "pilihan": [
        "Perubahan variabelnya dipengaruhi waktu",
        "Digunakan untuk mengetahui kondisi sistem pada saat tertentu",
        "Variabel berubah secara kontinyu",
        "Menggunakan nilai acak",
        "Memerlukan data real-time"
    ],
    "jawaban_benar": "Digunakan untuk mengetahui kondisi sistem pada saat tertentu"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Contoh simulasi kontinyu adalah ...",
    "pilihan": [
        "Perubahan panjang antrian di server",
        "Simulasi permintaan produk dengan data historis",
        "Perubahan volume bahan bakar dalam tangki",
        "Waktu pemanasan microwave yang konstan",
        "Jumlah pelanggan dalam sistem antrian"
    ],
    "jawaban_benar": "Perubahan volume bahan bakar dalam tangki"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Simulasi stokastik ditandai dengan ...",
    "pilihan": [
        "Variabel bernilai konstan",
        "Variabel berubah secara acak",
        "Tidak dipengaruhi waktu",
        "Hanya untuk sistem diskrit",
        "Hasil pasti"
    ],
    "jawaban_benar": "Variabel berubah secara acak"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Menurut Russmann dkk (2015), simulasi merupakan salah satu dari ... teknologi kunci Industri 4.0.",
    "pilihan": [
        "5",
        "7",
        "9",
        "11",
        "12"
    ],
    "jawaban_benar": "9"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Contoh pemanfaatan simulasi dalam Industri 4.0 yang disebutkan dalam teks adalah ...",
    "pilihan": [
        "Simulasi lalu lintas",
        "Simulasi promosi Go-Food",
        "Simulasi bangunan",
        "Simulasi cuaca",
        "Simulasi keuangan"
    ],
    "jawaban_benar": "Simulasi promosi Go-Food"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Digital twin didefinisikan sebagai ... (Shaw & Fruhlinger, 2019)",
    "pilihan": [
        "Model fisik dari produk",
        "Representasi digital dari objek fisik atau sistem",
        "Simulasi statis",
        "Database cloud",
        "Sensor pada mesin"
    ],
    "jawaban_benar": "Representasi digital dari objek fisik atau sistem"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Tiga elemen digital twin menurut Michael Grieves adalah ...",
    "pilihan": [
        "Sensor, aktuator, cloud",
        "Benda fisik, digital twin, informasi penghubung",
        "Hardware, software, firmware",
        "Data, informasi, pengetahuan",
        "Desain, produksi, pemeliharaan"
    ],
    "jawaban_benar": "Benda fisik, digital twin, informasi penghubung"
},

# =========================
# SHORT ANSWER (5)
# =========================

{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan tiga kelebihan simulasi menurut Siswanto dkk (2017)!",
    "jawaban_benar": "memodelkan keterkaitan antar elemen, fleksibel, hemat waktu dan biaya, tidak merusak sistem, mudah dikomunikasikan"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa perbedaan antara simulasi statis dan dinamis?",
    "jawaban_benar": "simulasi statis tidak dipengaruhi waktu, simulasi dinamis dipengaruhi waktu"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan dua contoh penerapan simulasi menurut Law (2015)!",
    "jawaban_benar": "desain sistem manufaktur, evaluasi organisasi jasa, analisis rantai pasokan, dll"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan tiga elemen digital twin menurut Michael Grieves!",
    "jawaban_benar": "benda fisik, digital twin, informasi penghubung"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan tiga tahap kerja digital twin!",
    "jawaban_benar": "melihat, berpikir, melakukan"
}

]

# Inisialisasi session state untuk menyimpan status koreksi
if "cek_dilakukan" not in st.session_state:
    st.session_state.cek_dilakukan = False

st.title("Latihan Soal: Simulasi (Bab VII)")

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