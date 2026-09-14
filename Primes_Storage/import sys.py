import sys
import json
import os
import pickle

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

def count(dict, n):
  if n not in dict:
    dict[n] = 1
  else:
    dict[n] += 1

def file_size(filename):
  f = os.path.getsize(filename)
  print(f"{filename} is {f:,} bytes")

#True/1 = Prime
#False/0 = Composite
length = 2**26
file_name = "funnyprime.json"
size = 2**5

comp = length%size
if comp:
  print(f"Size issue {comp}")
  length -= comp

# If list exists, import it
try:
  with open(file_name, 'r') as file:
    print("loading . . .")
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
  condense = condense_bin(b,size)
  with open(file_name, "w") as file:
    json.dump([length,size,condense], file)
  print(f"List expanded {import_length:,} to {length:,}")

elif import_length > length:
  b = b[:length]
  print(f"List shrunk {import_length:,} to {length:,}")
  print(len(b))

print()
print("Clearing")
primes = full_clears(b)
print("DONE")

binary_size = sys.getsizeof(b)
print(f"Binary is {binary_size:,} bytes large")

condense = condense_bin(b,size)
print(len(condense))
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
print(f"{int(binary_size / condensed_size)} times smaller")


print(f"Length: {len(condense)}")
print(f"Size: {size} bits")
print()
with open(file_name, 'w') as file:
  json.dump([length, size, condense], file)
file_size(file_name)

with open("data.pkl", "wb") as file:
  pickle.dump(condense, file)
file_size("data.pkl")

bin_count = {}
raw_bytes = bytes(
    int("".join(map(str, b[i : i + 8])), 2)
    for i in range(0, len(b), 8)
)

#print(raw_bytes)  # Output: b'A' (represents characters 'A' and 'B')
with open("prime.bin", "wb") as file:
    file.write(raw_bytes)
print("Done")