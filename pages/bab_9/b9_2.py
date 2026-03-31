import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .stColumn:first-child > div:first-child {
        background-color: #C7DBFF;
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

with cols[0].container(border=True):
    st.title("Manajemen Risiko (Risk Management)")

    # Pengertian Risk Management
    with st.container(border=True):
        st.markdown(
            """
            Sebagai bagian dari information security, **risk management** adalah proses untuk mengidentifikasi risiko termasuk ancaman terhadap kelangsungan bisnis perusahaan dan bagaimana cara mengontrol ancaman tersebut. Salah satu program dari risk management adalah pembuatan dan penerapan contingency planning.

            Proses untuk mengidentifikasi dan mengontrol risiko yang mungkin terjadi disebut risk management. Bagian-bagian risk management adalah:
            1. Identifikasi Risiko (Risk Identification)
            2. Kontrol Risiko (Risk Control)
            """
        )

    # Risk Identification
    with st.container(border=True):
        st.markdown(
            """
            ### 1. Identifikasi Risiko (Risk Identification)
            Proses untuk mengidentifikasi dan membuat dokumen tentang semua ancaman yang mungkin terjadi.
            - Langkah pertama: buat daftar semua ancaman/risiko setelah identifikasi aset.
            - Langkah kedua: kelompokkan risiko berdasarkan kriteria (biaya, prioritas, dll).
            - Pada tahap ini juga dilakukan **risk assessment** untuk memilah ancaman yang paling berpotensi merugikan.
            """
        )
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.image("assets/bab-9/fig5.png", use_container_width=True)
        st.caption("Gambar IX.5 Butir-butir untuk Mengidentifikasi Resiko")

    # Risk Control
    with st.container(border=True):
        st.markdown(
            """
            ### 2. Kontrol Risiko (Risk Control)
            Proses untuk mengontrol berbagai ancaman sehingga dapat mengurangi atau menghilangkan akibat dari berbagai ancaman terhadap informasi.
            """
        )

    # Filosofi Sun Tzu
    with st.container(border=True):
        st.markdown(
            """
            ### Filosofi Sun Tzu dalam Risk Management
            > “If you know the enemy and know yourself, you need not fear the result of a hundred battles. If you know yourself but not the enemy, for every victory gained you will also suffer a defeat. If you know neither the enemy nor yourself, you will succumb in every battle”

            Untuk mengetahui kekuatan dan kemampuan diri sendiri:
            1. Identifikasi semua data dan informasi di tempat kerja.
            2. Analisis semua data dan informasi tersebut.
            3. Pahami aliran data dan informasi.
            4. Identifikasi aset (hardware/software) yang digunakan.
            5. Tanyakan: Bagaimana aset bernilai? Apa kelemahannya? Seberapa sering perlu diganti/di-maintain? Apakah sudah ada kontrol?

            Untuk mengetahui kekuatan lawan:
            1. Identifikasi semua ancaman di tempat kerja.
            2. Analisis semua ancaman/risiko.
            3. Pahami skenario ancaman.
            4. Identifikasi kontrol yang ada terhadap ancaman.
            5. Identifikasi mitigation strategy, termasuk biaya dan efektivitas.
            """
        )

    # Penetapan Manajemen Risiko
    with st.container(border=True):
        st.markdown(
            """
            ### Penetapan Manajemen Risiko
            Manajemen risiko cybersecurity umumnya ditetapkan oleh manajemen atas (dewan direksi) dalam proses perencanaan. Perusahaan terbaik memiliki **Chief Information Security Officer (CISO)** yang bertanggung jawab menetapkan dan memelihara visi, strategi, dan program untuk melindungi aset informasi dan data pelanggan.

            **Kegiatan pertahanan siber yang dimiliki CISO:**
            1. Mengelola prosedur, pelatihan, dan pengujian keamanan.
            2. Mempertahankan konfigurasi perangkat aman, perangkat lunak terbaru, dan patch kerentanan.
            3. Penempatan sistem deteksi intrusi dan pengujian penetrasi.
            4. Konfigurasi jaringan aman.
            5. Penerapan perlindungan data dan program pencegahan kehilangan.
            6. Pembatasan akses ke hak istimewa minimal.
            7. Enkripsi data jika diperlukan.
            8. Konfigurasi layanan cloud yang tepat.
            9. Penerapan manajemen kerentanan dengan pemindaian internal dan pihak ketiga.
            10. Rekrutmen dan retensi profesional cybersecurity.

            Manajemen risiko cybersecurity adalah proses berkelanjutan. Organisasi tidak akan pernah aman sepenuhnya; serangan dapat datang dari tingkat mana pun.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Definisi Risk Management", expanded=True):
        st.markdown(
            """
            - Proses identifikasi dan kontrol risiko.
            - Bertujuan melindungi kelangsungan bisnis.
            - Bagian: Risk Identification dan Risk Control.
            """
        )

    with st.expander("🔍 Risk Identification"):
        st.markdown(
            """
            - Identifikasi ancaman setelah identifikasi aset.
            - Kelompokkan risiko berdasarkan kriteria.
            - Risk assessment: memilah ancaman potensial.
            """
        )

    with st.expander("🛡️ Risk Control"):
        st.markdown(
            """
            - Mengontrol ancaman untuk mengurangi dampak.
            - Mitigation strategy.
            """
        )

    with st.expander("📜 Filosofi Sun Tzu"):
        st.markdown(
            """
            - Kenali diri sendiri (data, aset, kelemahan).
            - Kenali lawan (ancaman, kontrol).
            - Terapkan dalam analisis risiko.
            """
        )

    with st.expander("👤 Peran CISO"):
        st.markdown(
            """
            - Menetapkan visi & strategi keamanan.
            - Bertanggung jawab atas aset informasi.
            - Melakukan 10 kegiatan pertahanan siber.
            """
        )

    with st.expander("🔄 Proses Berkelanjutan"):
        st.markdown(
            """
            - Manajemen risiko tidak pernah selesai.
            - Ancaman terus berkembang.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Tahap Utama", "2 (Identifikasi, Kontrol)")
        st.metric("Kegiatan CISO", "10")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Abi Tyas Tunggal (2019)
            - www.upguard.com
            """
        )