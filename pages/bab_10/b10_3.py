import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .stColumn:first-child > div:first-child {
        background-color: #7FA8FF;
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
    st.title("Teknologi Manufaktur Aditif")

    with st.container(border=True):
        st.markdown(
            """
            ### X.3 Teknologi Manufaktur Aditif

            Teknologi manufaktur aditif dapat diklasifikasikan menurut konsep manufaktur paling dasar. Berdasarkan ISO/ASTM 52900:2015 (ASTM F2792) Additive manufacturing - General principles - Terminology, teknologi manufaktur aditif dapat dikelompokkan menjadi 7 (tujuh) golongan. Rincian dari masing-masing teknologi tersebut, baik uraian penjelasannya, material dan penggunaannya, dapat dilihat pada tabel berikut:
            """
        )

    with st.container(border=True):
        data_teknologi = {
            "Jenis Teknologi": [
                "Fused Deposition Modeling (FDM)",
                "Powder Bed Fusion (PBF)",
                "Direct Energy Deposition (DED)",
                "Vat Photopolymerization",
                "Material Jetting",
                "Sheet Lamination",
                "Binder Jetting"
            ],
            "Uraian Dasar": [
                "Lapisan selaras dengan peleburan dan pengekstrusian termoplastik melalui nozzel",
                "Lapisan dari bahan partikel halus diendapkan dan dilelehkan (sintering) dengan sumber pemanas selektif",
                "Sangat mirip dengan proses pengelasan, nozzel yang dipasang lengan multi-sumbu mengendapkan material dan menyediakan sumber pemanas untuk membuat lapisan",
                "Menggunakan resin photopolymer yang dapat melakukan 'curing' secara selektif dengan penggunaan sinar UV",
                "Sangat mirip dengan proses pencetakan tradisional, kepala pencetakan inkjet digunakan untuk menyimpan material yang membentuk setiap lapisan",
                "Material yang disimpan dalam gulungan diaplikasikan dan diikat di atas permukaan biasa (lapisan pertama) atau lapisan sebelumnya, dan kemudian dipotong sesuai bentuk yang diinginkan",
                "Lapisan material bubuk halus diendapkan dan diikat secara selektif oleh kepala pencetakan (print head)"
            ],
            "Material & Aplikasi": [
                "Material: thermoplastic; Aplikasi: model ilustrasi, sketsa/model fungsional",
                "Material: plastik/logam; Aplikasi: model fungsional/komponen akhir",
                "Material: logam; Aplikasi: model fungsional/komponen akhir",
                "Material: resin; Aplikasi: model ilustrasi, sketsa/model fungsional",
                "Material: resin/logam/wax; Aplikasi: model ilustrasi, sketsa/model fungsional",
                "Material: kertas, komposit; Aplikasi: model ilustrasi (kertas), model fungsional/komponen akhir (komposit)",
                "Material: batu pasir; Aplikasi: model ilustrasi"
            ]
        }
        df_teknologi = pd.DataFrame(data_teknologi)
        st.table(df_teknologi)
        st.caption("Tabel X.1 Kelompok Utama Teknologi Manufaktur Aditif (Sumber: Gonzales dkk, 2018)")

    with st.container(border=True):
        st.markdown(
            """
            Menurut Singamneni S dkk (2019) metode yang paling banyak digunakan adalah Selective Laser Sintering (SLS), Selective Laser Melting (SLM), Electron Beam Melting (EBM), Stereolithography (SLA), ink-jet printing, Fused Deposition Modelling (FDM) and Direct Metal Deposition (MD). Sementara itu sebagai kandidat material dimungkinkan, sedang dikembangkan logam, polimer, keramik, dan komposit dengan kombinasi berbeda.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 7 Teknologi AM", expanded=True):
        st.markdown(
            """
            - FDM, PBF, DED, Vat Photopolymerization,
            - Material Jetting, Sheet Lamination, Binder Jetting.
            """
        )

    with st.expander("🔧 Metode Populer"):
        st.markdown(
            """
            - SLS, SLM, EBM, SLA, ink-jet, FDM, DMD.
            """
        )

    with st.expander("🧪 Material"):
        st.markdown(
            """
            - Plastik, logam, resin, wax, kertas, komposit, keramik.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Jenis Teknologi", "7")
        st.metric("Standar", "ISO/ASTM 52900:2015")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Gonzales dkk (2018)
            - Singamneni S dkk (2019)
            """
        )