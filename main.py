import streamlit as st

st.logo("assets/logo.png", size="large")

# Kemudian gunakan CSS untuk mengubah ukuran gambar logo secara spesifik
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 150px;   /* sesuaikan ukuran */
        height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="E-Modul Interaktif - Dasar Industri 4.0",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# 1. HALAMAN COVER & DASHBOARD (tetap manual karena icon khusus)
# =========================
cover = st.Page("pages/cover.py", title="Cover", icon=":material/home:")

# =========================
# 2. DATA SEMUA BAB DAN HALAMAN MATERI
# =========================
# Format: setiap bab punya judul dan daftar halaman
# Setiap halaman didefinisikan dengan path file dan judul
bab_list = [
    {
        "title": "Bab 1: Pengantar Industri 4.0",
        "pages": [
            {"file": "pages/bab_1/b1_1.py", "title": "1.1 Definisi Industri 4.0"},
            {"file": "pages/bab_1/b1_2.py", "title": "1.2 Model Arsitektur Industri 4.0"},
            {"file": "pages/bab_1/b1_3.py", "title": "1.3 Karakteristik Industri 4.0"},
            {"file": "pages/bab_1/b1_4.py", "title": "1.4 Prinsip Desain Industri 4.0 "},
            {"file": "pages/bab_1/b1_5.py", "title": "1.5 Manfaat Industri 4.0"},
            {"file": "pages/bab_1/b1_6.py", "title": "1.6 Making Indonesia 4.0"},
            {"file": "pages/bab_1/b1_7.py", "title": "Latihan Soal"},
        ]
    },
    {
        "title": "Bab 2: Internet of Things (IoT)",
        "pages": [
            {"file": "pages/bab_2/b2_1.py", "title": "2.1 Sejarah Internet of Things"},
            {"file": "pages/bab_2/b2_2.py", "title": "2.2 Definisi, konsep, dan pilar Internet of Things"},
            {"file": "pages/bab_2/b2_3.py", "title": "2.3 Machine to Machine (M2M) dan Internet of Things (IoT)"},
            {"file": "pages/bab_2/b2_4.py", "title": "2.4 Karakteristik Internet of Things"},
            {"file": "pages/bab_2/b2_5.py", "title": "2.5 Klasifikasi Internet of Things"},
            {"file": "pages/bab_2/b2_6.py", "title": "2.6 Arsitektur Internet of Things"},
            {"file": "pages/bab_2/b2_7.py", "title": "2.7 Cyber Physical System (CPS)"},
            {"file": "pages/bab_2/b2_8.py", "title": "2.8 Identifikasi dan Pengambilan Data Otomatis (AIDC)"},
            {"file": "pages/bab_2/b2_9.py", "title": "2.9 Augmented Reality (AR) dan Virtual Reality (VR)"},
            {"file": "pages/bab_2/b2_10.py", "title": "Simulasi"},
            {"file": "pages/bab_2/b2_11.py", "title": "Latihan Soal"},
        ]
    },
    {
        "title": "Bab 3: Robot Otonom",
        "pages": [
            {"file": "pages/bab_3/b3_1.py", "title": "3.1 Robot Otonom"},
            {"file": "pages/bab_3/b3_2.py", "title": "3.2 Definisi Robot"},
            {"file": "pages/bab_3/b3_3.py", "title": "3.3 Klasifikasi Robot"},
            {"file": "pages/bab_3/b3_4.py", "title": "3.4 Otomatisasi dan Klasifikasinya"},
            {"file": "pages/bab_3/b3_5.py", "title": "3.5 Aplikasi Robot Otonom"},
            {"file": "pages/bab_3/b3_6.py", "title": "3.6 Simulasi"},
            {"file": "pages/bab_3/b3_7.py", "title": "3.7 Latihan Soal"},
        ]
    },
    {
        "title": "Bab 4: Sistem Integrasi Vertikal & Horizontal",
        "pages": [
            {"file": "pages/bab_4/b4_1.py", "title": "4.1 Piramida Otomatisasi "},
            {"file": "pages/bab_4/b4_2.py", "title": "4.2 Programmable Logic Controller (PLC) dan perangkat pendukung lainnya"},
            {"file": "pages/bab_4/b4_3.py", "title": "4.3 Supervisory Control and Data Acquisition (SCADA)"},
            {"file": "pages/bab_4/b4_4.py", "title": "4.4 Manufacturing Execution System (MES)"},
            {"file": "pages/bab_4/b4_5.py", "title": "4.5 Enterprise Resource Planning (ERP)"},
            {"file": "pages/bab_4/b4_6.py", "title": "4.6 Cyber Physical Systems (CPS) based Automation"},
            {"file": "pages/bab_4/b4_7.py", "title": "4.7 Open Protocol Communication Unified Architecture (OPC-UA)"},
            {"file": "pages/bab_4/b4_8.py", "title": "Simulasi"},
            {"file": "pages/bab_4/b4_9.py", "title": "Latihan Soal"},
        ]
    },
    {
        "title": "Bab 5: Cloud Computing",
        "pages": [
            {"file": "pages/bab_5/b5_1.py", "title": "5.1 Definisi Komputasi Awan"},
            {"file": "pages/bab_5/b5_2.py", "title": "5.2 Layanan Komputasi Awan"},
            {"file": "pages/bab_5/b5_3.py", "title": "5.3 Cloud Computing Deployment Model"},
            {"file": "pages/bab_5/b5_4.py", "title": "Simulasi Interaktif"},
            {"file": "pages/bab_5/b5_5.py", "title": "Latihan Soal"},
        ]
    },
    {
        "title": "Bab 6: Big Data Analytic",
        "pages": [
            {"file": "pages/bab_6/b6_1.py", "title": "6.1 Pengertian, karakteristik dan manfaat big data"},
            {"file": "pages/bab_6/b6_2.py", "title": "6.2 Structured Data dan Unstructured Data"},
            {"file": "pages/bab_6/b6_3.py", "title": "6.3 Historian Data, Real Time Database dan Data Lake"},
            {"file": "pages/bab_6/b6_4.py", "title": "6.4 Data Warehouse, Data Mart, dan Data Mining"},
            {"file": "pages/bab_6/b6_5.py", "title": "6.5 Data Science"},
            {"file": "pages/bab_6/b6_6.py", "title": "6.6 Business Intelligence, Data Visualization, dan Intelligent Dashboard"},
            {"file": "pages/bab_6/b6_7.py", "title": "6.7 Advanced Analytics (Algorithm, Regression, Decision Trees, Time Series Analysis)"},
            {"file": "pages/bab_6/b6_8.py", "title": "6.8 Tingkatan Analisis"},
            {"file": "pages/bab_6/b6_9.py", "title": "Simulasi Interaktif"},
            {"file": "pages/bab_6/b6_10.py", "title": "Latihan Soal"},
        ]
    },
        {
        "title": "Bab 7: Simulasi",
        "pages": [
            {"file": "pages/bab_7/b7_1.py", "title": "7.1 Pengertian dan Tujuan Simulasi"},
            {"file": "pages/bab_7/b7_2.py", "title": "7.2 Jenis-Jenis Simulasi"},
            {"file": "pages/bab_7/b7_3.py", "title": "7.3 Simulasi dalam Industri 4.0"},
            {"file": "pages/bab_7/b7_4.py", "title": "7.3 Digital Twin"},
            {"file": "pages/bab_7/b7_5.py", "title": "Simulasi Interaktif"},
            {"file": "pages/bab_7/b7_6.py", "title": "Latihan Soal"},
        ]
    },
    {
        "title": "Bab 8: Artificial Intelligence",
        "pages": [
            {"file": "pages/bab_8/b8_1.py", "title": "8.1 Sejarah dan Definisi Kecerdasan Buatan"},
            {"file": "pages/bab_8/b8_2.py", "title": "8.2 Klasifikasi Dan Mekanisme Kerja Kecerdasan Buatan"},
            {"file": "pages/bab_8/b8_3.py", "title": "8.3 Pembelajaran Mesin (Machine Learning)"},
            {"file": "pages/bab_8/b8_4.py", "title": "8.3 Deep Learning (DL)"},
            {"file": "pages/bab_8/b8_5.py", "title": "8.3 Perbedaan AI, ML, DL"},
            {"file": "pages/bab_8/b8_6.py", "title": "8.3 Aplikasi AI pada Industri"},
            {"file": "pages/bab_8/b8_7.py", "title": "Simulasi Interaktif"},
            {"file": "pages/bab_8/b8_8.py", "title": "Latihan Soal"},
        ]
    },
        {
        "title": "Bab 9: Cyber Security",
        "pages": [
            {"file": "pages/bab_9/b9_1.py", "title": "9.1 Definisi Robot Otonom"},
            {"file": "pages/bab_9/b9_2.py", "title": "9.2 Klasifikasi Robot Otonom"},
            {"file": "pages/bab_9/b9_3.py", "title": "9.3 Aplikasi Robot Otonom"},
            {"file": "pages/bab_9/b9_4.py", "title": "9.3 Aplikasi Robot Otonom"},
        ]
    },
            {
        "title": "Bab 10: Additive Manufacture",
        "pages": [
            {"file": "pages/bab_10/b10_1.py", "title": "10.1 Definisi manufaktur aditif"},
            {"file": "pages/bab_10/b10_2.py", "title": "10.2 Prinsip kerja manufaktur aditif"},
            {"file": "pages/bab_10/b10_3.py", "title": "10.3 Teknologi manufaktur aditif"},
            {"file": "pages/bab_10/b10_4.py", "title": "10.3 Kelebihan dan kekurangan teknologi manufaktur aditif"},
            {"file": "pages/bab_10/b10_5.py", "title": "10.3 Aplikasi manufaktur aditif"},
            {"file": "pages/bab_10/b10_6.py", "title": "Simulasi Interaktif"},
            {"file": "pages/bab_10/b10_7.py", "title": "Latihan Soal"},
        ]
    },
    
    # === TAMBAHKAN BAB BARU DI SINI ===
    # {
    #     "title": "Bab 5: Contoh Bab Baru",
    #     "pages": [
    #         {"file": "pages/bab_5/b5_1.py", "title": "Bab 5 - 5.1 Subbab 1"},
    #         {"file": "pages/bab_5/b5_2.py", "title": "Bab 5 - 5.2 Subbab 2"},
    #     ]
    # },
]

