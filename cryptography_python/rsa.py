# import totient() method from sympy
from sympy.ntheory.factor_ import totient
import math
 
# calculate phi(n) for a given number n
def phi(n):
   result = n;
   for i in range(2, sqrt(n) + 1):
       if n % i == 0:
           while n % i == 0:
               n /= i;
           result -= result / i
   if n > 1:
       result -= result / n
   return result
 
# calculate gcd(a, b) using the Euclidean algorithm
def gcd(a, b):
   if b == 0:
       return a
   return gcd(b, a % b)
 
# calculate a^b mod m using modular exponentiation
def modpow(a, b, m):
   result = 1
   while b > 0:
       if b & 1:
           result = (result * a) % m
       a = (a * a) % m
       b >>= 1
   return result

def getModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def encrypt(p, q, e, n, original_message):
    encrypted = modpow(original_message, e, n)
    print("Encrypted message: ", encrypted)

def decrypt(p, q, e, n, encrypted):
    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    d = getModInverse(e, phi)
    decrypted = modpow(encrypted, d, n)
    print("Decrypted message: ", decrypted)

def get_privatekey(e, phi):
   d = 0
   while(True):
       if (e * d % phi) == 1:
           return d
       d += 1

def main():
   p = 5
   q = 13
   n = p * q
   e = 5
   phi = (p - 1) * (q - 1)
   original_message = 9
   #encrypted_message = 24
   
   print("private key is ", get_privatekey(e, phi), sep="")

   encrypt(p, q, e, n, original_message)
   #decrypt(p, q, e, n, encrypted_message)

if __name__ == "__main__":
    main()
