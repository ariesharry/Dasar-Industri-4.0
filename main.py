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
            {"file": "pages/bab_1/b1_2.py", "title": "1.2 Karakteristik Industri 4.0"},
            {"file": "pages/bab_1/b1_3.py", "title": "1.3 Manfaat Industri 4.0"},
        ]
    },
    {
        "title": "Bab 2: Internet of Things (IoT)",
        "pages": [
            {"file": "pages/bab_2/b2_1.py", "title": "Bab 2 - 2.1 Definisi Internet of Things"},
            {"file": "pages/bab_2/b2_2.py", "title": "Bab 2 - 2.2 Klasifikasi Internet of Things"},
            {"file": "pages/bab_2/b2_3.py", "title": "Bab 2 - 2.3 Karakteristik Internet of Things"},
        ]
    },
    {
        "title": "Bab 3: Robot Otonom",
        "pages": [
            {"file": "pages/bab_3/b3_1.py", "title": "3.1 Definisi Robot Otonom"},
            {"file": "pages/bab_3/b3_2.py", "title": "3.2 Klasifikasi Robot Otonom"},
            {"file": "pages/bab_3/b3_3.py", "title": "3.3 Aplikasi Robot Otonom"},
        ]
    },
    {
        "title": "Bab 4: Sistem Integrasi Vertikal & Horizontal",
        "pages": [
            {"file": "pages/bab_4/b4_1.py", "title": "Bab 4 - 4.1 Definisi Sistem Integrasi Vertikal dan Horizontal"},
            {"file": "pages/bab_4/b4_2.py", "title": "Bab 4 - 4.2 Teknologi Integrasi dan Otomatisasi"},
            {"file": "pages/bab_4/b4_3.py", "title": "Bab 4 - 4.3 Sistem Komunikasi dalam Otomatisasi Industri"},
        ]
    },
    {
        "title": "Bab 5: Cloud Computing",
        "pages": [
            {"file": "pages/bab_5/b5_1.py", "title": "5.1 Definisi Sistem Integrasi Vertikal dan Horizontal"},
            {"file": "pages/bab_5/b5_2.py", "title": "5.2 Teknologi Integrasi dan Otomatisasi"},
            {"file": "pages/bab_5/b5_3.py", "title": "5.3 Sistem Komunikasi dalam Otomatisasi Industri"},
        ]
    },
    {
        "title": "Bab 6: Big Data Analytic",
        "pages": [
            {"file": "pages/bab_6/b6_1.py", "title": "6.1 Definisi Robot Otonom"},
            {"file": "pages/bab_6/b6_2.py", "title": "6.2 Klasifikasi Robot Otonom"},
            {"file": "pages/bab_6/b6_3.py", "title": "6.3 Aplikasi Robot Otonom"},
        ]
    },
        {
        "title": "Bab 7: Simulasi",
        "pages": [
            {"file": "pages/bab_7/b7_1.py", "title": "7.1 Definisi Robot Otonom"},
            {"file": "pages/bab_7/b7_2.py", "title": "7.2 Klasifikasi Robot Otonom"},
            {"file": "pages/bab_7/b7_3.py", "title": "7.3 Aplikasi Robot Otonom"},
        ]
    },
    {
        "title": "Bab 8: Artificial Intelligence",
        "pages": [
            {"file": "pages/bab_8/b8_1.py", "title": "8.1 Definisi Robot Otonom"},
            {"file": "pages/bab_8/b8_2.py", "title": "8.2 Klasifikasi Robot Otonom"},
            {"file": "pages/bab_8/b8_3.py", "title": "8.3 Aplikasi Robot Otonom"},
        ]
    },
        {
        "title": "Bab 9: Cyber Security",
        "pages": [
            {"file": "pages/bab_9/b9_1.py", "title": "9.1 Definisi Robot Otonom"},
            {"file": "pages/bab_9/b9_2.py", "title": "9.2 Klasifikasi Robot Otonom"},
            {"file": "pages/bab_9/b9_3.py", "title": "9.3 Aplikasi Robot Otonom"},
        ]
    },
            {
        "title": "Bab 10: Additive Manufacture",
        "pages": [
            {"file": "pages/bab_10/b10_1.py", "title": "10.1 Definisi Robot Otonom"},
            {"file": "pages/bab_10/b10_2.py", "title": "10.2 Klasifikasi Robot Otonom"},
            {"file": "pages/bab_10/b10_3.py", "title": "10.3 Aplikasi Robot Otonom"},
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