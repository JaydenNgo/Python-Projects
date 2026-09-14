import math
import json

rt = math.sqrt(2)

def ln(x):
  return math.log(x)

def sqrt(x):
  return math.sqrt(x)

def est(x,factor):
  # if not x or not factor: return 0
  return ln(factor*x)*x

def prime():
  primes = []
  num = 2
  while True:
    for prime in primes:
      # Not prime
      if num//prime == num/prime:
        num += 1
        break
    else:
      primes.append(num)
      yield num
      num += 1

def primesqrtmod(n, seed = [2]):
  primes = seed
  num = seed[-1]
  length = (len(seed))
  while length < n:
    num += 1
    #Remove int for visual
    maxsearch = sqrt(num)
    for prime in primes:
      # Passed the sqrt mark
      if prime > maxsearch:
        primes.append(num)
        #num += 1
        length += 1
        break
      # Not prime
      if not (num % prime):
        #num += 1
        break

  return primes

# Produce a list of the first n primes
# Can take preexisting list and adds to it
def primelist(n, seed = []):
  primes = seed
  length = len(seed)
  if length:
    num = seed[-1]
  else:
    num = 2
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


file_name = "Primes.json"
maxx = 500000
#173
#p1 = primelist(maxx)
#p2 = primesqrtmod(maxx)

#print(p1,p2)

# If list exists, import it
try:
    with open(file_name, 'r') as file:
        primes = json.load(file)
    print(f"List loaded")

# If DNE, create a list
except (FileNotFoundError, json.JSONDecodeError):
    #primes = primelist(maxx)
    primes = primesqrtmod(maxx)
    print("New List created")

# Change in size
length = len(primes)
if maxx < length:
  primes = primes[:maxx]
  print(f"List shrunk {length} to {maxx}")

else:
  #primes = primelist(maxx,primes)
  primes = primesqrtmod(maxx,primes)
  print(f"List expanded {length} to {maxx}")
  with open(file_name, "w") as file:
    json.dump(primes, file)

print(primes[-1])
def prime_MSE(maxx, scalar):
  total_diff = 0
  for index, val in enumerate(primes):
    ind = index+1
    if ind > maxx:
      break
    
    estimate = est(ind, scalar)
    #print(f"{val}, {estimate}, {ind}")
    diff = (val-estimate)**2
    total_diff += diff
  
  MSE = total_diff/maxx
  print(f"MSE Difference:  {MSE:.3f}, {scalar:.7f}")
  return MSE

# Kind of like gradient descent
# Keep going until you start incresing (prev -> min -> next)
# Loop ends at next, so just back to prev and check at the next degree of precision
'''
start = 3
for degree in range(1,7):
  print(degree, "of precision")
  prev = prime_MSE(maxx,start)
  i = 0
  while True:
    factor = start + 10**(-degree)*i
    curr = prime_MSE(maxx,factor)
    if curr > prev:
      break
    prev = curr
    i += 1
  start = factor-(2*10**(-degree))

print(est(10000,2+rt))
'''
#MSES = [prime_MSE(3000,0.3414 + 0.00001*i) for i in range(10)]

#print(min(MSES))