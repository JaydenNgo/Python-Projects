import sys
import os
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

def list_to_bin(l):
    # 1. Group into chunks of 8
    # 2. Join the chunk into a string and parse as base-2
    # 3. Convert the list of integers into raw bytes
    return  bytes(
        int("".join(map(str, l[i : i + 8])), 2)
        for i in range(0, len(l), 8)
    )

def unpack(condensed,size=8):
  return [int(j) for i in condensed for j in f"{i:0{size}b}"]

def file_size(filename):
  f = os.path.getsize(filename)
  print(f"{filename} is {f:,} bytes")
  f /= 1_000
  if f > 1:
    print(f"{filename} is {f:.4} kilobytes")
    f /= 1_000
  if f > 1:
    print(f"{filename} is {f:.4} megabytes")

file_name = "prime.bin"
length = 2**27
print(length)
print()

try:
  with open(file_name, 'rb') as file:
    print("loading . . .")
    raw_byte = file.read()
  b = unpack(raw_byte)
  import_length = len(b)
  print(f"List loaded {import_length}")
  

# If DNE, create a list
except (FileNotFoundError):
  
  b = [1 for _ in range(length)]
  print("New List created")
  print("Clearing")
  primes = full_clears(b)
  print("Cleared")


# Change in size
# if import smaller than desired, grow it
if import_length < length:
  b += [1 for _ in range(length-import_length)]
  with open(file_name, "wb") as file:
    file.write(list_to_bin(b))
  print(f"List expanded {import_length:,} to {length:,}")

elif import_length > length:
  b = b[:length]
  print(f"List shrunk {import_length:,} to {length:,}")
  print(len(b))




#print(primes)

file_size(file_name)