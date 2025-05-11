import random
from sympy import mod_inverse



def generate_key(g, p):
    x = random.randint(1, p - 2)
    y = pow(g, x, p)
    return (p, g, y), x

def encrypte(message, public_key):
    p, g, y = public_key
    k = random.randint(1, p - 2)
    c1 = pow(g, k, p)
    ciphertext = [(c1, (ord(char) * pow(y, k, p)) % p) for char in message]
    return ciphertext

def decrypte(ciphertext, private_key, public_key):
    p, g, y = public_key
    decrypted_message = [chr(c2 * mod_inverse(pow(c1, private_key, p), p) % p) for c1, c2 in ciphertext]
    return ''.join(decrypted_message)