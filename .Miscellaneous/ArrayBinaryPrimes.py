import array
import math

def sqrt(x):
  return math.sqrt(x)


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

def save(listt, file):
  if file[-4:] != ".bin":
    file += ".bin"
  numbers = array.array('d', listt)
  with open(file, 'wb') as f:
    numbers.tofile(f)

  
def extract(file):
  if file[-4:] != ".bin":
    file += ".bin"
  new_arr = array.array('d')
  with open(file, 'rb') as f:
    try:
      while True:
        new_arr.fromfile(f, 1)
    except EOFError:
      pass
  return [int(i) for i in new_arr]

maxx = 7368788
p = [i for i in primesqrtmod(maxx)]
save(p, "prime.bin")
p1 = extract("prime")
print(p1[-1])

print("done")