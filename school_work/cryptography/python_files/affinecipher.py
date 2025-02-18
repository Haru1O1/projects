def inverse(a):
  inverseFound = -1
  for i in range(26):
      if ( (a * i) % 26 == 1 ):
          inverseFound = i
          break
  return (inverseFound)

def bruteforce(x, y):
  for a in range(1, 26, 1):
      for b in range(26):
           if ( (a * x + b) % 26 == y and inverse(a) * (y-b) % 26 == x):
               print (a, b)
               
def main():
  bruteforce(1, 23)

if __name__ == "__main__":
  main()
