# import totient() method from sympy 
from sympy.ntheory.factor_ import totient 

n = 720 # phi(n)

# Use totient() method 
totient_n = totient(n) 
	
print("phi({}) = {} ".format(n, totient_n)) 

