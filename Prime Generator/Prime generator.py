import math

rt = math.sqrt(2)
def ln(x):
  return math.log(x)

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
    
def isprime(n):
  for i in prime():
    if i == n:
      return True
    elif i > n:
      return False

def primelist(n):
  primes = []
  length = 1
  for val in prime():
    if length > n:
      break
    primes.append(val)
    length += 1
  return primes

def est(x,factor):
  if not x or not factor: return 0
  return ln(factor*x)*x

max = 10000
primes = primelist(max)

#616398.3443232562 3
# x = val
# y = ind
# est(x): # of primes up to x
def prime_MAE(max, scalar):
  total_diff = 0
  for i in primes:
    index, val = i
    ind = index+1
    if index >= max:
      break
    estimate = est(index, scalar)
    ind = index+1
    print(f"{val}, {estimate}, {ind}")
    diff = abs(ind-estimate)
    #print(diff)
    total_diff += diff
  MAE  = total_diff/max
  print("MAE Difference: ", MAE, scalar)
  return MAE

def prime_MSE(max, scalar):
  total_diff = 0
  for index, val in enumerate(primes):
    ind = index+1
    if ind > max:
      break
    estimate = est(ind, scalar)
    #print(f"{val}, {estimate}, {ind}")
    diff = (val-estimate)**2
    #print(diff)
    total_diff += diff
  
  MSE = total_diff/max
  print("MSE Difference: ", MSE, scalar)
  return MSE

degree = 3
start = 3

prev = prime_MSE(max,start)
'''
for i in range(10**degree):
  factor = start + 10**(-degree)*i
  curr = prime_MSE(max,factor)
  if curr > prev:
    break
  prev = curr

'''

#MSES = [prime_MSE(3000,0.3414 + 0.00001*i) for i in range(10)]

#print(min(MSES))