import time

def speed(func, inp):
  start = time.time()
  x = func(*inp)
  end = time.time()-start
  print(end, "seconds")
  return x

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

maxx = 30000
a = speed(primelist, (maxx,[]))

b = primelist(10000)
c = speed(primelist, (maxx,b))

print(a[0], a[maxx-1])
print(c[0], c[maxx-1])