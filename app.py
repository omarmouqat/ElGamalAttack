import streamlit as st
import random
import math
from sympy import mod_inverse
from sympy.ntheory import factorint
from sympy.ntheory.modular import crt

# ElGamal encryption functions
def key_generation(g, p):
    x = random.randint(1, p - 2)
    y = pow(g, x, p)
    return (p, g, y), x

def encryption(message, public_key):
    p, g, y = public_key
    k = random.randint(1, p - 2)
    c1 = pow(g, k, p)
    ciphertext = [(c1, (ord(char) * pow(y, k, p)) % p) for char in message]
    return ciphertext

def decryption(ciphertext, private_key, public_key):
    p, g, y = public_key
    decrypted_message = [chr(c2 * mod_inverse(pow(c1, private_key, p), p) % p) for c1, c2 in ciphertext]
    return ''.join(decrypted_message)

# Attack 1: Baby-step Giant-step
def baby_step_giant_step(g, y, p):
    m = math.isqrt(p) + 1
    table = {}
    for j in range(m):
        table[pow(g, j, p)] = j
    g_inv = pow(g, -m, p)
    gamma = y
    for i in range(m):
        if gamma in table:
            return i * m + table[gamma]
        gamma = (gamma * g_inv) % p
    return None

# Attack 2: Pohlig–Hellman
def dlog_mod_prime_power(g, y, p, q, e):
    x = 0
    g_inv = mod_inverse(g, p)
    for k in range(e):
        h = (pow(g_inv, x, p) * y) % p
        h_k = pow(h, (p - 1) // (q ** (k + 1)), p)
        g_k = pow(g, (p - 1) // (q ** (k + 1)), p)
        for d in range(q):
            if pow(g_k, d, p) == h_k:
                x += d * (q ** k)
                break
    return x

def pohlig_hellman(g, y, p):
    factors = factorint(p - 1)
    congruences = []
    moduli = []
    for q, e in factors.items():
        x_q = dlog_mod_prime_power(g, y, p, q, e)
        congruences.append(x_q)
        moduli.append(q ** e)
    x, _ = crt(moduli, congruences)
    return x

# Streamlit interface
st.title("🔐 ElGamal Decryption using Attacks")

# Generate keys
p = 467
g = 2
public_key, private_key = key_generation(g, p)
y = public_key[2]

# Input
message = st.text_input("Enter a message to encrypt:")
attack_method = st.selectbox("Choose an attack to recover the private key:", ["Baby-step Giant-step", "Pohlig–Hellman"])

if message:
    # Encrypt message
    ciphertext = encryption(message, public_key)
    st.write("### 🔒 Ciphertext:")
    st.write(str(ciphertext))

    # Try attack
    if attack_method == "Baby-step Giant-step":
        recovered_key = baby_step_giant_step(g, y, p)
    else:
        recovered_key = pohlig_hellman(g, y, p)

    if recovered_key is not None:
        st.success(f"Recovered Private Key: {recovered_key}")
        decrypted = decryption(ciphertext, recovered_key, public_key)
        st.write("### 🔓 Decrypted Message: ")
        st.success(decrypted)
    else:
        st.error("Failed to recover the private key.")
