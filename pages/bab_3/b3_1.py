import streamlit as st
import plotly.express as px
import numpy as np

st.header("3.1 Linear Regression")

st.subheader("Teori Singkat")
st.write("Linear Regression mencari garis terbaik (y = mx + c) yang meminimalkan error terhadap data.")

# Visualisasi interaktif
st.subheader("Simulasi Interaktif")
m = st.slider("Slope (m)", -5.0, 5.0, 2.0, 0.1)
c = st.slider("Intercept (c)", -10.0, 10.0, 1.0, 0.1)

x = np.linspace(0, 10, 100)
y_true = 2 * x + 1 + np.random.normal(0, 2, 100)  # Data dummy
y_pred = m * x + c

fig = px.scatter(x=x, y=y_true, title="Simulasi Linear Regression")
fig.add_scatter(x=x, y=y_pred, mode='lines', name='Prediksi')
st.plotly_chart(fig)

# Latihan sederhana
st.subheader("Latihan Cepat")
prediksi = st.number_input("Prediksi y jika x=7 (dengan model y = 2x + 1)", value=0.0)
if st.button("Cek Jawaban"):
    jawaban_benar = 2*7 + 1
    if abs(prediksi - jawaban_benar) < 0.1:
        st.success("Benar! y = 15")
    else:
        st.error(f"Salah. Jawaban benar: {jawaban_benar}")