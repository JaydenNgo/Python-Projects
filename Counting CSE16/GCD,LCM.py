def gcd(a,b):
  a0 = a
  b0 = b
  r = a%b
  while r > 0:
    a = b
    b = r
    r = a%b
  print('gcd', b, ', lcm', int((a0*b0)/b))


gcd(3,8)