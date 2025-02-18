# import totient() method from sympy 
from sympy.functions.combinatorial.numbers import totient

n = 720 # phi(n)

# Use totient() method 
totient_n = totient(n) 

def main():
    print("phi({}) = {} ".format(n, totient_n)) 

if __name__ == "__main__":
    main()