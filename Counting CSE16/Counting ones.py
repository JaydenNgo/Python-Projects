def bin(n):
  if n == 0:
    return none
  elif n == 1:
    yield [0]
    yield [1]
  else:
    for i in bin(n-1):
      yield i + [0]
      yield i + [1]

countss = 0  
count = 0
for j in bin(10):
  for k in j:
    if k == 1:
      count += 1
  if count >= 3:
    countss += 1
  count = 0
print(countss)