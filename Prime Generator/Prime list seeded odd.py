import math
import time

# Conclusion, using +2 when at a prime doesn't affect run time

def speed(func, inp):
  start = time.time()
  x = func(*inp)
  end = time.time()-start
  print(end, "seconds")
  return x

def printList(list):
  print(f"{list[0]}, {list[1]}, ... , {list[-2]}, {list[-1]}")

def primelist(n, seed = []):
  primes = seed
  length = len(seed)
  if length == 0:
    num = 2
  else:
    num = seed[-1]
  count = length
  while count < n:
    for prime in primes:
      # Not prime
      if num//prime == num/prime:
        num += 1
        break
    else:
      primes.append(num)
      num += 1
      count += 1
  
  return primes

def primelistOdd(n, seed):
  primes = seed
  length = len(seed)
  if length == 0:
    num = 3
  else:
    num = seed[-1]
  count = length
  while count < n:
    for prime in primes:
      # Not prime
      if num//prime == num/prime:
        num += 1
        break
    # If is prime
    else:
      primes.append(num)
      num += 2
      count += 1
  
  return primes

maxx = 20000
see2 = primelist(10000,[])
print("Seeded", len(see2))
c = speed(primelistOdd, (maxx,[2]))
d = speed(primelistOdd, (maxx,see2))

see = primelist(10000,[])
print("Seeded")
a = speed(primelist, (maxx,[]))
b = speed(primelist, (maxx,see))




printList(a)
printList(b)
printList(c)
printList(d)


