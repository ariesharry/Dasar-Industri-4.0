import streamlit as st
import streamlit.components.v1 as components

st.title("3D Printing Simulation")

components.html(
    """
    <iframe src="https://grid.space/kiri/"
    width="100%"
    height="800"
    style="border:none;">
    </iframe>
    """,
    height=800,
)