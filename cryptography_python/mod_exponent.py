def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # Ensure base is within modulus range

    while exponent > 0:
        if exponent % 2 == 1:  # If current bit of exponent is 1
            result = (result * base) % modulus  # Multiply result by base modulo modulus
        
        base = (base * base) % modulus  # Square the base modulo modulus
        exponent //= 2  # Divide exponent by 2 (right shift)

    return result

# Example usage:
a = 200
b = 14161729
m = 2269733

# Compute a^b % m using modular exponentiation
result = modular_exponentiation(a, b, m)
print(result)  # Output: 883430

