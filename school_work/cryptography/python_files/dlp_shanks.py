def shank_bsgs(alpha, beta, p):
   m = int(p ** 0.5) + 1
   a_table = {}
   alpha_inv = pow(alpha, m * (p - 2), p)

   for xb in range(m):
      a_table[pow(alpha, xb, p)] = xb

   for xg in range(m):
      axb = (beta * pow(alpha_inv, xg, p)) % p
      if axb in a_table:
         xb = a_table[axb]
         x = xg * m + xb
         print(x,",",xb,",",xg, sep="")
         return x
   return None
shank_bsgs(41, 12959645, 100000081)
shank_bsgs(105, 308, 701)
shank_bsgs(3, 18, 19)
shank_bsgs(6,8,17)
#shank_bsgs(105, 308, 701)
