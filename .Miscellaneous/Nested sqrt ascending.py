import math
import sys

sys.setrecursionlimit(10**5)

def f(n,c):
  if n == c:
    return math.sqrt(c)
  else:
    return math.sqrt(n+f(n+1,c))

print(f(1,10**4))
