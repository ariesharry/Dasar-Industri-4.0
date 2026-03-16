import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Simulasi IoT – Wokwi",
    layout="wide"
)

st.title(":material/airplay: Simulasi IoT")

# Container khusus untuk simulasi
with st.container():
    st.markdown(
        """
        <style>
        .wokwi-container iframe {
            width: 100%;
            min-height: 70vh;
            border: none;
        }
        </style>
        <div class="wokwi-container">
        """,
        unsafe_allow_html=True
    )

    components.iframe(
        src="https://wokwi.com/projects/321525495180034642",
        height=700,
        scrolling=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

