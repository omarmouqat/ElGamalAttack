from sympy import mod_inverse
from sympy.ntheory import factorint
from sympy.ntheory.modular import crt
import math


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