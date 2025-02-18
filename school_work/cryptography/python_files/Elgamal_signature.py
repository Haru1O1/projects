import random

def mod_exp(base, exp, mod):
    # Modular exponentiation: base^exp % mod
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def mod_inverse(a, m):
    # Modular inverse of a mod m using extended Euclidean algorithm
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def elgamal_sign(p, alpha, beta, d, x, k):
    # Generate ElGamal signature (r, s) for message x using ephemeral key k
    r = mod_exp(alpha, k, p)
    k_inv = mod_inverse(k, p-1)
    if k_inv is None:
        raise ValueError("Ephemeral key k does not have a valid inverse modulo p-1")
    s = ((x - d * r) % (p-1)) * k_inv % (p-1)
    return (r, s)

def main():
    # Example usage:
    p = 29  # A large prime modulus (must be a safe prime for security)
    alpha = 6       # Generator of the multiplicative group Z_p^*
    d = 12  # Private key
    beta = 17  # Public key component beta

    message = 5  # Message to be signed (an integer)
    k = 39  # Ephemeral key (random integer)
    # Generate ElGamal signature
    signature = elgamal_sign(p, alpha, beta, d, message, k)
    print("Generated Signature (r, s):", signature)

if __name__ == "__main__":
   main()