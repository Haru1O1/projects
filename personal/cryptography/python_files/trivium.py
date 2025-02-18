import random

LENGTH_A = 93
LENGTH_B = 84
LENGTH_C = 111

def initialize(key, IV, A, B, C):
  A = IV + [0] * (LENGTH_A - 80)
  B = key + [0] * (LENGTH_B - 80)
  C = [0] * (LENGTH_C - 3) + [1, 1, 1]
  return A, B, C

def shift(A, B, C):
  out_A = A[65] ^ (A[90] & A[91]) ^ A[92]
  out_B = B[68] ^ (B[81] & B[82]) ^ B[83]
  out_C = C[65] ^ (C[108] & C[109]) ^ C[110]

  in_A = out_C ^ A[68]
  in_B = out_A ^ B[77]
  in_C = out_B ^ C[86]

  # Shift registers
  A.insert(0, in_A)
  A.pop()

  B.insert(0, in_B)
  B.pop()

  C.insert(0, in_C)
  C.pop()

  output = out_A ^ out_B ^ out_C
  return output

def warmup(A, B, C):
  for _ in range(4 * (LENGTH_A + LENGTH_B + LENGTH_C)):
     shift(A, B, C)

def main():
  A = [0 for _ in range(LENGTH_A)]
  B = [0 for _ in range(LENGTH_B)]
  C = [0 for _ in range(LENGTH_C)]

  key = [random.randint(1, 1) for _ in range(80)]
  IV = [random.randint(1, 1) for _ in range(80)]

  A, B, C = initialize(key, IV, A, B, C)
  assert A == IV + [0] * (LENGTH_A - 80)  # 80 1s followed by 13 0s
  assert B == key + [0] * (LENGTH_B - 80)  # 80 1s followed by 4 0s
  assert C == [0] * (LENGTH_C - 3) + [1, 1, 1]  # all zeros except the last three

  warmup(A, B, C)
  assert A == [1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0]

  # Generate the first 200 bits
  for _ in range(8):
    output = shift(A, B, C)
    print(output, end='')

if __name__ == "__main__":
  main()

