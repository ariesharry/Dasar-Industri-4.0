import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (10)
# =========================

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Apa kepanjangan dari CIA dalam information security?",
    "pilihan": [
        "Confidentiality, Integrity, Availability",
        "Central Intelligence Agency",
        "Computer Internet Architecture",
        "Confidentiality, Internet, Access",
        "Cryptography, Identity, Authentication"
    ],
    "jawaban_benar": "Confidentiality, Integrity, Availability"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Ancaman yang menyebabkan sumber daya sistem dihancurkan sehingga tidak berfungsi disebut ...",
    "pilihan": [
        "Intersepsi",
        "Interupsi",
        "Modifikasi",
        "Fabrikasi",
        "Spionase"
    ],
    "jawaban_benar": "Interupsi"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Berikut adalah metode Information Security, KECUALI:",
    "pilihan": [
        "Network Topology",
        "Security Information Management (SIM)",
        "Intrusion Detection System (IDS)",
        "Data Encryption Standard (DES)",
        "Packet Fingerprinting"
    ],
    "jawaban_benar": "Data Encryption Standard (DES)"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Level keamanan yang berkaitan dengan keamanan fisik adalah level ...",
    "pilihan": [
        "Level 0",
        "Level 1",
        "Level 2",
        "Level 3",
        "Level 4"
    ],
    "jawaban_benar": "Level 0"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Jenis penyusup yang hanya membaca data tidak terotorisasi disebut ...",
    "pilihan": [
        "Penyusup pasif",
        "Penyusup aktif",
        "Hacker",
        "Cracker",
        "Script kiddie"
    ],
    "jawaban_benar": "Penyusup pasif"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Sistem yang digunakan untuk mendeteksi dan melindungi dari serangan dengan cara memeriksa salinan paket disebut ...",
    "pilihan": [
        "IPS",
        "IDS",
        "Firewall",
        "SIM",
        "Port Scanner"
    ],
    "jawaban_benar": "IDS"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Berikut adalah sumber ancaman siber, KECUALI:",
    "pilihan": [
        "Negara",
        "Penjahat dunia maya",
        "Orang dalam (insider)",
        "Konfigurasi cloud yang baik",
        "Pengembang produk di bawah standar"
    ],
    "jawaban_benar": "Konfigurasi cloud yang baik"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Filosofi 'Kenali dirimu dan kenali musuhmu' dalam risk management berasal dari ...",
    "pilihan": [
        "Sun Tzu",
        "Confucius",
        "Lao Tzu",
        "Machiavelli",
        "Sun Yat-sen"
    ],
    "jawaban_benar": "Sun Tzu"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Pejabat yang bertanggung jawab menetapkan visi dan strategi keamanan informasi di perusahaan adalah ...",
    "pilihan": [
        "CEO",
        "CFO",
        "CISO",
        "CTO",
        "COO"
    ],
    "jawaban_benar": "CISO"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Proses untuk memilah ancaman mana yang sangat berpotensi merugikan disebut ...",
    "pilihan": [
        "Risk identification",
        "Risk assessment",
        "Risk control",
        "Risk mitigation",
        "Risk avoidance"
    ],
    "jawaban_benar": "Risk assessment"
},

# =========================
# SHORT ANSWER (5)
# =========================

{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan tiga elemen segitiga CIA!",
    "jawaban_benar": "confidentiality, integrity, availability"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa perbedaan IDS dan IPS?",
    "jawaban_benar": "IDS mendeteksi dan memberi peringatan, IPS mencegah dengan menolak paket"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan dua penyebab data loss!",
    "jawaban_benar": "bencana, kesalahan perangkat lunak, kesalahan manusia"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa fungsi dari Security Information Management (SIM)?",
    "jawaban_benar": "menyediakan informasi keamanan terpusat dan analisis data"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan dua kegiatan pertahanan siber yang dilakukan CISO!",
    "jawaban_benar": "mengelola pelatihan keamanan, konfigurasi perangkat aman, deteksi intrusi, dll"
}

]

# Inisialisasi session state
if "cek_dilakukan" not in st.session_state:
    st.session_state.cek_dilakukan = False

st.title("Latihan Soal: Keamanan Siber (Bab IX)")

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