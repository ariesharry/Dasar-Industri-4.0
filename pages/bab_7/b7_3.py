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
    st.title("Simulasi dalam Industri 4.0")

    with st.container(border=True):
        st.markdown(
            """
            Berdasarkan publikasi oleh Russmann dkk (2015) dari The Boston Consulting Group bahwa terdapat 9 (sembilan) teknologi kunci yang akan mendorong perkembangan revolusi industri keempat yaitu big data and analytics, autonomous robots, horizontal and vertical integration, industrial Internet of Things (IoT), cyber security, the Cloud, additive manufacturing, augmented and virtual reality (AR/VR) dan simulation. Keseluruh teknologi tersebut saat ini sudah ada, namun perkembangannya akan semakin pesat di masa mendatang dan mendorong perubahan menjadi transformatif. Sebagai salah satu teknologi kunci, simulasi, dengan bantuan komputer, sebenarnya saling terkait atau menjadi satu kesatuan dengan beberapa teknologi kunci lainnya. Misalkan pada teknologi kunci big data and analytics, dimana data yang berjumlah masif dikumpulkan dan dianalisis untuk kemudian menjadi dasar dalam sebuah pengambilan keputusan. Seringkali metode yang digunakan dalam analisis tersebut adalah metode simulasi. Contohnya adalah data pengguna aplikasi Gojek terkait layanan pesan antar makanan Go-Food. Simulasi dapat dilakukan dengan menerapkan beragam skenario promosi (misalkan diskon, bundling, cashback, reward point, dll) untuk menentukan tipe promosi apa yang paling tepat dalam memaksimalkan kepuasan pelanggan dan keuntungan perusahaan. Atau misalkan data parameter operasional suatu mesin yang dikumpulkan oleh sensor tertentu yang digunakan untuk memprediksi kapan mesin tersebut memerlukan perawatan (bersifat predictive maintenance yang disimpulkan melalui proses simulasi). Keberadaan simulasi yang embedded dalam teknologi kunci lainnya seperti ilustrasi di atas menggambarkan signifikansi peran simulasi tidak hanya sebagai teknologi kunci namun juga sebagai sebuah metodologi analisis yang bersifat fleksibel.
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Simulasi sebagai Teknologi Kunci", expanded=True):
        st.markdown(
            """
            - Salah satu dari 9 teknologi kunci Industri 4.0 (BCG).
            - Terkait erat dengan big data & analytics.
            """
        )

    with st.expander("💡 Contoh Penggunaan"):
        st.markdown(
            """
            - Simulasi promosi Go-Food (skenario diskon, bundling).
            - Predictive maintenance mesin berbasis data sensor.
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Teknologi Kunci Industri 4.0", "9 (termasuk simulasi)")
        st.metric("Sumber", "Russmann dkk (2015), BCG")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Rüssmann, M., Lorenz, M., Gerbert, P., Waldner, M., Justus, J., Engel, P., dan Harnisch, M. (2015)
            """
        )