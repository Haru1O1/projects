def EEA(r0, r1):
   # initial values
   # (r0, s0, t0) <--> r0 = 1*r0 + 0*r1
   # (r1, s1, t1) <--> r1 = 0*r0 + 1*r1
   s0 = 1
   t0 = 0
   s1 = 0
   t1 = 1
   while r1 > 0:
       q = r0 // r1
       r2 = r0 - q * r1
       s2 = s0 - q * s1
       t2 = t0 - q * t1
       # rename
       r0, r1 = r1, r2
       s0, s1 = s1, s2
       t0, t1 = t1, t2
      
   return r0, s0, t0
  
def main():
   r0 = 9876543210001234
   r1 = 1234567890123
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
  
if __name__ == "__main__":
   main()

