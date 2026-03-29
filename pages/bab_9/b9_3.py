import streamlit as st
import string

# Fungsi Caesar cipher
def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

# Fungsi untuk membuat tabel visual pergeseran huruf
def create_alphabet_table(shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = ""
    for i in range(0, 26, 5):  # tampilkan per 5 huruf agar rapi
        orig = alphabet[i:i+5]
        shifted = shifted_alphabet[i:i+5]
        table += f"| {orig} → {shifted} |\n"
    return table

st.set_page_config(page_title="Visualisasi Enkripsi Caesar", layout="wide")
st.title("🔐 Visualisasi Cara Kerja Enkripsi")
st.markdown("""
Enkripsi adalah proses mengubah pesan asli (**plaintext**) menjadi pesan rahasia (**ciphertext**) 
menggunakan **kunci**. Di sini kita menggunakan **Caesar Cipher**, yaitu dengan menggeser setiap huruf 
sejumlah langkah tertentu.
""")

# Input dari pengguna
plaintext = st.text_input("✍️ Masukkan pesan asli (plaintext):", "hello world")
shift = st.slider("🔑 Pilih kunci (jumlah pergeseran):", 0, 25, 3)

# Hitung ciphertext
ciphertext = caesar_cipher(plaintext, shift)

# Tampilkan hasil
col1, col2 = st.columns(2)
with col1:
    st.subheader("📝 Plaintext")
    st.code(plaintext, language="text")
with col2:
    st.subheader("🔒 Ciphertext")
    st.code(ciphertext, language="text")

# Visualisasi tabel pergeseran huruf
st.subheader("📊 Bagaimana pergeseran terjadi?")
st.markdown(f"**Kunci = {shift}** berarti setiap huruf digeser **{shift}** langkah ke kanan.")
st.markdown("Tabel pergeseran huruf (hanya huruf kecil untuk contoh):")
st.markdown(create_alphabet_table(shift))

# Penjelasan langkah per langkah
st.subheader("🧠 Penjelasan Langkah demi Langkah")
if plaintext:
    explanation = []
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shifted_char = ciphertext[i]
            orig_ord = ord(char.lower()) - ord('a')
            new_ord = (orig_ord + shift) % 26
            explanation.append(f"• `{char}` (posisi {orig_ord}) → geser {shift} → `{shifted_char}` (posisi {new_ord})")
        else:
            explanation.append(f"• `{char}` (bukan huruf) tetap `{char}`")
    st.markdown("\n".join(explanation))