# =========================
# 3. GENERATE OBJEK st.Page UNTUK SEMUA HALAMAN MATERI
# =========================
pages_per_bab = []      # list of lists: menyimpan objek Page per bab (untuk sidebar)
all_materi_pages = []   # flat list semua halaman materi (untuk st.navigation)

for bab in bab_list:
    bab_pages = []
    for page_info in bab["pages"]:
        # Buat objek Page (tanpa icon, sesuai kode awal)
        page_obj = st.Page(page_info["file"], title=page_info["title"])
        bab_pages.append(page_obj)
        all_materi_pages.append(page_obj)
    pages_per_bab.append(bab_pages)

# =========================
# 4. Siapkan NAVIGATION (HIDDEN MODE)
# =========================
contents = {
    "": [cover],               # Halaman tanpa section
    "_materi": all_materi_pages,          # Semua materi dalam satu section
}

pg = st.navigation(contents, position="hidden")

# =========================
# 5. SIDEBAR CUSTOM MENU
# =========================
with st.sidebar:
    st.page_link(cover, label="Cover", icon=":material/home:")

    st.markdown("## :material/menu: Table of Contents")

    # Loop untuk membuat expander per bab
    for i, bab in enumerate(bab_list):
        # expanded hanya untuk bab pertama
        with st.expander(bab["title"], expanded=(i == 0)):
            for page_obj in pages_per_bab[i]:
                st.page_link(page_obj)

    
# =========================
# 6. RUN PAGE
# =========================
pg.run()

import streamlit as st
import base64

def get_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("assets/logo-bottom.png")

st.sidebar.markdown(f"""
<style>
.bottom-logo {{
    position: fixed;
    bottom: 0px;
    width: 270px;
    background-color: #FBEFEF;
}}
</style>

<div class="bottom-logo">
    <img src="data:image/png;base64,{img}" width="240">
</div>
""", unsafe_allow_html=True)