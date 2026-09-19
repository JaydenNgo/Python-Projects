import sys
import math
sys.setrecursionlimit(10**5)

def sqrt(x):
  return math.sqrt(x)



def f(n):
  if n == 1:
    return 1
  else:
    return sqrt(n+f(n-1))

print((f(999)))
print((f(1000)))
