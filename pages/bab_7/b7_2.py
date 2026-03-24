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
    st.title("Jenis-Jenis Simulasi")

    with st.container(border=True):
        st.markdown(
            """
            Terdapat beberapa jenis simulasi yang disesuaikan dengan karakteristik dari sistem yang diamati. Secara umum berikut merupakan jenis simulasi yang sering ditemui dalam suatu studi simulasi yaitu:

            • **Simulasi statis dan dinamis**  
            Berdasarkan dampak variabel terhadap waktu, maka simulasi dibedakan menjadi statis dan dinamis. Pada simulasi statis, perubahan variabel pada sistem tidak dipengaruhi oleh waktu. Model simulasi statis digunakan untuk mengetahui kondisi sistem pada saat tertentu. Misalnya, simulasi permintaan produk sepatu dengan menggunakan data historis untuk estimasi jumlah permintaan di masa mendatang. Pada simulasi dinamis, perubahan-perubahan variabel dipengaruhi oleh waktu. Selain itu juga dapat diketahui status variabel pada waktu-waktu tertentu akan berbeda, karena statistik yang terkumpul berdasarkan waktu yang berjalan.

            • **Simulasi kontinyu dan diskrit**  
            Berdasarkan sifat perubahan variabel terhadap waktu, simulasi dapat digolongkan menjadi simulasi kontinyu atau diskrit. Pada simulasi kontinyu, status variabel pada sistem berubah secara kontinyu terhadap waktu, misal perubahan volume bahan bakar pada simulasi pengisian tangki BBM SPBU. Sedangkan pada simulasi diskrit, status dari tiap variabel berubah pada titik tertentu, misalnya perubahan panjang antrian di suatu server dari waktu ke waktu.

            • **Simulasi deterministik dan stokastik**  
            Simulasi juga dapat dibedakan berdasarkan sifat nilai variabel pada sistem. Pada simulasi deterministik, variabelnya bernilai konstan. Contohnya waktu pemanasan menu dalam microwave dianggap konstan sebesar 60 detik sebagaimana ditunjukkan oleh timer. Sedangkan pada simulasi stokastik, variabelnya dianggap berubah-ubah. Misal waktu pengisian BBM pada suatu SPBU akan berbeda-beda antar satu kendaraan dengan yang lainnya
            """
        )

# ================== KOLOM KEY TAKEAWAYS ==================
with cols[1].container(border=True):
    st.subheader("🎯 Key Takeaways")

    with st.expander("📌 Statis vs Dinamis", expanded=True):
        st.markdown(
            """
            - **Statis**: tidak dipengaruhi waktu (simulasi Monte Carlo).
            - **Dinamis**: dipengaruhi waktu (simulasi antrian).
            """
        )

    with st.expander("📌 Kontinyu vs Diskrit"):
        st.markdown(
            """
            - **Kontinyu**: variabel berubah terus (level air).
            - **Diskrit**: variabel berubah pada titik waktu (jumlah antrian).
            """
        )

    with st.expander("📌 Deterministik vs Stokastik"):
        st.markdown(
            """
            - **Deterministik**: nilai pasti (timer microwave).
            - **Stokastik**: nilai acak (waktu servis).
            """
        )

    # Fakta singkat
    with st.container(border=True):
        st.markdown("### 📊 Fakta Singkat")
        st.metric("Kategori Simulasi", "3 jenis (berdasarkan waktu, perubahan, nilai)")

    # Referensi
    with st.container(border=True):
        st.markdown("### 📚 Referensi")
        st.markdown(
            """
            - Law, Averill M. (2015)
            - Kelton dkk (2010)
            """
        )