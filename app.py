import streamlit as st
import ElGamal
import Attacks


# Streamlit interface
st.title("🔐 ElGamal Decryption using Attacks")

# Generate keys
p = 467

# Input
message = st.text_input("Enter a message to encrypt:")
Private_key = st.number_input("Enter the private key (Leave 0 for random):", min_value=0, max_value=p-2,value=0)
private_key = Private_key
public_key, private_key = ElGamal.generate_key(private_key, p)
attack_method = st.selectbox("Choose an attack to recover the private key:", ["Baby-step Giant-step", "Pohlig–Hellman"])

if message:
    # Encrypt message
    ciphertext = ElGamal.encrypte(message, public_key)
    st.write("### 🔒 Ciphertext:")
    st.write(str(ciphertext))

    # Try attack
    if attack_method == "Baby-step Giant-step":
        recovered_key = Attacks.baby_step_giant_step(public_key)
    else:
        recovered_key = Attacks.pohlig_hellman(public_key)

    if recovered_key is not None:
        st.success(f"Recovered Private Key: {recovered_key}")
        print("### 🔑 Recovered Key: ", recovered_key)
        print("### 🔑 Private Key: ", private_key)
        decrypted = ElGamal.decrypte(ciphertext, recovered_key, public_key)
        st.write("### 🔓 Decrypted Message: ")
        st.success(decrypted)
        st.success(ElGamal.decrypte(ciphertext, private_key, public_key))
        
    else:
        st.error("Failed to recover the private key.")


