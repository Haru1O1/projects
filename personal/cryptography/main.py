from Python_Files import *

def birthday():
    print("This is the birthday paradox implementation in python.")
    print("Requires: B(output bits length), P(collision probability)\n")

    B = int(input("Enter B: "))
    P = input("Enter the collision probability (default is 0.1): ")
    if P == "":
        P = 0.1
    else:
        P = float(P)

    try:
        birthday_run(B, P)
    except:
        print("A error occured")

def bruteDLP():
    print("This is the brute force DLP implementation in python.")
    print("Requires: alpha, beta, p\n")

    alpha = int(input("Enter alpha: "))
    beta = int(input("Enter beta: "))
    p = int(input("Enter p: "))

    try:
        result = brute_DLP(alpha, beta, p)
        print(f"Result: {result}")
    except:
        print("A error occured")

def dif():
    print("This is the diffie hellman implementation in python.")
    print("Requires: p, alpha, a, and b\n")

    p = int(input("Enter p: "))
    alpha = int(input("Enter alpha: "))
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    
    try:
        diffie_run(p, alpha, a, b)
    except:
        print("A error occured")

def aes():
    print("This is the AES implementation in python.")
    key = b"sixteen_byte_key"  # 16 bytes key
    iv = b"A" * 16  # 16 bytes IV
    x1 = b"This is a secret"  # 16 bytes
    x2 = b"Second block x1!"
    x3 = b"This is a secret"
    x = x1 + x2 + x3
    print("Plaintext =", x)

    try:
        y = aes_encrypt(key, iv, x)
        for i in range(0, len(y) // 16):
            print("y" + str(i + 1) + " =", y[16 * i : 16 * (i + 1)])
        decrypted_data = aes_decrypt(key, iv, y)
        print("Decrypted text =", decrypted_data)
    except:
        print("A error occured")

def affinecipher():
    print("This is the affine cipher implementation in python.")
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    try:
        bruteforce(x, y)
    except:
        print("A error occured")

def des():
    print("This is the DES implementation in python.")
    pt = input("Enter plaintext (in hex): ")
    key = input("Enter key (in hex): ")

    try:
        # Key generation
        key_bin = hex2bin(key)
        keyp = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
        key_bin = permute(key_bin, keyp, 56)
        shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        key_comp = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
        left = key_bin[0:28]
        right = key_bin[28:56]
        rkb = []
        rk = []
        for i in range(0, 16):
            left = shift_left(left, shift_table[i])
            right = shift_left(right, shift_table[i])
            combine_str = left + right
            round_key = permute(combine_str, key_comp, 48)
            rkb.append(round_key)
            rk.append(bin2hex(round_key))

        # Encryption
        cipher_text = bin2hex(encrypt(pt, rkb, rk))
        print("Cipher Text: ", cipher_text)

        # Decryption
        rkb_rev = rkb[::-1]
        rk_rev = rk[::-1]
        text = bin2hex(encrypt(cipher_text, rkb_rev, rk_rev))
        print("Plain Text: ", text)
    except Exception as e:
        print("An error occurred:", e)

def dlp_shanks():
    print("This is the DLP Shanks implementation in python.")
    print("Requires: alpha, beta, p\n")

    alpha = int(input("Enter alpha: "))
    beta = int(input("Enter beta: "))
    p = int(input("Enter p: "))

    try:
        result = shank_bsgs(alpha, beta, p)
        print(f"Result: {result}")
    except Exception as e:
        print("An error occurred:", e)

def eea():
    print("This is the EEA implementation in python.")
    print("Requires: r0, r1\n")

    r0 = int(input("Enter r0: "))
    r1 = int(input("Enter r1: "))

    try:
        result = EEA(r0, r1)
        x0, y0, z0 = result
        print("\nEEA(", r0, ",", r1, ")", sep="")
        print("Result =", result)
        if x0 != 1:
            print("The inverse of ", r1, " in mod ", r0, " does not exist", sep ="")
        elif x0 == 1 and z0 > 0:
            print("The inverse of ", r1, " in mod ", r0, " is ", z0, sep="")
        else:
            print("The inverse of ", r1, " in mod ", r0, " is ", r0 + z0, sep="")
    except Exception as e:
        print("An error occurred:", e)

def elgamal_signature():
    print("This is the Elgamal signature implementation in python.")
    p = int(input("Enter prime modulus p: "))
    alpha = int(input("Enter generator alpha: "))
    beta = int(input("Enter public key component beta: "))
    d = int(input("Enter private key d: "))
    message = int(input("Enter message to be signed: "))
    k = int(input("Enter ephemeral key k: "))

    try:
        signature = elgamal_sign(p, alpha, beta, d, message, k)
        print("Generated Signature (r, s):", signature)
    except Exception as e:
        print("An error occurred:", e)

def ellipticCurveFinite():
    print("This is the elliptic curve finite implementation in python.")
    a = int(input("Enter curve parameter a: "))
    b = int(input("Enter curve parameter b: "))
    r = int(input("Enter prime modulus r: "))

    try:
        points = []
        for x_val in range(r):
            for y_val in range(r):
                if (y_val**2 - x_val**3 - a*x_val - b) % r == 0:
                    points.append((x_val, y_val))
        print("Points on the curve:")
        for point in points:
            print(point)
    except Exception as e:
        print("An error occurred:", e)

def ellipticIntersection():
    print("This is the elliptic intersection implementation in python.")
    p = int(input("Enter prime modulus p: "))
    m = int(input("Enter slope m: "))
    b = int(input("Enter y-intercept b: "))

    try:
        intersection_points = solve_intersection_points(p, m, b)
        print("Intersection points:", intersection_points)
    except Exception as e:
        print("An error occurred:", e)

def ellipticPointAddition():
    print("This is the elliptic point addition implementation in python.")
    p = int(input("Enter prime modulus p: "))
    a = int(input("Enter curve parameter a: "))
    b = int(input("Enter curve parameter b: "))
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    try:
        s = 0
        if (x1 == x2):
            s = ((3 * (x1 ** 2) + a) * modinv(2 * y1, p)) % p
        else:
            s = ((y2 - y1) * modinv(x2 - x1, p)) % p
        x3 = (s ** 2 - x1 - x2) % p
        y3 = (s * (x1 - x3) - y1) % p
        print("Resulting point: (", x3, ",", y3, ")", sep="")
    except Exception as e:
        print("An error occurred:", e)

def mod_exponent():
    print("This is the modular exponentiation implementation in python.")
    base = int(input("Enter base: "))
    exponent = int(input("Enter exponent: "))
    modulus = int(input("Enter modulus: "))

    try:
        result = modular_exponentiation(base, exponent, modulus)
        print("Result:", result)
    except Exception as e:
        print("An error occurred:", e)

def mod_Multi_Inverse():
    print("This is the modular multiplicative inverse implementation in python.")
    A = int(input("Enter A: "))
    M = int(input("Enter M: "))

    try:
        result = modInverse(A, M)
        print("Result:", result)
    except Exception as e:
        print("An error occurred:", e)

def phi():
    print("This is the Euler's totient function implementation in python.")
    n = int(input("Enter n: "))

    try:
        result = totient(n)
        print("phi(", n, ") = ", result, sep="")
    except Exception as e:
        print("An error occurred:", e)

def primitive_elements():
    print("This is the primitive elements implementation in python.")
    n = int(input("Enter n: "))

    try:
        result = primitive_elm(n)
        print("Primitive elements:", result)
    except Exception as e:
        print("An error occurred:", e)

def rsa():
    print("This is the RSA implementation in python.")
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))
    e = int(input("Enter public exponent e: "))
    original_message = int(input("Enter original message: "))

    try:
        n = p * q
        rsa_encrypt(p, q, e, n, original_message)
        encrypted_message = int(input("Enter encrypted message: "))
        rsa_decrypt(p, q, e, n, encrypted_message)
    except Exception as e:
        print("An error occurred:", e)

