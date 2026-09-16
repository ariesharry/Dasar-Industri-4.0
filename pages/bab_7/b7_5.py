import streamlit as st

st.set_page_config(layout="wide")

st.title("RealVirtual Demo")

st.info(
    "Demo RealVirtual tidak dapat ditampilkan langsung di dalam iframe karena "
    "server RealVirtual melarang embedding dari situs lain. Klik tombol di bawah "
    "untuk membukanya di tab baru."
)

st.markdown(
    """
    <div style="
        padding: 2.5rem;
        border-radius: 1rem;
        background: linear-gradient(135deg, #0f172a, #1e3a8a);
        color: white;
        text-align: center;
        margin: 1rem 0 2rem;
    ">
        <h2 style="margin: 0 0 0.75rem;">Interactive Digital Twin</h2>
        <p style="margin: 0 0 1.5rem; color: #dbeafe;">
            Jalankan simulasi industri 4.0 langsung di browser.
        </p>
        <a href="https://web.realvirtual.io/demo" target="_blank" rel="noopener noreferrer"
           style="
               display: inline-block;
               padding: 0.75rem 1.5rem;
               border-radius: 0.5rem;
               background: #3b82f6;
               color: white;
               text-decoration: none;
               font-weight: 600;
           ">
            Buka RealVirtual Demo ↗
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Jika tab baru tidak terbuka, izinkan pop-up untuk situs ini lalu klik tombol kembali.")
