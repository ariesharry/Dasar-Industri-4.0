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
    st.markdown(
        """
        <h1 style='text-align: center;'>📘 BAB 2</h1>
        """,
        unsafe_allow_html=True
    )

    # Container isi
    with st.container(border=True):
        st.markdown(
            """
            
            ### 🎯 Capaian Pembelajaran
            
            Mahasiswa mampu memahami pengetahuan tentang:
            
            1. **Internet of Things (IoT)**, **Industrial Internet of Things (IIoT)**, 
            dan **Internet of Services (IoS)**  
            
            2. **Cyber Physical System (CPS)** dan konsep **digital/smart manufacturing**  
            """
        )
    st.title("Sejarah Internet of Things")

    # Bagian 1: Pengertian dan Dampak IoT
    with st.container(border=True):
        st.markdown(
            """
            **Internet of Things (IoT)** telah menjadi salah satu konsep bisnis industri yang 
            paling banyak dibicarakan dalam beberapa tahun terakhir. Konsep ini dipercaya 
            mempengaruhi kinerja bisnis suatu organisasi. Fenomena IoT adalah salah satu 
            teknologi *disruptive* yang mengubah cara kerja organisasi dalam menjalankan bisnis.

            Pada saat ini, kita berada di awal era di mana komunikasi dan konektivitas terjadi 
            di mana‑mana bukanlah suatu mimpi atau tantangan lagi. Fokusnya telah bergeser ke 
            arah integrasi manusia dan perangkat tanpa batas untuk menyatukan dunia fisik dengan 
            lingkungan virtual buatan manusia, menciptakan apa yang disebut **Internet of Things (IoT)**.
            """
        )
    
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
                        src="https://www.youtube.com/embed/n-f8B76Hozk"
                        title="YouTube video"
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen>
                    </iframe>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Bagian 2: Contoh Aplikasi IoT (Gojek, Qlue, LinkAja)
    with st.container(border=True):
        st.markdown(
            """
            ### 📱 Contoh Penerapan IoT

            **Gojek** – Aplikasi yang memanjakan pelanggan untuk memilih layanan secara online. 
            Layanan yang ditawarkan meliputi:
            - Kebutuhan sehari-hari: GoFood, GoDaily, GoLaundry, GoAuto, GoMed
            - Hiburan & gaya hidup: GoMassage, GoClean, GoFix, GoGlam, GoTix
            - Pembayaran: GoPulsa, GoPoints, GoNearby, GoBills, GoGive, GoSure
            - Belanja: GoShop, GoMart, GoMall
            - Transportasi & logistik: GoRide, GoCar, GoBluebird, GoSend, GoBox

            Sebagai contoh, pelanggan dapat memesan makanan/minuman via **GoFood** dan pesanan 
            akan segera dikirim ke lokasi pelanggan.
            """
        )
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-2/fig1.png", use_container_width=True)
        st.caption("Gambar II.1 – Contoh IoT : Aplikasi GoJek (Sumber: saisa.eu)")

        st.markdown(
            """
            **Jakarta Smart City (Qlue)** – Platform bagi warga untuk menyampaikan keluhan 
            (pelanggaran lalu lintas, kerusakan fasilitas umum, sampah, banjir, dll.) 
            diluncurkan tahun 2015.

            **LinkAja (Telkomsel)** – Aplikasi untuk layanan pembayaran, pembelian pulsa, 
            tagihan, tiket, kartu elektronik, keuangan, hiburan, pajak, dan layanan berbagi.
            """
        )

    # Bagian 3: Sejarah IoT dan Evolusi
    with st.container(border=True):
        st.markdown(
            """
            ### 📜 Sejarah dan Evolusi IoT

            Pada awal 2000-an, **Kevin Ashton** – pelopor gagasan IoT dari MIT's AutoID Lab – 
            saat bekerja di Proctor & Gamble (P&G) mencari cara menghubungkan informasi RFID 
            ke Internet untuk meningkatkan bisnis. Konsepnya sederhana: semua objek sehari‑hari 
            dilengkapi pengidentifikasi dan konektivitas nirkabel, sehingga dapat berkomunikasi 
            satu sama lain dan dikelola oleh komputer (www.cisco.com).

            **Evolusi IoT** dimulai dari Pra‑Internet hingga IoT seperti digambarkan berikut.
            """
        )
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-2/fig2.png", use_container_width=True)
        st.caption("Gambar II.2 – Evolusi Internet of Things (Sumber: diadaptasi dari cisco.com)")

        # Rincian evolusi dalam tabel agar lebih informatif
        evolusi_data = {
            "Era": ["Pra Internet", "Internet Konten", "Internet Layanan", "Internet Orang", "Internet of Things"],
            "Komunikasi": ["Manusia ke Manusia", "Manusia ke Konten", "Manusia ke Layanan", "Manusia ke Manusia (real‑time)", "Mesin ke Mesin"],
            "Contoh Teknologi": ["Telepon, SMS", "WWW, Email", "Web 2.0, E‑Commerce", "Facebook, Twitter, Skype", "RFID, Sensor, IoT"]
        }
        df_evolusi = pd.DataFrame(evolusi_data)
        st.table(df_evolusi)

        st.markdown(
            """
            **Penjelasan singkat:**
            - **Pra Internet**: komunikasi manusia ke manusia via telepon/SMS.
            - **Internet Konten**: lahirnya World Wide Web, email, pesan.
            - **Internet Layanan**: Web 2.0 melahirkan E‑Commerce, E‑produktivitas.
            - **Internet Orang**: koneksi real‑time antar manusia melalui media sosial.
            - **Internet of Things**: era komunikasi mesin ke mesin.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi IoT", expanded=True):
        st.markdown(
            """
            - Konsep integrasi dunia fisik dan virtual melalui konektivitas di mana‑mana.
            - Teknologi disruptif yang mengubah model bisnis.
            """
        )

    with st.expander("🌍 Contoh Implementasi IoT"):
        st.markdown(
            """
            - **Gojek**: super‑app dengan layanan on‑demand (transportasi, pesan antar, pembayaran).
            - **Qlue** (Jakarta Smart City): pelaporan warga untuk masalah kota.
            - **LinkAja**: dompet digital dan layanan telekomunikasi.
            """
        )

    with st.expander("🧑‍💻 Tokoh Penting"):
        st.markdown(
            """
            **Kevin Ashton** – Pelopor IoT dari MIT AutoID Lab. Mencetuskan ide menghubungkan 
            objek fisik (RFID) ke internet untuk efisiensi bisnis.
            """
        )

    with st.expander("📈 Evolusi IoT"):
        st.markdown(
            """
            1. **Pra Internet** (manusia ke manusia)  
            2. **Internet Konten** (WWW, email)  
            3. **Internet Layanan** (Web 2.0, e‑commerce)  
            4. **Internet Orang** (media sosial real‑time)  
            5. **Internet of Things** (mesin ke mesin)
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Pencetus IoT", "Kevin Ashton (2000-an)")
        st.metric("Contoh Awal", "RFID untuk P&G")
        st.metric("Era Saat Ini", "IoT / Mesin ke Mesin")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - www.cisco.com  
            - https://saisa.eu/blogs/Guidance/?p=1539  
            - Kevin Ashton, MIT AutoID Lab
            """
        )