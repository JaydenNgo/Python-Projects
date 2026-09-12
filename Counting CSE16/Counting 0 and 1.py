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

count = 0
for i in bin(9):
  zero = 0
  one = 0
  for j in i:
    if j == 0:
      zero += 1
    if j == 1:
      one += 1
  
  if (zero, one) == (5,4):
    print(zero,one,i)
    count += 1
  else:
    print('   ',i)
  zero = 0
  one = 0

print(count)