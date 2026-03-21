import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (10)
# =========================

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Apa definisi komputasi awan (cloud computing)?",
    "pilihan": [
        "Penyimpanan data hanya di hard disk lokal",
        "Layanan yang di-host melalui internet, data dan program diakses via internet",
        "Sistem operasi untuk komputer meja",
        "Jaringan komputer tanpa internet",
        "Perangkat keras server fisik"
    ],
    "jawaban_benar": "Layanan yang di-host melalui internet, data dan program diakses via internet"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Model layanan cloud yang menyediakan infrastruktur virtual (server, storage, jaringan) disebut ...",
    "pilihan": [
        "SaaS",
        "PaaS",
        "IaaS",
        "CaaS",
        "FaaS"
    ],
    "jawaban_benar": "IaaS"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Contoh layanan SaaS adalah ...",
    "pilihan": [
        "AWS EC2",
        "Google Compute Engine",
        "Google Apps (Gmail, Docs)",
        "Windows Azure",
        "OpenShift"
    ],
    "jawaban_benar": "Google Apps (Gmail, Docs)"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Kelebihan utama menggunakan cloud computing dibandingkan on‑premise adalah ...",
    "pilihan": [
        "Biaya awal lebih rendah dan skalabilitas mudah",
        "Kontrol penuh atas data",
        "Tidak perlu koneksi internet",
        "Keamanan data terjamin mutlak",
        "Investasi hardware besar di awal"
    ],
    "jawaban_benar": "Biaya awal lebih rendah dan skalabilitas mudah"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Model deployment cloud yang digunakan secara eksklusif oleh satu organisasi disebut ...",
    "pilihan": [
        "Public cloud",
        "Private cloud",
        "Hybrid cloud",
        "Community cloud",
        "Distributed cloud"
    ],
    "jawaban_benar": "Private cloud"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Vendor utama public cloud antara lain ...",
    "pilihan": [
        "VMware, OpenStack",
        "AWS, Microsoft Azure, Google Cloud Platform",
        "Digital Ocean saja",
        "IBM Watson",
        "Oracle Database"
    ],
    "jawaban_benar": "AWS, Microsoft Azure, Google Cloud Platform"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Kemampuan cloud bursting biasanya dimiliki oleh model ...",
    "pilihan": [
        "Public cloud",
        "Private cloud",
        "Hybrid cloud",
        "On‑premise",
        "Multi‑cloud"
    ],
    "jawaban_benar": "Hybrid cloud"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Layanan penyimpanan online milik Google dengan kapasitas gratis 5GB adalah ...",
    "pilihan": [
        "Google Photos",
        "Google Drive",
        "Gmail",
        "Google Docs",
        "Google Cloud Storage"
    ],
    "jawaban_benar": "Google Drive"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Urutan tingkat pengetahuan administrasi sistem dari yang paling kompleks ke sederhana adalah ...",
    "pilihan": [
        "SaaS > PaaS > IaaS > On‑premise",
        "On‑premise > IaaS > PaaS > SaaS",
        "IaaS > PaaS > SaaS > On‑premise",
        "PaaS > IaaS > On‑premise > SaaS",
        "On‑premise > SaaS > PaaS > IaaS"
    ],
    "jawaban_benar": "On‑premise > IaaS > PaaS > SaaS"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Sistem operasi cloud buatan Microsoft untuk mengembangkan dan mengatur aplikasi adalah ...",
    "pilihan": [
        "Windows Server",
        "Microsoft 365",
        "Windows Azure",
        "SharePoint",
        "OneDrive"
    ],
    "jawaban_benar": "Windows Azure"
},

# =========================
# SHORT ANSWER (5)
# =========================

{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa kepanjangan dari IaaS?",
    "jawaban_benar": "Infrastructure as a Service"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan dua contoh layanan PaaS!",
    "jawaban_benar": "AWS Elastic Beanstalk, Heroku"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa kelemahan utama cloud computing terkait koneksi?",
    "jawaban_benar": "ketergantungan pada kualitas internet"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Model cloud mana yang menggabungkan public dan private cloud?",
    "jawaban_benar": "hybrid cloud"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa fungsi utama GitHub dalam pengembangan perangkat lunak?",
    "jawaban_benar": "repositori berbasis cloud untuk kolaborasi dan kontrol versi"
}

]

# Inisialisasi session state
if "cek_dilakukan" not in st.session_state:
    st.session_state.cek_dilakukan = False

st.title("Latihan Soal: Cloud Computing")

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