def trivium():
    print("This is the Trivium implementation in python.")
    key = [int(x) for x in input("Enter key (80 bits): ").split()]
    IV = [int(x) for x in input("Enter IV (80 bits): ").split()]

    try:
        A = [0 for _ in range(LENGTH_A)]
        B = [0 for _ in range(LENGTH_B)]
        C = [0 for _ in range(LENGTH_C)]

        A, B, C = initialize(key, IV, A, B, C)
        warmup(A, B, C)
        print("Generated bits:")
        for _ in range(200):
            output = shift(A, B, C)
            print(output, end='')
        print()
    except Exception as e:
        print("An error occurred:", e)

def help():
    print("Available options:")
    print("1 : Diffie-Hellman")
    print("2 : Birthday Paradox")
    print("3 : AES")
    print("4 : Affine Cipher")
    print("5 : DES")
    print("6 : Brute Force DLP")
    print("7 : DLP Shanks")
    print("8 : EEA")
    print("9 : Elgamal Signature")
    print("10 : Elliptic Curve Finite")
    print("11 : Elliptic Intersection")
    print("12 : Elliptic Point Addition")
    print("13 : Modular Exponentiation")
    print("14 : Modular Multiplicative Inverse")
    print("15 : Euler's Totient Function")
    print("16 : Primitive Elements")
    print("17 : RSA")
    print("18 : Trivium")

def main():
    options = {
        0 : help,
        1 : dif,
        2 : birthday,
        3 : aes,
        4 : affinecipher,
        5 : des,
        6 : bruteDLP,
        7 : dlp_shanks,
        8 : eea,
        9 : elgamal_signature,
        10 : ellipticCurveFinite,
        11 : ellipticIntersection,
        12 : ellipticPointAddition,
        13 : mod_exponent,
        14 : mod_Multi_Inverse,
        15 : phi,
        16 : primitive_elements,
        17 : rsa,
        18 : trivium,
    }
    
    while True:
        print("\nPlease choose what to solve by entering a number (0 for help, 'quit' to exit)")
        choice = input("Enter your choice: ")
        
        if choice.lower() == 'quit':
            print("Exiting the program.")
            break
        
        try:
            choice = int(choice)
            if choice in options:
                options[choice]()
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter a number or 'quit' to exit.")

if __name__ == "__main__":
    main()