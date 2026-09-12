# Prime speed check
import time
import math
import array

def sqrt(x):
  return math.sqrt(x)

def speedcheck(func, inp):
  start = time.time()
  x = [i for i in func(inp)]
  end = time.time()-start
  print(end, "seconds")
  return x, end


def prime(n):
  primes = []
  num = 2
  while num <= n:
    for prime in primes:
      # Not prime
      if num//prime == num/prime:
        num += 1
        break
    else:
      primes.append(num)
      yield num
      num += 1

def primesqrt(n):
  primes = [2]
  num = 2
  while num <= n:
    #Remove int for visual
    maxsearch = sqrt(num)
    for prime in primes:
      # Passed the sqrt mark
      if prime > maxsearch:
        primes.append(num)
        yield num
        num += 1
        break
      # Not prime
      if num//prime == num/prime:
        num += 1
        break

def primesqrtodd(n):
  primes = [2]
  yield 2
  num = 3
  while num <= n:
    #Remove int for visual
    maxsearch = sqrt(num)
    for prime in primes:
      # Passed the sqrt mark
      if prime > maxsearch:
        primes.append(num)
        yield num
        num += 2
        break
      # Not prime
      if num//prime == num/prime:
        num += 1
        break

def primesqrtmod(n):
  primes = [2]
  num = 2
  while num <= n:
    #Remove int for visual
    maxsearch = sqrt(num)
    for prime in primes:
      # Passed the sqrt mark
      if prime > maxsearch:
        primes.append(num)
        yield num
        num += 1
        break
      # Not prime
      if not (num % prime):
        num += 1
        break
    else:
      print("hi")
      


maxx = 100000
#200000

#sqr0, time0 = speedcheck(prime, maxx)

sqr1, time1 = speedcheck(primesqrt, maxx)

sqr2, time2 = speedcheck(primesqrtodd, maxx)

sqr3, time3 = speedcheck(primesqrtmod, maxx)



print()
print(time1/time2, "Norm vs Odd")
print(time1/time3, "Norm vs Mod")
#print(time0/time3, "OG, vs Mod")
#print(sqr2)
#print(norm,"\n", sqr)
print("\n\n", sqr1 == sqr2, "\n\n")
print("", sqr1 == sqr3, "\n\n")
# Runtime for all primes up to 1 mil
# OG: 3 minutes
# Sqrt: 1.6 seconds
# Change to Mod: 0.95 seconds