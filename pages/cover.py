import streamlit as st
from PIL import Image
import os

# Konfigurasi halaman
st.set_page_config(
    page_title="E-Modul Industri 4.0",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed"
)
import base64
st.markdown("""
<div class="logo-container">
    <img src="data:image/png;base64,{}" width="200">
</div>
""".format(
    base64.b64encode(open("assets/logo-pk.png", "rb").read()).decode()
), unsafe_allow_html=True)

st.markdown("""
<style>
.logo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 1rem;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# CSS kustom untuk tampilan cover (tema biru)
st.markdown("""
<style>
    /* Reset padding dan margin default */
    .main > div {
        padding: 0rem !important;
        margin: 0rem !important;
    }
    
    /* Container utama full screen dengan gradien biru */
    .stApp {
        background: linear-gradient(135deg, #0a1f44, #1e3a8a, #2563eb);
        background-attachment: fixed;
    }
    
    /* Konten tengah */
    .cover-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 70vh;
        text-align: center;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 2rem;
    }
    
    /* Judul utama dengan efek biru */
    .main-title {
        font-size: 5rem;
        font-weight: 900;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 20px rgba(37,99,235,0.7), 0 0 40px rgba(37,99,235,0.5);
        animation: fadeInUp 1.5s ease;
    }
    
    /* Subjudul */
    .sub-title {
        font-size: 1.8rem;
        font-weight: 300;
        letter-spacing: 0.3em;
        margin-bottom: 3rem;
        opacity: 0.9;
        text-shadow: 0 0 10px rgba(255,255,255,0.5);
        animation: fadeInUp 1.8s ease;
    }
    
    /* Garis dekoratif biru */
    .divider {
        width: 150px;
        height: 4px;
        background: linear-gradient(90deg, transparent, #3b82f6, transparent);
        margin: 2rem auto;
        animation: expandWidth 2s ease;
    }
    
    /* Animasi */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes expandWidth {
        from {
            width: 0;
        }
        to {
            width: 150px;
        }
    }
    
    /* Responsif */
    @media (max-width: 768px) {
        .main-title {
            font-size: 3rem;
        }
        .sub-title {
            font-size: 1.2rem;
            letter-spacing: 0.2em;
        }
    }
</style>
""", unsafe_allow_html=True)

# Konten cover
st.markdown("""
<div class="cover-content">
    <div class="sub-title">E-MODUL INTERAKTIF</div>
    <div class="main-title">DASAR INDUSTRI 4.0</div>
    <div class="divider"></div>
    <div style="font-size: 1.2rem; max-width: 700px; margin-top: 2rem; opacity:0.8; animation: fadeInUp 2.2s ease;">
        Memahami konsep, teknologi, dan implementasi revolusi industri keempat<br>
        untuk menghadapi era digital
    </div>
</div>
""", unsafe_allow_html=True)
