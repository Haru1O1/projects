from python_files import *

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
    print()

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

def main():
    print("Please choose what to solve by entering a number")
    options = {
        1 : dif,
        2 : birthday,
    }
    options[2]()

main()