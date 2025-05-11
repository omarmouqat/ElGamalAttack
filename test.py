import streamlit as st
import ElGamal
from random import randint
import ast
from sympy import isprime


def Encrypt():
    st.write("### 🔒 Encryption ")
    clear_text = st.text_input("Enter a message to encrypt:")
    p_col, g_col,y_col = st.columns(3)
    with p_col:
        p = st.number_input("P:",value=0)
    with g_col:
        g = st.number_input("G:",value=0)
    with y_col:
        y = st.number_input("Y:",value=0)
    
    
    if st.button("Encrypt"):   
        if not clear_text:
            st.error("Please enter a message to encrypt.")
        elif not p:
            st.error("Please enter a prime number.")
        else:   
            if not isprime(p):
                st.error("p should be a prime number.")
                return
            
            ciphertext = ElGamal.encrypte(clear_text, (p, g, y))
            st.write("#### 🔒 Ciphertext:")
            st.success(ciphertext)
            
        


def Decrypt():
    st.write("### 🔒 Decryption:")
    ciphertext = st.text_input("Enter a message to decrypt:")
    p_col,g_col,y_col,x_col = st.columns(4)
    with p_col:
        p = st.number_input("P:",value=0)
    with g_col:
        g = st.number_input("G:",value=0)
    with y_col:
        y = st.number_input("Y:",value=0)
    with x_col:
        x = st.number_input("Private Key:",value=0)
        

    if st.button("Decrypt"):
        if not p:
            st.error("Please enter a prime number.")
        else:   
            if not isprime(p):
                st.error("p should be a prime number.")
                return
            if x == 0:
                x =randint(1, p - 2)
            if x >= p:
                st.error("Private key should be less than p.")
                return
            if x < 1:
                st.error("Private key should be greater than 0.")
                return
            
           
            ciphertext = ast.literal_eval(ciphertext)
            if not isinstance(ciphertext[0], int) or not isinstance(ciphertext[1], list):
                st.error("Invalid ciphertext format. The first element should be an integer and the second element should be a list.")
                return
            public_key = (p, g, y)
            cleartext = ElGamal.decrypte(ciphertext=ciphertext,private_key=x,public_key=public_key)
            st.write("#### 🔒 Decrypted Message:")
            st.success(cleartext)
   

def Attack():
    st.write("### 🔒 Ciphertext:")
    st.text_input("Enter a message to attack:")

def GenerateKey():
    st.write("### 🔒 Key Generation:")
    p_col, x_col = st.columns(2)
    with p_col:
        p = st.number_input("Enter a prime number (p):",value=0)
    with x_col:
        x = st.number_input("Enter the private key (Leave 0 for random):",value=0)
    
    if st.button("Generate Key"):   
        if not p:
            st.error("Please enter a prime number.")
        else:   
            if not isprime(p):
                st.error("p should be a prime number.")
                return
            if x == 0:
                x =randint(1, p - 2)
            if x >= p:
                st.error("Private key should be less than p.")
                return
            if x < 1:
                st.error("Private key should be greater than 0.")
                return
            
            public_key, private_key = ElGamal.generate_key(x, p)
            st.write(f"#### 🔒 Public Key:          (p={str(public_key[0])}, g={str(public_key[1])}, y={str(public_key[2])})")
            st.write(f"#### 🔒 Private Key:         {private_key}")

if __name__ == "__main__":
    st.title("🔐 ElGamal Algorithm")
    selection =st.segmented_control("", options=["Keys","Encrypt", "Decrypt","Attack"],selection_mode="single",default="Keys")
    if selection == "Encrypt":
        Encrypt()
    elif selection == "Keys":
        GenerateKey()
    elif selection == "Decrypt":
        Decrypt()
    elif selection == "Attack":
        Attack()
