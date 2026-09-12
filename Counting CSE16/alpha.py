
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
  
count = 0
for j in bin(8,7):
  print(j)
  for ind,num in enumerate(j):
    if j[ind:ind+2] == [3,4]:
      count += 1

print(count)