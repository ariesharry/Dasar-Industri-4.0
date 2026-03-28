import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
st.markdown(
    """
    <style>
    /* Target container utama di kolom pertama */
    .stColumn:first-child > div:first-child {
        background-color: #caf0f8;   /* pink muda */
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
    st.title("Robot Otonom")

    # Bagian 1: Pengantar Robot Otonom
    with st.container(border=True):
        st.markdown(
            """
            Dengan terus berkembangnya teknologi dan ditemukannya internet, menjadi dasar 
            terbukanya gerbang menuju **revolusi industri 4.0**. Robot menjadi salah satu 
            teknologi kunci yang terus berkembang dengan tidak hanya mengedepankan prinsip 
            kecepatan, tetapi juga ketepatan. Hal tersebut mendasari tercetusnya konsep 
            **robot otonom**.
            """
        )

    # Bagian 2: Definisi dan Cara Kerja
    with st.container(border=True):
        st.markdown(
            """
            ### 🤖 Definisi Robot Otonom

            **Robot otonom** adalah robot yang bekerja mandiri tanpa harus dikontrol langsung 
            oleh manusia. Robot ini terdiri atas kumpulan sistem yang saling bekerja sama, 
            di mana tiap-tiap bagian dapat saling berkomunikasi.

            **Cara kerja:**
            - Robot otonom menggunakan **komputer pusat** untuk memproses data yang diterima oleh sensor.
            - Dengan menggunakan algoritma yang berbeda-beda, komputer menentukan tindakan yang harus diambil.
            - Komputer pusat kemudian memerintahkan sistem untuk melakukan tindakan yang sesuai.

            Robot otonom dirancang untuk **menangani lingkungannya sendiri** dan bekerja untuk 
            waktu yang lama tanpa campur tangan manusia. Mereka memiliki fitur-fitur canggih 
            untuk memahami lingkungan fisik dan mengotomatisasi tugas-tugas yang sebelumnya 
            dilakukan manual.
            """
        )

    # Gambar III.1
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-3/fig1.png", use_container_width=True)
        st.caption(
            "Gambar III.1 – Robotic Scrubber Drier yang Bisa Dioperasikan secara Otonom di Terminal 3 Bandara Soekarno-Hatta "
            "(Sumber: tribunnews.com)"
        )

    # Bagian 3: Perbandingan dengan AGV
    with st.container(border=True):
        st.markdown(
            """
            ### 🔄 Perbandingan Autonomous Robot vs AGV

            **Autonomous Robot** memiliki keunggulan besar dalam fleksibilitas, kompatibilitas, 
            dan kontrol dibandingkan dengan **AGV (Automated Guided Vehicle)**.
            """
        )

        # Tabel perbandingan
        perbandingan_data = {
            "Aspek": ["Navigasi", "Maneuver", "Perubahan Infrastruktur", "Jalur"],
            "AGV": [
                "Membutuhkan 'track' (magnetic tape/kabel di lantai)",
                "Tidak dapat bermanuver di sekitar rintangan",
                "Memerlukan perubahan fisik untuk memperluas/memodifikasi jalur",
                "Jalur tetap"
            ],
            "Autonomous Robot": [
                "Navigasi otonom tanpa 'track'",
                "Dapat melakukan perjalanan aman di sekitar orang dan rintangan",
                "Tidak memerlukan perubahan infrastruktur",
                "Menavigasi secara dinamis menggunakan peta fasilitas"
            ]
        }
        df_perbandingan = pd.DataFrame(perbandingan_data)
        st.table(df_perbandingan)
    
    with st.container():
        # Buat 3 kolom untuk center (kiri - tengah - kanan)
        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])

        with col2:
            # Embed video
            st.markdown(
                """
                <div style="
                    border-radius: 10px;
                    overflow: hidden;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                    margin-bottom: 30px;
                ">
                    <iframe 
                        width="100%" 
                        height="400" 
                        src="https://www.youtube.com/embed/8V2rdl9I_zk"
                        title="YouTube video"
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen>
                    </iframe>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Bagian 4: Contoh Penggunaan
    with st.container(border=True):
        st.markdown(
            """
            ### 🏭 Contoh Penggunaan Robot Otonom

            - **Robot pengiriman** yang dapat menggunakan lift dan bergerak di seluruh gedung bertingkat.
            - **Robot pembersih** seperti Robotic Scrubber Drier di bandara.
            - Robot yang bekerja di lingkungan industri, gudang, dan rumah sakit.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi Robot Otonom", expanded=True):
        st.markdown(
            """
            - Robot yang bekerja **mandiri** tanpa kontrol langsung manusia.
            - Menggunakan **komputer pusat** dan sensor untuk memproses data.
            - Bekerja dalam waktu lama tanpa intervensi manusia.
            """
        )

    with st.expander("⚙️ Cara Kerja"):
        st.markdown(
            """
            1. Sensor mengumpulkan data lingkungan.
            2. Komputer pusat memproses data dengan algoritma.
            3. Komputer memerintahkan aktuator untuk bertindak.
            """
        )

    with st.expander("🆚 Perbandingan dengan AGV"):
        st.markdown(
            """
            **AGV**:
            - Butuh track magnetik/kabel
            - Tidak bisa hindari rintangan
            - Perlu perubahan infrastruktur
            - Jalur tetap

            **Autonomous Robot**:
            - Navigasi otonom
            - Bisa hindari rintangan & orang
            - Tanpa perubahan infrastruktur
            - Navigasi dinamis dengan peta
            """
        )

    with st.expander("🏢 Contoh Aplikasi"):
        st.markdown(
            """
            - Robot pembersih di bandara
            - Robot pengiriman di gedung
            - Robot industri dan logistik
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Komponen Utama", "Sensor, Komputer Pusat, Aktuator")
        st.metric("Keunggulan vs AGV", "Fleksibel, Dinamis, Tanpa Track")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - tribunnews.com (gambar robot pembersih)
            - Materi kuliah robotika dan industri 4.0
            """
        )