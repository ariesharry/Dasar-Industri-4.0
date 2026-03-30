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
    st.title("Aplikasi Manufaktur Aditif")

    with st.container(border=True):
        st.markdown(
            """
            ### X.5 Aplikasi Manufaktur Aditif

            Berdasarkan ketiga fitur keunggulan utama proses AM yang telah dibahas sebelumnya, yaitu, waktu, biaya, dan fleksibilitas, maka banyak industri sudah mulai tertarik untuk menggunakan teknologi AM, terutama industri yang membutuhkan pembuatan prototype cepat dan/atau pembuatan komponen, yang membutuhkan jumlah rendah untuk komponen yang akan diproduksi dengan spesifikasi tertentu (kompleks) sesuai dengan permintaan konsumen. Menurut Mehrpouya (2019), komponen AM yang diproduksi di industri otomotif dan dirgantara telah memberikan andil sebesar 20% dari seluruh pasar AM.

            Para pemimpin industri pesawat terbang telah menjajaki kemungkinan penggunaan AM untuk menghasilkan berbagai komponen pesawat terbang seperti engsel, braket, komponen interior. Teknologi AM ini mendorong badan pesawat menjadi lebih ringan, sehingga efisiensi penggunaan bahan bakar menjadi lebih baik. Di samping sektor otomotif dan dirgantara, aplikasi AM juga terdapat pada industri seni, kesehatan dan bahkan industri arsitektur.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("✈️ Sektor Utama", expanded=True):
        st.markdown(
            """
            - Otomotif dan dirgantara (20% pasar).
            - Pesawat: engsel, braket, interior.
            - Seni, kesehatan, arsitektur.
            """
        )

    with st.expander("💡 Keunggulan"):
        st.markdown(
            """
            - Prototipe cepat.
            - Komponen kompleks dengan jumlah kecil.
            - Ringan (efisiensi bahan bakar).
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Kontribusi Otomotif & Dirgantara", "20%")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Mehrpouya (2019)
            """
        )