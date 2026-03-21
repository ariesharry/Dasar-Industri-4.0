import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (10)
# =========================

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Apa nama awal dari konsep manufaktur aditif yang dikembangkan pada 1980-an?",
    "pilihan": [
        "Additive Manufacturing",
        "Rapid Prototyping",
        "3D Printing",
        "CNC Machining",
        "Subtractive Manufacturing"
    ],
    "jawaban_benar": "Rapid Prototyping"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Standar industri resmi untuk terminologi manufaktur aditif adalah ...",
    "pilihan": [
        "ISO 9001",
        "ASTM F2792",
        "IEC 61508",
        "IEEE 802.11",
        "ASME Y14.5"
    ],
    "jawaban_benar": "ASTM F2792"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Tahap paling penting dalam proses manufaktur aditif yang membagi model 3D menjadi lapisan-lapisan disebut ...",
    "pilihan": [
        "Konversi STL",
        "Pengirisan (slicing)",
        "Paska-pemrosesan",
        "Perbaikan model",
        "Pengaturan parameter"
    ],
    "jawaban_benar": "Pengirisan (slicing)"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Teknologi AM yang menggunakan resin photopolymer dan sinar UV termasuk dalam kategori ...",
    "pilihan": [
        "FDM",
        "PBF",
        "Vat Photopolymerization",
        "Material Jetting",
        "Binder Jetting"
    ],
    "jawaban_benar": "Vat Photopolymerization"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Metode AM yang paling banyak digunakan antara lain adalah ...",
    "pilihan": [
        "SLS, SLM, FDM",
        "CNC, EDM, Wire Cut",
        "Injection Molding",
        "Casting, Forging",
        "Welding, Brazing"
    ],
    "jawaban_benar": "SLS, SLM, FDM"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Kelebihan utama manufaktur aditif dibandingkan metode tradisional adalah ...",
    "pilihan": [
        "Presisi tinggi",
        "Kecepatan produksi massal",
        "Kemampuan membuat geometri kompleks",
        "Material lebih beragam",
        "Biaya per unit lebih murah untuk jumlah besar"
    ],
    "jawaban_benar": "Kemampuan membuat geometri kompleks"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Kekurangan manufaktur aditif dalam hal presisi adalah ...",
    "pilihan": [
        "± 0,X00 mm",
        "± 0,000 mm",
        "± 0,XX0 mm",
        "± 0,0X0 mm",
        "± 0,000X mm"
    ],
    "jawaban_benar": "± 0,X00 mm"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Studi kasus menunjukkan bahwa limbah material pada AM berkurang sekitar ...",
    "pilihan": [
        "10%",
        "20%",
        "40%",
        "60%",
        "80%"
    ],
    "jawaban_benar": "40%"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Sektor industri yang menyumbang 20% pasar AM menurut Mehrpouya (2019) adalah ...",
    "pilihan": [
        "Kesehatan dan arsitektur",
        "Otomotif dan dirgantara",
        "Elektronik dan semikonduktor",
        "Pertanian dan pangan",
        "Energi dan tambang"
    ],
    "jawaban_benar": "Otomotif dan dirgantara"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Komponen pesawat yang dapat diproduksi dengan AM antara lain ...",
    "pilihan": [
        "Mesin turbin",
        "Roda pendaratan",
        "Engsel dan braket",
        "Sayap utama",
        "Badan pesawat"
    ],
    "jawaban_benar": "Engsel dan braket"
},

# =========================
# SHORT ANSWER (5)
# =========================

{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan dua metode AM yang termasuk dalam kategori Powder Bed Fusion!",
    "jawaban_benar": "SLS, SLM, EBM"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa keuntungan utama AM dalam hal kustomisasi?",
    "jawaban_benar": "modifikasi desain semudah desain asli tanpa tooling tambahan"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan dua contoh paska-pemrosesan pada AM!",
    "jawaban_benar": "penghilangan penopang, fine machining, heat treatment, polishing"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa perbedaan utama antara manufaktur aditif dan subtraktif?",
    "jawaban_benar": "aditif menambah material lapis demi lapis, subtraktif menguranginya"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan tiga bidang aplikasi AM selain otomotif dan dirgantara!",
    "jawaban_benar": "seni, kesehatan, arsitektur"
}

]

# Inisialisasi session state
if "cek_dilakukan" not in st.session_state:
    st.session_state.cek_dilakukan = False

st.title("Latihan Soal: Manufaktur Aditif (Bab X)")

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