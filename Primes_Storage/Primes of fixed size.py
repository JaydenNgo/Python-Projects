import sys
import json
import time

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
      for j in range(2*i,len(l),i):
        l[j] = 0
  return primes

# Takes in binary list "l" (primes) 
# and converts groups of length "size" into integers
# returns list of integers
def condense_bin(l,size):
  if length%size:
    print(f"Size issue {length%size}")
    return
  return [int("".join([str(i) for i in l[i:i+size]]),2) for i in range(0,len(b),size)]
  condense = []
  for i in range(0,len(b),size):
    group = l[i:i+size]
    n = "".join([str(i) for i in l[i:i+size]])
    condense.append(int(n,2))
  return condense

# Inverse of condense
# Takes in list of integers and converts into binary length "size"
def unpack(condensed,size):
  return [int(j) for i in condensed for j in f"{i:0{size}b}"]
  new_01 = []
  for i in condensed:
    convert = f"{i:0{size}b}"
    new_01 += [int(j) for j in convert]
  return new_01

#True/1 = Prime
#False/0 = Composite
length = 9_999_872 
file_name = "newprime.json"
size = 2**8
print(f"Size: {size} bits")

comp = length%size
if comp:
  print(f"Size issue {comp}")
  length -= comp
  #sys.exit(0)

# If list exists, import it
try:
  with open(file_name, 'r') as file:
    import_length, import_size, condensed = json.load(file)
  b = unpack(condensed, import_size)
  print(f"List loaded")

# If DNE, create a list
except (FileNotFoundError, json.JSONDecodeError):
  b = [1 for _ in range(length)]
  import_length = length
  print("New List created")


# Change in size
# if import smaller than desired, grow it
if import_length < length:
  b += [1 for _ in range(length-import_length)]
  with open(file_name, "w") as file:
    json.dump([length,size,b], file)
  print(f"List expanded {import_length:,} to {length:,}")

elif import_length > length:
  b = b[:import_length]
  print(f"List shrunk {import_length:,} to {length:,}")
  
  
print()
primes = full_clears(b)

binary_size = sys.getsizeof(b)
print(f"Binary is {binary_size:,} bytes large")

condense = condense_bin(b,size)
condensed_size = sys.getsizeof(condense)
print(f"Condensed is {condensed_size:,} bytes large")

prime_size = sys.getsizeof(primes)
print(f"Primes is {prime_size:,} bytes large")
#------------------------------------------------------------------

new_01 = unpack(condense,size)
print()
print(f"Sanity Check: {new_01 == b}")

print()
print(f"For prime numbers up to {length:,} ")
print(f"Bytes: {binary_size:,},  {condensed_size:,}")
print(f"{(binary_size / condensed_size):.4} times smaller")
print("Done")