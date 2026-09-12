import random
sum = 0
rep = 100
for i in range(rep):
  h = 100000
  m = h//2
  l = 0
  num = random.randint(1,h)
  
  c = 0

  while m != num:
    if m < num:
      l = m
      m = (l+h)//2
     
    if m > num:
      h = m
      m = (l+h)//2
      
    c += 1
  sum += c
print('avg', sum/rep)

