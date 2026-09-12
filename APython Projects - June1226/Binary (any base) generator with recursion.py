import time

def bin(len, base):
  if len == 0:
    return None
  elif len == 1:
    for i in range(base):
      yield [i]
  else:
    for j in range(base):
      for i in bin(len-1, base):
        yield [j] + i
  
start = time.time()

for j in bin(8,7):
  print(j)
end = time.time()

print(end-start)