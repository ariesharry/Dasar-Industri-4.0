import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from sklearn.cluster import KMeans
import plotly.express as px


st.set_page_config(
    page_title="Simulasi IoT & ML",
    layout="wide"
)


st.title("🎥 Video Pendukung Pembelajaran")
st.caption("Penjelasan konsep dan penerapan terkait simulasi yang telah dilakukan")

st.video("https://www.youtube.com/watch?v=X6Tj2PT41v8")


st.divider()

st.title("🔧 Simulasi IoT")
st.caption("Eksplorasi rangkaian IoT secara interaktif menggunakan simulator")

components.iframe(
    src="https://wokwi.com/projects/321525495180034642",
    height=700,
    scrolling=True
)

st.divider()
st.title("🧠 Simulasi Machine Learning – K-Means")
st.caption("Ubah parameter dan amati perubahan hasil clustering")

# Parameter interaktif
col1, col2 = st.columns(2)
with col1:
    n_samples = st.slider("Jumlah Data", 50, 300, 150)
with col2:
    n_clusters = st.slider("Jumlah Cluster (k)", 2, 6, 3)

# Generate data
np.random.seed(42)
X = np.random.rand(n_samples, 2)

# KMeans
kmeans = KMeans(n_clusters=n_clusters, n_init=10)
labels = kmeans.fit_predict(X)

# Plotly scatter
fig = px.scatter(
    x=X[:, 0],
    y=X[:, 1],
    color=labels.astype(str),
    title="Visualisasi K-Means Clustering",
)

# Kontrol ukuran chart (PENTING)
fig.update_layout(
    height=400,              # <- ukuran sedang
    margin=dict(l=20, r=20, t=40, b=20),
    legend_title_text="Cluster"
)

st.plotly_chart(fig, use_container_width=True)



from sklearn.linear_model import LinearRegression

st.divider()
st.title("📈 Simulasi Machine Learning – Regresi Linear")
st.caption("Eksplorasi hubungan data dan garis regresi secara interaktif")

# Parameter interaktif
col1, col2 = st.columns(2)
with col1:
    n_samples_lr = st.slider("Jumlah Data", 20, 200, 80, key="lr_samples")
with col2:
    noise_level = st.slider("Tingkat Noise", 0.0, 1.0, 0.3, step=0.05)

# Generate data
np.random.seed(42)
X_lr = np.linspace(0, 10, n_samples_lr).reshape(-1, 1)
y_lr = 2.5 * X_lr.flatten() + 5 + noise_level * np.random.randn(n_samples_lr)

# Model regresi
model = LinearRegression()
model.fit(X_lr, y_lr)
y_pred = model.predict(X_lr)

# Plotly visualization
fig_lr = px.scatter(
    x=X_lr.flatten(),
    y=y_lr,
    title="Visualisasi Regresi Linear",
    labels={"x": "X (Input)", "y": "Y (Output)"},
)

fig_lr.add_scatter(
    x=X_lr.flatten(),
    y=y_pred,
    mode="lines",
    name="Garis Regresi"
)

# Kontrol ukuran chart
fig_lr.update_layout(
    height=400,
    margin=dict(l=20, r=20, t=40, b=20),
    legend_title_text="Keterangan"
)

st.plotly_chart(fig_lr, use_container_width=True)

# Insight singkat (edukatif)
st.markdown(f"""
**Persamaan Regresi:**  
\( y = {model.coef_[0]:.2f}x + {model.intercept_:.2f} \)
""")


st.divider()
st.title("📝 Kuis Interaktif")
st.caption("Jawab pertanyaan berikut untuk menguji pemahaman Anda")

score = 0
total = 3


q1 = st.radio(
    "1️⃣ Apa peran utama Internet of Things (IoT) dalam Industri 4.0?",
    [
        "Menggantikan seluruh tenaga kerja manusia",
        "Menghubungkan perangkat fisik untuk mengumpulkan dan bertukar data",
        "Hanya sebagai media penyimpanan data",
        "Menggantikan sistem informasi konvensional"
    ],
    index=None
)

if q1:
    if q1 == "Menghubungkan perangkat fisik untuk mengumpulkan dan bertukar data":
        st.success("✅ Benar. IoT memungkinkan perangkat saling terhubung dan bertukar data.")
        score += 1
    else:
        st.error("❌ Kurang tepat. IoT berfokus pada konektivitas dan pertukaran data antar perangkat.")


q2 = st.radio(
    "2️⃣ Pada simulasi K-Means, apa fungsi parameter *k*?",
    [
        "Menentukan jumlah data",
        "Menentukan jumlah cluster",
        "Menentukan tingkat noise",
        "Menentukan kecepatan komputasi"
    ],
    index=None
)

if q2:
    if q2 == "Menentukan jumlah cluster":
        st.success("✅ Benar. Nilai k menentukan berapa kelompok data yang dibentuk.")
        score += 1
    else:
        st.error("❌ Salah. Parameter k digunakan untuk menentukan jumlah cluster.")

q3 = st.radio(
    "3️⃣ Apa makna utama garis pada regresi linear?",
    [
        "Garis acak tanpa arti",
        "Hubungan rata-rata antara variabel input dan output",
        "Batas maksimum data",
        "Hasil klasifikasi data"
    ],
    index=None
)

if q3:
    if q3 == "Hubungan rata-rata antara variabel input dan output":
        st.success("✅ Benar. Garis regresi merepresentasikan hubungan linear antar variabel.")
        score += 1
    else:
        st.error("❌ Kurang tepat. Regresi linear memodelkan hubungan input–output.")

if q1 and q2 and q3:
    st.divider()
    st.subheader("📊 Hasil Kuis")

    st.info(f"Skor Anda: **{score} / {total}**")

    if score == total:
        st.success("🎉 Sangat baik! Anda memahami konsep IoT dan ML dengan baik.")
    elif score >= 2:
        st.warning("👍 Cukup baik. Silakan tinjau kembali bagian yang masih kurang.")
    else:
        st.error("📘 Perlu belajar ulang. Silakan ulangi simulasi dan video.")
