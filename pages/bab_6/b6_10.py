import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (10)
# =========================

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Apa yang dimaksud dengan big data menurut McKinsey Global (2011)?",
    "pilihan": [
        "Data yang hanya berupa angka",
        "Data dengan volume, kecepatan, dan keragaman sangat besar, membutuhkan arsitektur inovatif untuk mendapatkan nilai bisnis",
        "Data yang hanya tersimpan di cloud",
        "Data yang tidak bisa diolah dengan komputer",
        "Data yang selalu terstruktur"
    ],
    "jawaban_benar": "Data dengan volume, kecepatan, dan keragaman sangat besar, membutuhkan arsitektur inovatif untuk mendapatkan nilai bisnis"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Berikut adalah karakteristik 5V big data, KECUALI:",
    "pilihan": [
        "Volume",
        "Velocity",
        "Variety",
        "Veracity",
        "Viability"
    ],
    "jawaban_benar": "Viability"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Data seperti teks, gambar, video, dan email termasuk dalam kategori ...",
    "pilihan": [
        "Data terstruktur",
        "Data semi‑terstruktur",
        "Data tidak terstruktur",
        "Data warehouse",
        "Data mart"
    ],
    "jawaban_benar": "Data tidak terstruktur"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Gudang penyimpanan besar untuk data mentah dalam format aslinya disebut ...",
    "pilihan": [
        "Data warehouse",
        "Data mart",
        "Data lake",
        "Database relasional",
        "Data mining"
    ],
    "jawaban_benar": "Data lake"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Teknik data mining yang mengelompokkan obyek tanpa label kelas disebut ...",
    "pilihan": [
        "Klasifikasi",
        "Regresi",
        "Klastering",
        "Asosiasi",
        "Prediksi"
    ],
    "jawaban_benar": "Klastering"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Apa fungsi utama dari data warehouse?",
    "pilihan": [
        "Menyimpan data mentah sementara",
        "Mendukung pengambilan keputusan dengan data historis yang terintegrasi",
        "Menggantikan database operasional",
        "Hanya untuk backup data",
        "Menganalisis data real‑time"
    ],
    "jawaban_benar": "Mendukung pengambilan keputusan dengan data historis yang terintegrasi"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Manakah yang termasuk teknik advanced analytics?",
    "pilihan": [
        "Pelaporan KPI",
        "Dashboard",
        "Machine learning",
        "OLAP",
        "Ad hoc query"
    ],
    "jawaban_benar": "Machine learning"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Tingkatan analisis yang menjawab pertanyaan 'Apa yang akan terjadi?' adalah ...",
    "pilihan": [
        "Deskriptif",
        "Diagnostik",
        "Prediktif",
        "Preskriptif",
        "Kognitif"
    ],
    "jawaban_benar": "Prediktif"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Subset data warehouse yang berorientasi pada lini bisnis tertentu disebut ...",
    "pilihan": [
        "Data lake",
        "Data mart",
        "Data mining",
        "Database",
        "Data cube"
    ],
    "jawaban_benar": "Data mart"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Proses menemukan pola baru dari data berukuran besar dikenal sebagai ...",
    "pilihan": [
        "Data warehouse",
        "Data visualization",
        "Data mining",
        "Data integration",
        "Data cleaning"
    ],
    "jawaban_benar": "Data mining"
},

# =========================
# SHORT ANSWER (5)
# =========================

{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan tiga elemen penting dalam big data!",
    "jawaban_benar": "data, informasi, pengetahuan"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa kepanjangan dari 5V dalam karakteristik big data? (sebutkan minimal 3)",
    "jawaban_benar": "Volume, Velocity, Variety, Veracity, Value"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Tahapan data mining setelah transformasi data adalah ...",
    "jawaban_benar": "penggalian data"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa perbedaan utama antara data lake dan data warehouse?",
    "jawaban_benar": "data lake menyimpan data mentah dalam format asli, data warehouse menyimpan data terstruktur dan terintegrasi untuk analisis"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan dua manfaat BI dashboard!",
    "jawaban_benar": "identifikasi tren, peningkatan efisiensi"
}

]

# Inisialisasi session state
if "cek_dilakukan" not in st.session_state:
    st.session_state.cek_dilakukan = False

st.title("Latihan Soal: Big Data Analytic")

for i, soal in enumerate(soal_list):
    with st.container():
        st.markdown(f"**Soal {i+1}**")
        st.markdown(f"{soal['pertanyaan']}")
        
        if soal["tipe"] == "pilihan_ganda":
            jawaban_user = st.radio(
                "Pilih jawaban:",
                options=soal["pilihan"],
                key=f"mc_{i}",
                index=None,
                label_visibility="collapsed"
            )
        else:
            jawaban_user = st.text_input(
                "Masukkan jawaban:",
                key=f"sa_{i}",
                label_visibility="collapsed"
            ).strip()
        
        if st.session_state.cek_dilakukan:
            if soal["tipe"] == "pilihan_ganda":
                jawaban = st.session_state.get(f"mc_{i}")
            else:
                jawaban = st.session_state.get(f"sa_{i}", "").strip()
            
            if jawaban is None:
                jawaban = ""
            
            if soal["tipe"] == "isian_singkat":
                benar = jawaban.lower() == soal["jawaban_benar"].lower()
            else:
                benar = jawaban == soal["jawaban_benar"]
            
            if benar:
                st.success("✅ Jawaban Anda benar!")
            else:
                st.error(f"❌ Jawaban Anda salah. Jawaban yang benar: {soal['jawaban_benar']}")
        
        st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔍 Cek Jawaban", use_container_width=True):
        st.session_state.cek_dilakukan = True
        st.rerun()

if st.session_state.cek_dilakukan:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Coba Lagi", use_container_width=True):
            for key in list(st.session_state.keys()):
                if key.startswith("mc_") or key.startswith("sa_"):
                    del st.session_state[key]
            st.session_state.cek_dilakukan = False
            st.rerun()

st.markdown("---")
st.markdown("<p style='text-align: center;'>Selamat belajar! 🌟</p>", unsafe_allow_html=True)