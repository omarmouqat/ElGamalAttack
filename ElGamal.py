from random import randint
from sympy import mod_inverse
from sympy import isprime, primitive_root

def generate_key(private_key:int,p:int):
    """Generate public"""
    g = primitive_root(p)  
    y = pow(g, private_key, p)  
    return (p, g, y), private_key



def encrypte(message, public_key):
    p, g, y = public_key
    k = randint(1, p - 2)
    c2 = []
    c1 = pow(g, k, p)
    for char in message:
        m = (ord(char) * pow(y, k, p)) % p
        c2+= [m]
    return c1,c2

def decrypte(ciphertext, private_key, public_key):
    p, g, y = public_key
    decrypted_message=""
    c1 = ciphertext[0]
    for c2 in ciphertext[1]:
        s = pow(c1, private_key, p) 
        #Test
        s_inv = mod_inverse(s, p)  
        m = (c2 * s_inv) % p
        decrypted_message+= chr(m)
    return decrypted_message

