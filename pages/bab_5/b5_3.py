import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ========== CSS untuk background kolom pertama ==========
st.markdown(
    """
    <style>
    .stColumn:first-child > div:first-child {
        background-color: #FBEFEF;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
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
    st.title("Cloud Computing Deployment Model")

    # Gambar V.3
    with st.container(border=True):
        st.image("https://via.placeholder.com/600x250?text=Gambar+V.3+-+Jenis-jenis+Komputasi+Awan", use_container_width=True)
        st.caption("Gambar V.3 – Jenis-jenis komputasi awan (Sumber: blog.bookmyidentity.com)")

    # Public Cloud
    with st.container(border=True):
        st.markdown(
            """
            ### ☁️ Public Cloud
            Model di mana penyedia pihak ketiga menyediakan sumber daya komputasi (server, storage) melalui internet untuk publik.
            - **Karakteristik:** Arsitektur multi‑tenant, harga *pay‑as‑you‑go*.
            - **Vendor utama:** AWS, Microsoft Azure, Google Cloud Platform.
            """
        )

    # Private Cloud
    with st.container(border=True):
        st.markdown(
            """
            ### 🔒 Private Cloud
            Infrastruktur cloud yang digunakan secara eksklusif oleh satu organisasi. Bisa dikelola sendiri atau oleh pihak ketiga, dan di‑host di internal maupun eksternal.
            - **Karakteristik:** Kontrol penuh, keamanan lebih tinggi, cocok untuk data sensitif.
            - **Vendor:** VMware, OpenStack, atau solusi internal.
            """
        )

    # Hybrid Cloud
    with st.container(border=True):
        st.markdown(
            """
            ### 🔁 Hybrid Cloud
            Kombinasi public cloud, private cloud, dan/atau infrastruktur on‑premise yang saling terintegrasi.
            - **Karakteristik:** *Cloud bursting* (meluap ke publik saat privat penuh), fleksibilitas tinggi.
            - **Vendor:** Kombinasi dari penyedia public dan private.
            """
        )

    # Manfaat cloud untuk Industri 4.0
    with st.container(border=True):
        st.markdown(
            """
            ### 🏭 Cloud sebagai Fondasi Industri 4.0
            Cloud memungkinkan akses ke *digital twin*, simulasi prediktif, dan analitik dari mana saja.
            Produk seperti pemantauan mesin industri, pelacakan aset, dan pemantauan pengiriman dibangun di atas teknologi cloud.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("☁️ Public Cloud", expanded=True):
        st.markdown(
            """
            - Sumber daya untuk publik.
            - Multi‑tenant, bayar sesuai pakai.
            - Contoh: AWS, Azure, GCP.
            """
        )

    with st.expander("🔒 Private Cloud"):
        st.markdown(
            """
            - Eksklusif untuk satu organisasi.
            - Kontrol & keamanan lebih tinggi.
            - Cocok untuk data sensitif.
            """
        )

    with st.expander("🔁 Hybrid Cloud"):
        st.markdown(
            """
            - Gabungan public + private.
            - Cloud bursting.
            - Fleksibilitas optimal.
            """
        )

    with st.expander("🏭 Peran di Industri 4.0"):
        st.markdown(
            """
            - Fondasi untuk digital twin, simulasi, IoT.
            - Memungkinkan akses real‑time di mana saja.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Model Deployment", "Public, Private, Hybrid")
        st.metric("Vendor Public", "AWS, Azure, GCP")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - blog.bookmyidentity.com
            - Modul Industri 4.0 Dasar
            """
        )