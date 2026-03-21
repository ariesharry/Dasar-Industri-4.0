import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from sklearn.cluster import KMeans
import plotly.express as px


st.set_page_config(
    page_title="Simulasi IoT",
    layout="wide"
)


st.title("🔧 Simulasi IoT")
st.caption("Eksplorasi rangkaian IoT secara interaktif menggunakan simulator")

components.iframe(
    src="https://wokwi.com/projects/321525495180034642",
    height=700,
    scrolling=True
)