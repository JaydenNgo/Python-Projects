import math
import time

def primesqrt():
  primes = [2]
  num = 2
  yield num
  while True:
    #Remove int for visual
    maxsearch = math.sqrt(num)
    for prime in primes:
      # Not prime
      if not num%prime:
        num += 1
        break
      # Passed the sqrt mark
      if prime > maxsearch:
        primes.append(num)
        yield num
        num += 1
        break
      
def count(dict, n):
  if n not in dict:
    dict[n] = 1
  else:
    dict[n] += 1


def fta(n):   
  prime_count = {}
  max_search = math.isqrt(n)+1
  for num in primesqrt():
    #print(num, max_search)
    if num > max_search:
      count(prime_count, n)
      break
    while (not n%num):
      n = n//num
      max_search = math.isqrt(n)+1
      count(prime_count, num)
      #print(n)

  #for k,v in prime_count.items():
    #print(k,'^', v)
  if 1 in prime_count:
    prime_count.pop(1)
  return prime_count

def check(dict):
  a = 1
  for k,v in dict.items():
    a *= k**v
  #print(a)
  return a

number = 1234567891011121315562
ftas = {i:max(fta(i)) for i in range(2,250)}
for k,v in ftas.items():
  print(k,v)



