import streamlit as st

soal_list = [

# =========================
# MULTIPLE CHOICE (10)
# =========================

{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Dalam piramida otomatisasi tradisional (industri 3.0), level yang berisi perangkat seperti sensor, aktuator, motor listrik, dan sakelar adalah level ...",
    "pilihan": [
        "Level 0 – lapangan/proses produksi",
        "Level 1 – kontrol/sensing-manipulasi",
        "Level 2 – pemantauan dan pengawasan",
        "Level 3 – perencanaan manajemen operasi",
        "Level 4 – cloud"
    ],
    "jawaban_benar": "Level 0 – lapangan/proses produksi"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Apa kepanjangan dari PLC?",
    "pilihan": [
        "Programmable Logic Controller",
        "Programmable Language Computer",
        "Process Logic Control",
        "Programmable Linear Controller",
        "Process Language Code"
    ],
    "jawaban_benar": "Programmable Logic Controller"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Sistem SCADA sangat penting dalam industri karena membantu ...",
    "pilihan": [
        "Menggantikan peran MES sepenuhnya",
        "Mengontrol proses secara lokal dan remote, memantau data real-time, dan mengurangi downtime",
        "Hanya berfungsi untuk mengontrol satu mesin saja",
        "Menggantikan peran ERP",
        "Menyediakan perangkat keras saja tanpa perangkat lunak"
    ],
    "jawaban_benar": "Mengontrol proses secara lokal dan remote, memantau data real-time, dan mengurangi downtime"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Model MESA-11 yang dikembangkan pada tahun 1997 mendefinisikan berapa fungsi inti dari Manufacturing Execution System (MES)?",
    "pilihan": [
        "5",
        "7",
        "9",
        "11",
        "15"
    ],
    "jawaban_benar": "11"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Tujuan dasar menggunakan sistem ERP adalah ...",
    "pilihan": [
        "Menggantikan peran PLC",
        "Menyediakan satu pusat penyimpanan data terintegrasi, menghilangkan duplikasi, dan menjadi satu sumber kebenaran",
        "Hanya untuk mengelola keuangan perusahaan",
        "Menggantikan SCADA",
        "Mengontrol mesin produksi secara langsung"
    ],
    "jawaban_benar": "Menyediakan satu pusat penyimpanan data terintegrasi, menghilangkan duplikasi, dan menjadi satu sumber kebenaran"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Dalam transformasi menuju Industri 4.0, piramida otomatisasi mendapat tambahan level baru yaitu ...",
    "pilihan": [
        "Level 4 – big data",
        "Level 5 – cloud",
        "Level 6 – artificial intelligence",
        "Level 3 – internet",
        "Level 2 – cyber physical"
    ],
    "jawaban_benar": "Level 5 – cloud"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "OPC UA adalah protokol komunikasi yang dikembangkan oleh ...",
    "pilihan": [
        "OPC Foundation",
        "ISO",
        "IEEE",
        "IEC",
        "MESA International"
    ],
    "jawaban_benar": "OPC Foundation"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Manakah dari berikut ini yang termasuk dalam perangkat input pada PLC?",
    "pilihan": [
        "Motor starter",
        "Valve",
        "Solenoid",
        "Proximity sensor",
        "Horn & alarm"
    ],
    "jawaban_benar": "Proximity sensor"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Protokol komunikasi ringan yang menggunakan metode publish/subscribe dan biasa digunakan dalam IoT adalah ...",
    "pilihan": [
        "OPC UA",
        "MQTT",
        "HTTP",
        "FTP",
        "SMTP"
    ],
    "jawaban_benar": "MQTT"
},
{
    "tipe": "pilihan_ganda",
    "pertanyaan": "Integrasi horizontal dalam Industri 4.0 terjadi di beberapa tingkatan, yaitu ...",
    "pilihan": [
        "Di lantai produksi, antar fasilitas, dan di seluruh rantai pasokan",
        "Hanya di lantai produksi",
        "Hanya antar perusahaan",
        "Hanya di tingkat cloud",
        "Hanya di tingkat ERP"
    ],
    "jawaban_benar": "Di lantai produksi, antar fasilitas, dan di seluruh rantai pasokan"
},

# =========================
# SHORT ANSWER (5)
# =========================

{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa kepanjangan dari SCADA?",
    "jawaban_benar": "Supervisory Control and Data Acquisition"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan salah satu keuntungan menggunakan ERP open source dibandingkan komersial!",
    "jawaban_benar": "biaya murah/tidak ada lisensi"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Apa fungsi utama dari HMI dalam sistem otomatisasi?",
    "jawaban_benar": "antarmuka manusia-mesin untuk memodelkan dan mengontrol sistem"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Dalam integrasi vertikal Industri 4.0, data mengalir secara bebas antara lapisan lapangan hingga ke bagian apa saja? (Sebutkan satu contoh)",
    "jawaban_benar": "R&D, jaminan kualitas, manajemen produk, TI, penjualan, pemasaran, logistik"
},
{
    "tipe": "isian_singkat",
    "pertanyaan": "Sebutkan salah satu alasan utama OPC UA terus diadopsi dalam industri manufaktur!",
    "jawaban_benar": "mendukung smart manufacturing / mengurangi kompleksitas komunikasi / mengakomodasi sistem lama / lintas platform / non-proprietary / multi-sumber data"
}

]

# Inisialisasi session state untuk menyimpan status koreksi
if "cek_dilakukan" not in st.session_state:
    st.session_state.cek_dilakukan = False

st.title("Latihan Soal: Sistem Integrasi Vertikal dan Horizontal")

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