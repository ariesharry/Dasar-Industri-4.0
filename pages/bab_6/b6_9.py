import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import sys
from io import StringIO
import traceback
from code_editor import code_editor

# Konfigurasi halaman
st.set_page_config(page_title="Forecast Minyak dengan LSTM", layout="wide")
st.title("🛢️ Forecasting Harga Minyak dengan LSTM (Eksekusi per Tahap)")
st.markdown("Edit kode di kolom kiri, jalankan per tahap, lihat hasil teks dan grafik di kolom kanan.")

# Inisialisasi session state
if 'namespace' not in st.session_state:
    # Buat data sintetis harga minyak
    np.random.seed(42)
    dates = pd.date_range(start='2015-01-01', end='2023-12-31', freq='D')
    n = len(dates)
    trend = np.linspace(50, 80, n)
    seasonal = 10 * np.sin(2 * np.pi * np.arange(n) / 365.25)
    noise = np.random.normal(0, 2, n)
    prices = trend + seasonal + noise
    prices = np.maximum(prices, 10)
    df = pd.DataFrame({'date': dates, 'price': prices})
    
    # Namespace awal dengan modul umum dan data
    namespace = {
        'pd': pd,
        'np': np,
        'plt': plt,
        'datetime': datetime,
        'timedelta': timedelta,
        'df': df,
    }
    st.session_state.namespace = namespace
    st.session_state.current_stage = "Data & Preprocessing"
    st.session_state.last_output = ""
    st.session_state.last_error = ""

# Daftar tahapan
stages = ["Data & Preprocessing", "Training LSTM", "Forecasting & Evaluasi"]

# Kode default per tahap
default_codes = {
    "Data & Preprocessing": '''# ===== TAHAP 1: DATA & PREPROCESSING =====
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 1.1 Data mentah
print("Data mentah (5 baris pertama):")
print(df.head())
print(f"Periode: {df['date'].min()} s/d {df['date'].max()}")
print("Statistik deskriptif harga:")
print(df['price'].describe())

# Plot data mentah
fig1, ax = plt.subplots(figsize=(10, 4))
ax.plot(df['date'], df['price'], color='blue', label='Harga Aktual')
ax.set_title('Data Mentah Harga Minyak Harian')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Harga (USD)')
ax.legend()
ax.grid(True)
plt.tight_layout()
data_mentah_plot = fig1

# 1.2 Preprocessing: scaling dan sequence
data = df['price'].values.reshape(-1, 1)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# Fungsi membuat sequence
def create_sequences(data, seq_length=30):
    X, y = [], []
    for i in range(len(data)-seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

seq_length = 30
X, y = create_sequences(scaled_data, seq_length)

# Split train/test (80% train, 20% test)
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

print(f"Shape X_train: {X_train.shape}, y_train: {y_train.shape}")
print(f"Shape X_test: {X_test.shape}, y_test: {y_test.shape}")
''',
    "Training LSTM": '''# ===== TAHAP 2: TRAINING LSTM =====
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# 2.1 Bangun model LSTM
from tensorflow.keras.layers import Input
model = Sequential([
    Input(shape=(X_train.shape[1], 1)),
    LSTM(50, activation='relu', return_sequences=True),
    Dropout(0.2),
    LSTM(50, activation='relu'),
    Dropout(0.2),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.summary(print_fn=lambda x: print(x))

# 2.2 Training dengan early stopping
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=20,
    batch_size=32,
    callbacks=[early_stop],
    verbose=1
)

# 2.3 Plot loss
fig2, ax = plt.subplots(figsize=(10, 4))
ax.plot(history.history['loss'], label='Training Loss')
ax.plot(history.history['val_loss'], label='Validation Loss')
ax.set_title('Model Loss')
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
ax.legend()
ax.grid(True)
plt.tight_layout()
loss_plot = fig2

print("\\n✅ Training selesai.")
''',
    "Forecasting & Evaluasi": '''# ===== TAHAP 3: FORECASTING & EVALUASI =====
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 3.1 Prediksi pada train dan test
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Kembalikan ke skala asli
train_predict = scaler.inverse_transform(train_predict)
y_train_actual = scaler.inverse_transform(y_train)
test_predict = scaler.inverse_transform(test_predict)
y_test_actual = scaler.inverse_transform(y_test)

# 3.2 Hitung error
train_mae = mean_absolute_error(y_train_actual, train_predict)
test_mae = mean_absolute_error(y_test_actual, test_predict)
train_rmse = np.sqrt(mean_squared_error(y_train_actual, train_predict))
test_rmse = np.sqrt(mean_squared_error(y_test_actual, test_predict))

print("=== Evaluasi Model ===")
print(f"Train MAE : {train_mae:.2f}, Train RMSE : {train_rmse:.2f}")
print(f"Test MAE  : {test_mae:.2f}, Test RMSE  : {test_rmse:.2f}")

# 3.3 Plot prediksi vs aktual
train_dates = df['date'][seq_length:seq_length+len(train_predict)]
test_dates = df['date'][seq_length+train_size:seq_length+train_size+len(test_predict)]

fig3, ax = plt.subplots(figsize=(12, 5))
ax.plot(df['date'], df['price'], label='Aktual', color='blue', alpha=0.5)
ax.plot(train_dates, train_predict, label='Prediksi Training', color='green')
ax.plot(test_dates, test_predict, label='Prediksi Testing', color='red')
ax.set_title('Perbandingan Harga Aktual vs Prediksi LSTM')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Harga (USD)')
ax.legend()
ax.grid(True)
plt.tight_layout()
prediksi_plot = fig3

# 3.4 Forecast 30 hari ke depan
last_sequence = scaled_data[-seq_length:].reshape(1, seq_length, 1)
future_preds = []
for _ in range(30):
    next_pred = model.predict(last_sequence, verbose=0)[0, 0]
    future_preds.append(next_pred)
    last_sequence = np.roll(last_sequence, -1, axis=1)
    last_sequence[0, -1, 0] = next_pred

future_preds = scaler.inverse_transform(np.array(future_preds).reshape(-1, 1))

# Buat tanggal forecast
last_date = df['date'].iloc[-1]
future_dates = [last_date + timedelta(days=i+1) for i in range(30)]

fig4, ax = plt.subplots(figsize=(12, 5))
ax.plot(df['date'], df['price'], label='Historis', color='blue')
ax.plot(future_dates, future_preds, label='Forecast 30 hari', color='red', marker='o')
ax.set_title('Forecast Harga Minyak 30 Hari ke Depan')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Harga (USD)')
ax.legend()
ax.grid(True)
plt.tight_layout()
forecast_plot = fig4

print("\\n✅ Forecasting selesai. Silakan lihat grafik di kolom kanan.")
'''
}

