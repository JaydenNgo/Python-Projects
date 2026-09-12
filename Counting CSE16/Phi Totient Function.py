def gcd(a,b):
  if a == 0:
    return 1
  r = a%b
  while r > 0:
    a = b
    b = r
    r = a%b
  return b

def phi(n):
  a = [gcd(i,n) for i in range(1,n+1)]
  b = sum([j for j in a if j == 1])
  print(f'phi({n}) =', b)
  return b

phi(1024)