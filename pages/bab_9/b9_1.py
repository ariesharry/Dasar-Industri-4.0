import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
st.markdown(
    """
    <style>
    .stColumn:first-child > div:first-child {
        background-color: #caf0f8;
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
    st.title("Jenis Ancaman Siber")

    # Pengantar Cybersecurity
    with st.container(border=True):
        st.markdown(
            """
            **Cybersecurity** merupakan teknologi, proses dan praktik yang dirancang untuk melindungi kekayaan intelektual organisasi, data pelanggan, dan informasi sensitif lainnya dari akses tidak sah oleh penjahat cyber. Frekuensi dan tingkat keparahan kejahatan dunia maya terus meningkat dan ada kebutuhan yang signifikan untuk peningkatan manajemen risiko keamanan siber sebagai bagian dari profil risiko perusahaan setiap organisasi.

            Dalam era milenium ini, pengertian cybersecurity lebih banyak membahas tentang bagaimana melindungi orang dan organisasi dari ancaman tradisional seperti malware, serangan rekayasa sosial, perusakan situs web (website defacing), peretasan (hacktivism), dll. Beberapa tahun terakhir dapat kita saksikan bahwa telah terjadi peningkatan kecanggihan dan intensitas serangan dunia maya, yang sekarang berorientasi pada kejahatan keuangan, spionase industri, dan bahkan menargetkan pemerintah dan infrastruktur kritis dari waktu ke waktu.
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
                        src="https://www.youtube.com/embed/shQEXpUwaIY"
                        title="YouTube video"
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen>
                    </iframe>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Information Security dan CIA Triangle
    with st.container(border=True):
        st.markdown(
            """
            ### Information Security dan Segitiga CIA

            Information Security atau keamanan sistem informasi adalah perlindungan informasi dan elemen-elemennya termasuk sistem dan perangkat kerasnya. Jika dihubungkan dengan goal dari information security, yaitu confidentiality, integrity dan availability (dikenal dengan segitiga CIA), maka information security adalah sebuah perlindungan informasi dari confidentiality, integrity dan availability pada saat informasi tersebut sedang diproses, ditransmisikan, ataupun dalam penyimpanannya.

            **Segitiga CIA:**
            1. **Confidentiality** – proses untuk mengamankan dan memastikan bahwa hanya orang yang berhak saja yang dapat mengakses informasi tertentu. Informasi ini berkaitan dengan data personal dan bersifat rahasia.
            2. **Integrity** – jaminan bahwa semua data tersedia dalam keadaan utuh dan lengkap sesuai apa adanya, serta tidak dapat dimodifikasi oleh orang yang tidak berhak.
            3. **Availability** – usaha supaya data akan dapat diakses setiap saat, tanpa delay, dan tersedia dengan utuh tanpa cacat.
            """
        )

    # Mengapa Information Security diperlukan?
    with st.container(border=True):
        st.markdown(
            """
            ### Mengapa Information Security Diperlukan?
            1. “Information-based society” menyebabkan nilai informasi menjadi sangat penting dan menuntut kemampuan untuk mengakses dan menyediakan informasi secara cepat dan akurat.
            2. Infrastruktur Jaringan komputer (LAN, Internet) memungkinkan penyediaan informasi secara cepat, sekaligus membuka potensi lubang keamanan (security hole).

            **Kejahatan Information Security meningkat karena:**
            1. Aplikasi bisnis berbasis TI dan jaringan komputer meningkat (online banking, e-commerce, EDI).
            2. Desentralisasi server menyebabkan lebih banyak sistem yang harus ditangani.
            3. Transisi dari single vendor ke multi vendor.
            4. Meningkatnya kemampuan pemakai.
            5. Kesulitan penegak hukum dan belum adanya ketentuan yang pasti.
            6. Semakin kompleksnya sistem, semakin besar source code program.
            7. Berhubungan dengan internet.
            8. Mudahnya memperoleh software untuk menyerang.
            9. Perangkat hukum yang kurang akomodatif.
            10. Semakin kompleksnya sistem.
            11. Terjadinya lubang keamanan.
            12. Semakin banyak usaha yang memanfaatkan IT berbasis jaringan.
            """
        )

    # Level Keamanan
    with st.container(border=True):
        st.markdown(
            """
            ### Level Keamanan Information Security
            Berdasarkan level, metode Information Security dibedakan menjadi:
            - **Level 0** – keamanan fisik (physical security). Apabila keamanan fisik terjaga maka keamanan di dalam komputer juga terjaga.
            - **Level 1** – terdiri dari database security, data security, dan device security.
            - **Level 2** – keamanan jaringan (network security), sebagai tindak lanjut level 1.
            - **Level 3** – information security (informasi seperti kata sandi, file penting).
            - **Level 4** – keseluruhan dari level 1-3. Jika satu tidak terpenuhi, level 4 tidak terpenuhi.
            """
        )

    # Metode Information Security
    with st.container(border=True):
        st.markdown(
            """
            ### Metode Information Security

            **1. Network Topology**
            Sebuah jaringan komputer dapat dibagi atas kelompok eksternal (Internet), internal, dan DeMilitarized Zone (DMZ).
            - Pihak luar hanya dapat berhubungan dengan host di DMZ.
            - Host di DMZ dapat melakukan hubungan dengan host internal secara terbatas.
            - Host internal tidak dapat langsung ke luar, harus melalui perantara di DMZ.

            **2. Security Information Management (SIM)**
            SIM berfungsi menyediakan informasi terkait pengamanan jaringan secara terpusat. SIM juga mampu menganalisis data melalui teknik korelasi, menghasilkan peringatan dan laporan lengkap.

            **3. IDS / IPS**
            - **IDS (Intrusion Detection System)** menerima salinan paket, memeriksa, dan memberi peringatan jika ditemukan paket berbahaya.
            - **IPS (Intrusion Prevention System)** lebih aktif, bekerja sama dengan firewall untuk menolak paket berbahaya.
            Metode deteksi: Signature based (daftar signature) dan Anomaly based (pola tidak biasa).

            **4. Port Scanning**
            Digunakan penyerang untuk mengetahui port terbuka. Caranya dengan mengirim paket inisiasi koneksi ke setiap port; jika ada jawaban, berarti port terbuka.

            **5. Packet Fingerprinting**
            Untuk mengetahui peralatan apa saja dalam jaringan (jenis perangkat, sistem operasi).
            """
        )

    # Jenis Information Security dalam kehidupan sehari-hari
    with st.container(border=True):
        st.markdown(
            """
            ### Jenis Information Security dalam Kehidupan Sehari-hari
            1. **Keamanan eksternal** – pengamanan fasilitas komputer dari penyusup dan bencana (kebakaran, banjir).
            2. **Keamanan interface pemakai** – identifikasi pemakai sebelum mengakses program dan data.
            3. **Keamanan internal** – kendali pada perangkat keras dan sistem operasi untuk menjaga integritas program dan data.
            """
        )

    # Data Loss dan Intruder
    with st.container(border=True):
        st.markdown(
            """
            ### Masalah Penting: Data Loss dan Intruder

            **Data Loss** disebabkan oleh:
            - Bencana
            - Kesalahan perangkat lunak/perangkat keras
            - Kesalahan manusia (human error)

            **Penyusup (Intruder)** dibagi dua:
            - **Penyusup pasif** – membaca data tidak terotorisasi.
            - **Penyusup aktif** – mengubah susunan sistem/data tidak terotorisasi.
            """
        )

    # Empat Kategori Ancaman
    with st.container(border=True):
        st.markdown(
            """
            ### Empat Kategori Ancaman Information Security
            1. **Interupsi** – sumber daya dihancurkan (ancaman terhadap ketersediaan).
            2. **Intersepsi** – akses tak sah ke sumber daya (ancaman kerahasiaan).
            3. **Modifikasi** – akses tak sah dan mengubah sumber daya (ancaman integritas).
            4. **Fabrikasi** – menyisipkan objek palsu ke sistem.
            """
        )

    # Daftar Ancaman
    with st.container(border=True):
        st.markdown(
            """
            ### Daftar Ancaman Information Security
            a. Adware
            b. Backdoor Trojan
            c. Bluejacking
            d. Bluesnarfing
            e. Boot Sector Viruses
            f. Browser Hijackers
            g. Chain Letters
            h. Cookies
            i. Denial of Service Attack
            j. Dialers
            k. Document Viruses
            l. Email Viruses
            m. Internet Worms
            n. Mobile Phone Viruses

            **Jenis Ancaman Lainnya:**
            - Virus
            - Email Virus
            - Internet Worms
            - Spam
            - Trojan Horse
            - Spyware
            - Serangan Brute-force
            """
        )

    # Ancaman di Era Industri 4.0
    with st.container(border=True):
        st.markdown(
            """
            ### Ancaman di Era Industri 4.0
            Di era industri 4.0, organisasi sangat terhubung dengan perangkat pintar dan jaringan pintar. Ini dapat menjadi target menguntungkan bagi penjahat cyber. Semakin besar konektivitas, semakin besar risiko serangan. Cybersecurity merupakan elemen inti Industry 4.0 dan harus menjadi bagian integral dari budaya dan strategi organisasi.

            **Ilustrasi ancaman** dapat berasal dari kekuatan asing, pesaing, peretas terorganisir, orang dalam, konfigurasi buruk, dan vendor pihak ketiga.
            """
        )
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-9/fig1.png", use_container_width=True)
        st.caption("Gambar IX.1 Berbagai Ancaman pada Sistem Pengendalian Proses (Sumber: mocana.com)")

    # Industrial Control System (ICS)
    with st.container(border=True):
        st.markdown(
            """
            ### Industrial Control System (ICS)
            ICS adalah istilah umum yang mencakup sistem kontrol dan instrumentasi untuk kontrol proses industri. Sistem dapat berkisar dari pengontrol panel modular hingga sistem kontrol terdistribusi besar. Semua sistem menerima data dari sensor, membandingkan dengan set point, dan mengendalikan proses melalui elemen kontrol akhir (katup, dll). Sistem besar biasanya menggunakan SCADA, DCS, atau PLC.
            """
        )
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-9/fig2.png", use_container_width=True)
        st.caption("Gambar IX.2 Jalur Serangan Siber Pada Collaborative Robotic Cyber Physical System")

    # Serangan Siber
    with st.container(border=True):
        st.markdown(
            """
            **Serangan siber (cyber-attack)** adalah manuver ofensif yang menargetkan sistem informasi, infrastruktur, jaringan, atau perangkat komputer dengan tindakan berbahaya untuk mencuri, mengubah, atau menghancurkan target. Serangan dapat berupa kampanye siber, perang siber, atau terorisme siber. Contoh canggih: worm Stuxnet. Analisis perilaku pengguna dan SIEM digunakan untuk pencegahan.
            """
        )
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-9/fig3.png", use_container_width=True)
        st.caption("Gambar IX.3 Bagaimana Ancaman Siber yang Menyerang Konvergensi IT, OT, dan IP")

    # Konvergensi IT dan OT
    with st.container(border=True):
        st.markdown(
            """
            ### Konvergensi IT dan OT
            Penanganan sekuriti di industri biasanya terbagi menjadi tiga: sekuriti fisik, sekuriti TI, dan sekuriti operasional. Teknologi modern dibagi menjadi IT (mengelola aplikasi, data, infrastruktur) dan OT (mengelola ribuan perangkat, sering dengan IoT). Keberhasilan cybersecurity membutuhkan kolaborasi IT dan OT. Security Operation Center (SOC) efektif memerlukan sinergi orang, proses, dan teknologi dari kedua bidang.
            """
        )

    # Enam Sumber Ancaman Siber
    with st.container(border=True):
        st.markdown(
            """
            ### Enam Sumber Ancaman Siber
            1. Negara
            2. Penjahat dunia maya (cyber criminal)
            3. Peretas (hacktivist)
            4. Orang dalam (insider) dan penyedia layanan
            5. Pengembang produk dan layanan di bawah standar
            6. Konfigurasi layanan cloud yang buruk

            **Target potensial penjahat cyber:**
            - Data pelanggan
            - Data karyawan
            - Kekayaan intelektual
            - Vendor pihak ketiga dan keempat
            - Kualitas dan keamanan produk
            - Ketentuan dan harga kontrak
            - Perencanaan strategis
            - Data keuangan
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Segitiga CIA", expanded=True):
        st.markdown(
            """
            - **Confidentiality**: hanya yang berhak dapat mengakses.
            - **Integrity**: data utuh, tidak dimodifikasi tak sah.
            - **Availability**: data tersedia setiap saat.
            """
        )

    with st.expander("🔒 Level Keamanan"):
        st.markdown(
            """
            Level 0: fisik  
            Level 1: database, data, device  
            Level 2: jaringan  
            Level 3: informasi  
            Level 4: keseluruhan
            """
        )

    with st.expander("🛡️ Metode Keamanan"):
        st.markdown(
            """
            - Network Topology (DMZ)
            - SIM (Security Information Management)
            - IDS/IPS (deteksi/cegah)
            - Port Scanning
            - Packet Fingerprinting
            """
        )

    with st.expander("⚠️ Empat Kategori Ancaman"):
        st.markdown(
            """
            - Interupsi (availability)
            - Intersepsi (confidentiality)
            - Modifikasi (integrity)
            - Fabrikasi
            """
        )

    with st.expander("🌐 Ancaman Industri 4.0"):
        st.markdown(
            """
            - Meningkat seiring konektivitas.
            - Sumber: negara, penjahat, insider, vendor.
            - Target: data pelanggan, kekayaan intelektual, dll.
            """
        )

    with st.expander("🔗 IT vs OT"):
        st.markdown(
            """
            - IT: aplikasi, data, infrastruktur.
            - OT: perangkat, IoT, kontrol proses.
            - Kolaborasi penting untuk keamanan.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Level Keamanan", "5 (0-4)")
        st.metric("Metode Keamanan", "5")
        st.metric("Sumber Ancaman", "6")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - www.upguard.com
            - www.mocana.com
            - www.secureworldexpo.com
            - id.wikipedia.org
            - manajemen-ti.com
            """
        )