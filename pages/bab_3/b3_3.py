import streamlit as st
import hashlib

st.set_page_config(page_title="Blockchain Simulator", layout="wide")

st.title("🔗 Blockchain Simulator (Stable Version)")

DIFFICULTY = 3

# =============================
# HASH FUNCTION
# =============================
def calculate_hash(index, data, prev_hash, nonce):
    return hashlib.sha256(
        f"{index}{data}{prev_hash}{nonce}".encode()
    ).hexdigest()

# =============================
# MINE FUNCTION
# =============================
def mine_block(index, data, prev_hash):
    nonce = 0
    while True:
        hash_result = calculate_hash(index, data, prev_hash, nonce)
        if hash_result.startswith("0" * DIFFICULTY):
            return nonce, hash_result
        nonce += 1

# =============================
# VALIDATE CHAIN
# =============================
def validate_chain(chain):
    for i in range(len(chain)):

        block = chain[i]

        recalculated = calculate_hash(
            block["index"],
            block["data"],
            block["prev_hash"],
            block["nonce"]
        )

        # hash harus cocok
        if recalculated != block["stored_hash"]:
            return False

        # difficulty
        if not block["stored_hash"].startswith("0" * DIFFICULTY):
            return False

        # koneksi antar block
        if i > 0:
            if block["prev_hash"] != chain[i-1]["stored_hash"]:
                return False

    return True

# =============================
# INITIALIZE CHAIN (SEMUA VALID)
# =============================
if "chain" not in st.session_state:

    chain = []

    # Genesis
    nonce, hash_val = mine_block(0, "Genesis Block", "0")

    chain.append({
        "index": 0,
        "data": "Genesis Block",
        "prev_hash": "0",
        "nonce": nonce,
        "stored_hash": hash_val
    })

    # Block 1 & 2
    for i in range(1, 3):
        prev_hash = chain[i-1]["stored_hash"]
        data = f"Block {i} Data"
        nonce, hash_val = mine_block(i, data, prev_hash)

        chain.append({
            "index": i,
            "data": data,
            "prev_hash": prev_hash,
            "nonce": nonce,
            "stored_hash": hash_val
        })

    st.session_state.chain = chain

# =============================
# DISPLAY BLOCKS
# =============================
cols = st.columns(3)

for i in range(3):

    block = st.session_state.chain[i]

    with cols[i]:
        with st.container(border=True):

            st.subheader(f"Block {i}")

            # INPUT DATA (sementara)
            new_data = st.text_area(
                "Data",
                value=block["data"],
                key=f"data_{i}"
            )

            new_nonce = st.number_input(
                "Nonce",
                value=block["nonce"],
                key=f"nonce_{i}"
            )

            # HITUNG HASH SEMENTARA
            current_hash = calculate_hash(
                block["index"],
                new_data,
                block["prev_hash"],
                new_nonce
            )

            st.write("Previous Hash:")
            st.code(block["prev_hash"])

            st.write("Stored Hash (hasil mining):")
            st.code(block["stored_hash"])

            st.write("Current Hash (live edit):")
            st.code(current_hash)

            # VALIDASI INDIVIDUAL
            if current_hash == block["stored_hash"]:
                st.success("Valid Block ✅")
            else:
                st.error("Invalid Block ❌")

            # SIMPAN DATA TAPI JANGAN UBAH STORED HASH
            block["data"] = new_data
            block["nonce"] = new_nonce

            # TOMBOL MINE
            if st.button("⛏ Mine Block", key=f"mine_{i}"):

                nonce, hash_val = mine_block(
                    block["index"],
                    block["data"],
                    block["prev_hash"]
                )

                block["nonce"] = nonce
                block["stored_hash"] = hash_val

                # update next block prev_hash (seperti blockchain asli)
                if i + 1 < 3:
                    st.session_state.chain[i+1]["prev_hash"] = hash_val

                st.rerun()

# =============================
# GLOBAL VALIDATION
# =============================
st.markdown("---")

if validate_chain(st.session_state.chain):
    st.success("Blockchain VALID ✅")
else:
    st.error("Blockchain RUSAK ❌")