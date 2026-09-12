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
  

def find(max,consec):
  count = 0
  for j in bin(max):
    for ind,num in enumerate(j):
      if j[ind:ind+consec] == [num for i in range(consec)]:
        print(num, j)
        count += 1
        break
    else:
      print(' ', j)
  return count
  


        
print(find(7,5))
