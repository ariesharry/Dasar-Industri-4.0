import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
st.markdown(
    """
    <style>
    /* Target container utama di kolom pertama */
    .stColumn:first-child > div:first-child {
        background-color: #C7DBFF;   /* pink muda */
        border-radius: 20px;
        padding: 20px;
        
    }
    .stColumn:first-child .stContainer {
        background-color: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)

cols = st.columns([0.7, 0.3])

# ================== KOLOM MATERI UTAMA ==================
with cols[0].container(border=True):
    st.title("Klasifikasi Robot")

    # Bagian 1: Pengantar
    with st.container(border=True):
        st.markdown(
            """
            Pemanfaatan robot menjadi solusi karena dapat dioperasikan terus menerus, 
            fleksibel diprogram, handal dibanding manusia, dan dapat dihubungkan dengan 
            perangkat kendali lain seperti PLC, komputer, dll. Tingkat kerumitan, beban, 
            dan kepresisian kerja robot menentukan bentuk dan tipe lengan robot.
            """
        )

    # Bagian 2: Robot Stasioner
    with st.container(border=True):
        st.markdown(
            """
            ### 🏗️ Robot Stasioner
            Robot yang dipasang tetap di suatu tempat, umumnya digunakan di industri manufaktur.
            """
        )

        # Sub‑bagian dengan kolom untuk efisiensi ruang
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(
                """
                **a. Cartesian/Gantry Robot**  
                Lengan tiga sendi prismatik, sumbu bertepatan dengan koordinat Cartesian.  
                *Aplikasi:* pick and place, sealant, perakitan, penanganan mesin, las busur.

                **b. Cylindrical Robot**  
                Membentuk silinder sistem koordinat.  
                *Aplikasi:* perakitan, penanganan mesin, las titik, die‑casting.

                **c. SCARA Robot**  
                Dua atau lebih joint revolusi + satu prismatik. Cepat dan presisi untuk perakitan horizontal.  
                *Aplikasi:* pemindah barang kecepatan tinggi.
                """
            )
        with col_b:
            st.markdown(
                """
                **d. Articulated Robot (Robot Arm)**  
                Pergerakan kompleks mirip lengan manusia, fleksibilitas tinggi.  
                *Aplikasi:* perakitan, die‑casting, fettling, las busur, lukis semprot.

                **e. Parallel Robot**  
                Kaku, mampu menopang beban besar.  
                *Aplikasi:* material handling beban berat.
                """
            )

    # Bagian 3: Robot Beroda
    with st.container(border=True):
        st.markdown(
            """
            ### 🚗 Robot Beroda (Mobile Robot)
            Robot yang bergerak dengan roda, diklasifikasikan berdasarkan jumlah roda.
            """
        )
        col_c, col_d = st.columns(2)
        with col_c:
            st.markdown(
                """
                **a. Single Wheel (Ball) Robot**  
                Satu roda tunggal, bisa bergerak langsung ke segala arah.  
                *Contoh:* robot resepsionis di satu lantai.

                **b. Two‑Wheel Robot**  
                Dua roda kiri‑kanan, dapat berputar di tempat (motor berlawanan arah).  
                *Contoh:* gardan belakang mobil, mainan RC.
                """
            )
        with col_d:
            st.markdown(
                """
                **c. Three and More Wheel Robot**  
                Tiga roda atau lebih. Dua roda poros digerakkan motor, satu roda sebagai kemudi.  
                *Contoh:* becak, bajaj.
                """
            )

    # Bagian 4: Drone
    with st.container(border=True):
        st.markdown(
            """
            ### 🛸 Drone (Unmanned Aerial Vehicle)
            Inovasi teknologi yang awalnya untuk militer, kini populer untuk kamera dan fotografi.
            Drone termasuk robot bergerak di udara.
            """
        )

    # Gambar III.2
    with st.container(border=True):
        scol1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-3/fig2.png", use_container_width=True)
        st.caption("Gambar III.2 – Berbagai jenis robot (1)")

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Klasifikasi Berdasarkan Penggerak", expanded=True):
        st.markdown(
            """
            - **Robot Stasioner**: Dipasang tetap, untuk industri.  
            - **Robot Beroda**: Bergerak dengan roda.  
            - **Drone**: Robot terbang.
            """
        )

    with st.expander("🏗️ Robot Stasioner"):
        st.markdown(
            """
            - Cartesian, Cylindrical, SCARA, Articulated, Parallel.  
            - Masing-masing punya aplikasi spesifik (pick and place, perakitan, las, dll).
            """
        )

    with st.expander("🚗 Robot Beroda"):
        st.markdown(
            """
            - Single wheel: manuver segala arah.  
            - Two‑wheel: bisa berputar di tempat.  
            - Three+ wheel: seperti becak, satu roda kemudi.
            """
        )

    with st.expander("🛸 Drone"):
        st.markdown(
            """
            - Awal militer, kini untuk fotografi, pengiriman, dll.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Kategori Utama", "Stasioner, Beroda, Drone")
        st.metric("Jenis Stasioner", "5 jenis")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Materi kuliah robotika  
            - Sumber industri otomasi
            """
        )