# Layout dua kolom
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📝 Pilih Tahap & Edit Kode")
    
    # Pilih tahap
    selected_stage = st.radio(
        "Tahapan:",
        stages,
        horizontal=True,
        label_visibility="collapsed",
        key="stage_selector"
    )
    st.session_state.current_stage = selected_stage
    
    # Kunci untuk menyimpan kode tahap ini di session_state
    code_key = f"code_{selected_stage}"
    
    # Migrasi jika masih string
    if code_key in st.session_state and isinstance(st.session_state[code_key], str):
        st.session_state[code_key] = {'text': st.session_state[code_key]}
    elif code_key not in st.session_state:
        st.session_state[code_key] = {'text': default_codes[selected_stage]}
    
    # --- Tombol aksi dan info variabel (sekarang di ATAS editor) ---
    col_run, col_reset = st.columns(2)
    with col_run:
        run_clicked = st.button("▶️ Jalankan Tahap Ini", use_container_width=True, type="primary")
    with col_reset:
        if st.button("↩️ Reset ke Default", use_container_width=True):
            st.session_state[code_key] = {'text': default_codes[selected_stage]}
            st.rerun()
    
    # Informasi namespace (variabel yang tersedia)
    with st.expander("📦 Variabel yang Tersedia Saat Ini", expanded=False):
        if st.session_state.namespace:
            # Ambil semua variabel (abaikan yang diawali underscore)
            var_names = [name for name in st.session_state.namespace.keys() if not name.startswith('_')]
            if not var_names:
                st.info("Tidak ada variabel yang tersedia.")
            else:
                for name in sorted(var_names):
                    obj = st.session_state.namespace[name]
                    st.markdown(f"**{name}** : `{type(obj).__name__}`")
                    
                    # Tampilkan preview untuk DataFrame
                    if isinstance(obj, pd.DataFrame):
                        with st.container(border=True):
                            st.dataframe(obj.head(5), use_container_width=True)
                    
                    # Tampilkan preview untuk Series
                    elif isinstance(obj, pd.Series):
                        st.write(obj.head(5))
                    
                    # Tampilkan preview untuk numpy array (jika 1D/2D)
                    elif isinstance(obj, np.ndarray):
                        st.write(f"Shape: {obj.shape}")
                        if obj.ndim <= 2 and obj.size > 0:
                            # Konversi ke DataFrame untuk tampilan lebih rapi
                            preview_df = pd.DataFrame(obj[:5] if obj.ndim == 1 else obj[:5, :])
                            st.dataframe(preview_df, use_container_width=True)
                    
                    # Tampilkan preview untuk list/dict jika ukurannya kecil
                    elif isinstance(obj, (list, dict)) and len(obj) < 10:
                        st.write(obj)
                    
                    # Pemisah antar variabel
                    st.divider()
        else:
            st.info("Belum ada variabel. Jalankan kode untuk menghasilkan.")
    
    # Code editor (tanpa tombol bawaan)
    with st.container(border=True):
        response = code_editor(
            st.session_state[code_key]['text'],
            lang='python',
            height=500,
            key=code_key,
            buttons=[]
        )
        # Catatan: editor otomatis memperbarui st.session_state[code_key]['text']

