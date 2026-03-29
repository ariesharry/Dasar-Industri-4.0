import streamlit as st
import random
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Inisialisasi session state
if "servers" not in st.session_state:
    st.session_state.servers = []  # list of dict: {id, total_requests, active_connections}
    st.session_state.round_robin_idx = 0
    st.session_state.request_log = []  # menyimpan log request terbaru

def reset_simulation(num_servers):
    st.session_state.servers = [
        {"id": i, "total_requests": 0, "active_connections": 0}
        for i in range(1, num_servers + 1)
    ]
    st.session_state.round_robin_idx = 0
    st.session_state.request_log.clear()

def select_server(algorithm):
    servers = st.session_state.servers
    if not servers:
        return None
    if algorithm == "Round Robin":
        idx = st.session_state.round_robin_idx % len(servers)
        st.session_state.round_robin_idx += 1
        return servers[idx]
    elif algorithm == "Least Connections":
        # Pilih server dengan active_connections terkecil
        return min(servers, key=lambda s: s["active_connections"])
    elif algorithm == "Random":
        return random.choice(servers)
    else:
        return servers[0]  # fallback

def send_request(algorithm):
    server = select_server(algorithm)
    if server:
        server["total_requests"] += 1
        server["active_connections"] += 1
        # Simpan log
        st.session_state.request_log.append({
            "time": len(st.session_state.request_log) + 1,
            "server": server["id"],
            "algorithm": algorithm,
            "action": "request"
        })

def process_request():
    # Cari server dengan active_connections > 0 secara acak atau urutan?
    # Agar adil, kita proses server yang memiliki koneksi aktif.
    active_servers = [s for s in st.session_state.servers if s["active_connections"] > 0]
    if not active_servers:
        return
    server = random.choice(active_servers)
    server["active_connections"] -= 1
    st.session_state.request_log.append({
        "time": len(st.session_state.request_log) + 1,
        "server": server["id"],
        "algorithm": "N/A",
        "action": "complete"
    })

# Konfigurasi halaman
st.set_page_config(page_title="Load Balancer Simulator", layout="wide")
st.title("⚖️ Load Balancer Simulator")
st.markdown("""
Simulasi interaktif yang menunjukkan bagaimana *load balancer* mendistribusikan request ke server backend.
Pilih algoritma, kirim request, dan lihat bagaimana beban tersebar.
""")

# Sidebar untuk konfigurasi
with st.sidebar:
    st.header("Pengaturan")
    num_servers = st.slider("Jumlah server", 1, 10, 3)
    algorithm = st.selectbox(
        "Algoritma Load Balancing",
        ["Round Robin", "Least Connections", "Random"],
        index=0,
        help="""
        - **Round Robin**: Request diberikan bergantian ke setiap server.
        - **Least Connections**: Request diberikan ke server dengan koneksi aktif paling sedikit.
        - **Random**: Request diberikan secara acak.
        """
    )
    if st.button("🔄 Reset Simulasi"):
        reset_simulation(num_servers)
        st.rerun()

# Pastikan jumlah server sesuai dengan slider
if len(st.session_state.servers) != num_servers:
    reset_simulation(num_servers)

# Tombol aksi
col1, col2, col3 = st.columns(3)
with col1:
    send_btn = st.button("📤 Kirim Request", use_container_width=True)
with col2:
    process_btn = st.button("✅ Proses Satu Request (Selesai)", use_container_width=True)
with col3:
    # Auto mode bisa ditambahkan nanti
    st.write("")

if send_btn:
    send_request(algorithm)
if process_btn:
    process_request()

# Tampilan data server
st.subheader("📊 Status Server")
# Buat DataFrame untuk tampilan
server_data = []
for s in st.session_state.servers:
    server_data.append({
        "Server": f"Server {s['id']}",
        "Total Requests": s["total_requests"],
        "Active Connections": s["active_connections"],
        "Load (%)": (s["active_connections"] / (sum(sv["active_connections"] for sv in st.session_state.servers) or 1)) * 100
    })
df = pd.DataFrame(server_data)

# Tampilkan tabel dengan format
st.dataframe(
    df.style.format({"Load (%)": "{:.1f}%"}),
    use_container_width=True,
    hide_index=True
)

# Visualisasi dengan plotly
col_chart1, col_chart2 = st.columns(2)
with col_chart1:
    fig_connections = px.bar(
        df, x="Server", y="Active Connections",
        title="Aktif Koneksi per Server",
        color="Server", text="Active Connections"
    )
    fig_connections.update_traces(textposition="outside")
    st.plotly_chart(fig_connections, use_container_width=True)

with col_chart2:
    fig_requests = px.bar(
        df, x="Server", y="Total Requests",
        title="Total Request Diterima per Server",
        color="Server", text="Total Requests"
    )
    fig_requests.update_traces(textposition="outside")
    st.plotly_chart(fig_requests, use_container_width=True)

# Log request terbaru
st.subheader("📜 Log Aktivitas")
if st.session_state.request_log:
    log_df = pd.DataFrame(st.session_state.request_log[-10:])  # 10 terakhir
    # Ubah action menjadi ikon atau teks yang jelas
    log_df["action"] = log_df["action"].map({"request": "📤 Request", "complete": "✅ Complete"})
    log_df = log_df.rename(columns={"time": "Urutan", "server": "Server", "algorithm": "Algoritma", "action": "Aksi"})
    st.dataframe(log_df, use_container_width=True, hide_index=True)
else:
    st.info("Belum ada aktivitas. Kirim atau proses request untuk melihat log.")

# Penjelasan tambahan
st.markdown("---")
with st.expander("ℹ️ Cara Kerja Simulator"):
    st.write("""
    1. **Kirim Request**: Request baru akan dialokasikan ke salah satu server berdasarkan algoritma yang dipilih.
    2. **Proses Satu Request**: Menyelesaikan satu koneksi aktif dari server yang dipilih secara acak (untuk mensimulasikan bahwa request telah selesai diproses).
    3. **Active Connections**: Jumlah request yang sedang diproses di server tersebut.
    4. **Total Requests**: Jumlah kumulatif request yang pernah diterima server.
    
    Dengan memproses request, Anda dapat melihat bagaimana algoritma *Least Connections* memilih server dengan beban aktif terkecil.
    """)

st.markdown("---")
st.caption("Simulasi ini menunjukkan konsep dasar load balancing. Dalam implementasi nyata, load balancer juga mempertimbangkan kesehatan server dan faktor lain.")