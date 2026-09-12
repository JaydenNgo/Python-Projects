def dyfib(num,length):
  base = [1 for i in range(num)]
  inc = [i for i in range(1,num+1)]
  
  for i in range(length-num):
    new = sum(base[-i] for i in inc)
    base.append(new)
    #print(base)
  return base

for i in range(1,5):
  print(dyfib(i+1,10))