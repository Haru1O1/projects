from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes




def aes_encrypt(key, iv, x):
   cipher = Cipher(algorithms.AES(key), modes.ECB())
   encryptor = cipher.encryptor()
   y = encryptor.update(x) + encryptor.finalize()
   return y




def aes_decrypt(key, iv, y):
   cipher = Cipher(algorithms.AES(key), modes.ECB())
   decryptor = cipher.decryptor()
   x = decryptor.update(y) + decryptor.finalize()
   return x




def main():
   key = b"sixteen_byte_key"  # 16 bytes key
   iv = b"A" * 16  # 16 bytes IV
   # plaintext blocks
   x1 = b"This is a secret"  # 16 bytes
   x2 = b"Second block x1!"
   x3 = b"This is a secret"


   x = x1 + x2 + x3
   print("Plaintext =", x)


   # Encryption
   y = aes_encrypt(key, iv, x)


   # ciphertext blocks
   for i in range(0, len(y) // 16):
       print("y" + str(i + 1) + " =", y[16 * i : 16 * (i + 1)])


   # Decryption
   decrypted_data = aes_decrypt(key, iv, y)
   print("Decrypted text =", decrypted_data)

if __name__ == "__main__":
   main()
