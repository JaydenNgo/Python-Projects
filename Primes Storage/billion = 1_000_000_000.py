import time

def time_it(func, input):
  start = time.time()
  out = func(input)
  print(time.time()-start)
  return out
# Takes in a binary list and turns all composite numbers to 0
# Note: you can take existing binary list, and append new 1's which extends the list
# Modifies the input list in place
# returns a list of prime numbers up to the length of the list
def full_clears(l):
  l[0] = l[1] = 0
  primes = []
  for i in range(len(l)):
    if l[i]:  #if is prime
      primes.append(i)
      #clear all divisible by said prime
      for j in range(i+i,len(l),i):
        l[j] = 0
  return primes

def full_clears_half(l):
  l[0] = l[1] = 0
  primes = []
  mid = len(l)//2+1
  for i in range(len(l)):
    if l[i]:  #if is prime
      if i > mid:
        primes += [i for i in range(mid,len(l)) if l[i]]
        break
      primes.append(i)
      #clear all divisible by said prime
      for j in range(2*i,len(l),i):
        l[j] = 0
  return primes

def full_skip_clears(l):
  l[0] = l[1] = 0
  primes = []
  prod = 1
  for i in range(len(l)):
    if l[i]:  #if is prime
      primes.append(i)
      prod *= i
      #clear all divisible by said prime
      for j in range(i+prod,len(l),prod):
        l[j] = 0
      
  return primes

length = 1_000
b = [1 for _ in range(length)]
c = [1 for _ in range(length)]
d = [1 for _ in range(length)]

bp = time_it(full_clears, b)
cp = time_it(full_clears_half, c)
dp = time_it(full_skip_clears, d)

print(f"{bp}\n")
print(f"{cp}\n")
print(f"{dp}\n")
print(f" Diff1: {set(bp)-set(cp)}")
print(f" Diff2: {list(set(bp)^set(dp))}")

print(f"Check: {bp == cp}")
print(f"Check: {bp == dp}")