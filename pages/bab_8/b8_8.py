import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (10)
# =========================

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Siapa yang merintis istilah kecerdasan buatan (AI) pada tahun 1956?",
    "pilihan": [
        "Alan Turing",
        "John McCarthy",
        "Marvin Minsky",
        "Herbert Simon",
        "John von Neumann"
    ],
    "jawaban_benar": "John McCarthy"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Menurut Russell & Norvig, definisi AI dikelompokkan menjadi empat kategori, yaitu ...",
    "pilihan": [
        "Berpikir manusiawi, berpikir rasional, bertindak manusiawi, bertindak rasional",
        "Learning, reasoning, self-correction, perception",
        "Supervised, unsupervised, reinforcement, deep learning",
        "Data, informasi, pengetahuan, wisdom",
        "Statis, dinamis, kontinyu, diskrit"
    ],
    "jawaban_benar": "Berpikir manusiawi, berpikir rasional, bertindak manusiawi, bertindak rasional"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Berikut adalah klasifikasi AI menurut Martin (2015), KECUALI:",
    "pilihan": [
        "Machine Learning",
        "Natural Language Processing",
        "Robotics",
        "Cloud Computing",
        "Social Intelligence"
    ],
    "jawaban_benar": "Cloud Computing"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Proses yang terjadi dalam AI mencakup ...",
    "pilihan": [
        "Learning, reasoning, self-correction",
        "Input, proses, output",
        "Rencana, aksi, evaluasi",
        "Data, informasi, pengetahuan",
        "Analisis, prediksi, optimasi"
    ],
    "jawaban_benar": "Learning, reasoning, self-correction"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Menurut Primartha (2018), machine learning adalah ...",
    "pilihan": [
        "Pemrograman komputer untuk mencapai kinerja tertentu dengan data latih",
        "Sistem yang meniru cara berpikir manusia",
        "Jaringan saraf tiruan berlapis-lapis",
        "Pengolahan bahasa alami",
        "Robotika cerdas"
    ],
    "jawaban_benar": "Pemrograman komputer untuk mencapai kinerja tertentu dengan data latih"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Algoritma supervised learning digunakan untuk masalah ...",
    "pilihan": [
        "Klasifikasi dan regresi",
        "Clustering dan asosiasi",
        "Reduksi dimensi",
        "Penguatan feedback",
        "Pengenalan pola tanpa label"
    ],
    "jawaban_benar": "Klasifikasi dan regresi"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Contoh penerapan reinforcement learning adalah ...",
    "pilihan": [
        "Robot belajar menghindari tabrakan",
        "Klasifikasi email spam",
        "Prediksi harga saham",
        "Segmentasi pelanggan",
        "Deteksi objek dalam gambar"
    ],
    "jawaban_benar": "Robot belajar menghindari tabrakan"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Deep learning adalah subset dari ...",
    "pilihan": [
        "Artificial Intelligence saja",
        "Machine Learning",
        "Data Science",
        "Supervised Learning",
        "Reinforcement Learning"
    ],
    "jawaban_benar": "Machine Learning"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Tahun kemunculan deep learning sekitar ...",
    "pilihan": [
        "1950an",
        "1960an",
        "1970an",
        "1980an",
        "1990an"
    ],
    "jawaban_benar": "1970an"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Contoh aplikasi AI di bidang pertanian adalah ...",
    "pilihan": [
        "Pemantauan tanaman untuk optimasi air dan pupuk",
        "Diagnosis penyakit",
        "Prediksi pasar saham",
        "Rekomendasi film",
        "Pengenalan wajah"
    ],
    "jawaban_benar": "Pemantauan tanaman untuk optimasi air dan pupuk"
},

# =========================
# SHORT ANSWER (5)
# =========================

{
    "tipe": "isian_singkat",
    "pertanyaan": "Siapa pencetus istilah kecerdasan buatan (AI)?",
    "jawaban_benar": "John McCarthy"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan tiga proses yang terjadi dalam AI!",
    "jawaban_benar": "learning, reasoning, self-correction"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa perbedaan utama supervised learning dan unsupervised learning?",
    "jawaban_benar": "supervised menggunakan data berlabel, unsupervised menggunakan data tak berlabel"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan dua bidang aplikasi AI di industri!",
    "jawaban_benar": "kesehatan, pertanian, keuangan, pendidikan, manufaktur, dll"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa kepanjangan dari NLP dalam AI?",
    "jawaban_benar": "Natural Language Processing"
}

]

# Inisialisasi session state
if "cek_dilakukan" not in st.session_state:
    st.session_state.cek_dilakukan = False

st.title("Latihan Soal: Kecerdasan Buatan (Bab VIII)")

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