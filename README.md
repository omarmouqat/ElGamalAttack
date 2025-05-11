# 🔐 ElGamal Cryptosystem with Discrete Logarithm Attacks

This Streamlit app demonstrates **ElGamal encryption and decryption**, and simulates **attacks** on the cryptosystem to recover the private key using:

- Baby-step Giant-step algorithm
- Pohlig–Hellman algorithm

---

## 🧠 Features

- **Key Generation** using a predefined prime `p` and generator `g`
- **Message Encryption** using ElGamal
- **Private Key Recovery** using:
  - Baby-step Giant-step
  - Pohlig–Hellman
- **Decryption** after key recovery
- **Streamlit-based UI** for interactive exploration

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YourUsername/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies
Make sure you have Python 3 installed.
```bash
pip install streamlit sympy
```
### 3. Run the app
```bash
streamlit run elgamal_attacks.py
Replace elgamal_attacks.py with the actual filename if it's different.
```

## 💡 How It Works
### 🔐 ElGamal Algorithm
A public key (p, g, y) is generated where y = g^x mod p and x is the private key.

A message is encrypted using a random value k.

Decryption requires knowing the private key x.

## 🧨 Attacks
### 🪜 Baby-step Giant-step
A generic square root attack that solves the discrete logarithm in O(√p) time and space.

### 🧮 Pohlig–Hellman
Efficient for numbers where p-1 has small prime factors (smooth numbers). Uses the Chinese Remainder Theorem to combine solutions mod prime powers.

### 🖥️ Example
Input a short plaintext message.

Choose an attack method.

The app will:

- Encrypt the message

- Simulate recovery of the private key using the selected attack

- Decrypt the message using the recovered key


## 👤 Author
- Omar Mouqat
- Oussama Mahjour
## 🎓 Master's in Software Engineering and decision-making
## 📍 Faculty of Sciences, Rabat
