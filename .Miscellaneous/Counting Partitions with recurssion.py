checked = []
def count(amount,max):
  if amount < 0:
    return 0
  elif (amount == 0) or (max == 1):
    return 1
  else:
    return count(amount-max,max) + count(amount,max-1)
#Maybe implement a checked version to reduce computation time
for i in range(50):
  print(i, ',', count(i,i))