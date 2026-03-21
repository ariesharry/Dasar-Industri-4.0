import streamlit as st

st.set_page_config(layout="wide")

st.title("RealVirtual Demo")

st.markdown("""
<iframe 
    src="https://realvirtual.io/demo/democell/" 
    width="100%" 
    height="900" 
    frameborder="0"
    allowfullscreen>
</iframe>
""", unsafe_allow_html=True)