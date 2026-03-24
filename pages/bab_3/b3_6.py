import streamlit as st
import streamlit.components.v1 as components

st.title("Arm Robotic Simulation")

components.html(
    """
    <iframe src="https://rocksi.net/"
    width="100%"
    height="800"
    style="border:none;">
    </iframe>
    """,
    height=800,
)