import streamlit as st
import streamlit.components.v1 as components

st.title("PLC Simulator")

components.html(
    """
    <iframe src="https://app.plcsimulator.online/"
    width="100%"
    height="800"
    style="border:none;">
    </iframe>
    """,
    height=800,
)