with col2:
    st.subheader("📊 Output & Grafik")
    
    output_container = st.container()
    
    # Eksekusi kode jika tombol run ditekan
    if run_clicked:
        with st.spinner("Menjalankan kode... (training mungkin memakan waktu)"):
            # Ambil teks terbaru dari session_state
            user_code = st.session_state[code_key]['text']
            
            # Siapkan namespace
            namespace = st.session_state.namespace.copy()
            namespace['st'] = st
            
            # Redirect stdout/stderr
            old_stdout = sys.stdout
            old_stderr = sys.stderr
            sys.stdout = mystdout = StringIO()
            sys.stderr = mystderr = StringIO()
            
            try:
                exec(user_code, namespace)
                st.session_state.namespace.update(namespace)
                st.session_state.last_output = mystdout.getvalue()
                st.session_state.last_error = mystderr.getvalue()
            except Exception:
                traceback.print_exc(file=sys.stderr)
                st.session_state.last_error = mystderr.getvalue()
                st.session_state.last_output = mystdout.getvalue()
            finally:
                sys.stdout = old_stdout
                sys.stderr = old_stderr
        
        # Tampilkan output
        with output_container:
            if st.session_state.last_error:
                with st.expander("❗ Error", expanded=True):
                    st.text(st.session_state.last_error)
            if st.session_state.last_output:
                with st.expander("📤 Output Teks", expanded=True):
                    st.text(st.session_state.last_output)
            
            # Tampilkan figure
            figures = [(name, obj) for name, obj in st.session_state.namespace.items() if isinstance(obj, plt.Figure)]
            if figures:
                st.markdown("**📈 Grafik yang Dihasilkan:**")
                for name, fig in figures:
                    with st.expander(f"Grafik: {name}", expanded=True):
                        st.pyplot(fig)
            else:
                st.info("Belum ada grafik yang dihasilkan. Pastikan kode Anda menyimpan figure ke variabel (misal: `nama_plot = fig`).")
    else:
        # Tampilkan output terakhir
        with output_container:
            if st.session_state.last_error:
                with st.expander("❗ Error Terakhir", expanded=False):
                    st.text(st.session_state.last_error)
            if st.session_state.last_output:
                with st.expander("📤 Output Teks Terakhir", expanded=False):
                    st.text(st.session_state.last_output)
            
            figures = [(name, obj) for name, obj in st.session_state.namespace.items() if isinstance(obj, plt.Figure)]
            if figures:
                st.markdown("**📈 Grafik dari Eksekusi Terakhir:**")
                for name, fig in figures[-3:]:
                    with st.expander(f"Grafik: {name}", expanded=False):
                        st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Pastikan library terinstal: `streamlit`, `pandas`, `numpy`, `matplotlib`, `scikit-learn`, `tensorflow`, `streamlit-code-editor`. Untuk menjalankan: `streamlit run app.py`")