import random
import time

def rand(n):
  a = [i for i in range(n)]
  while True:
    random.shuffle(a)
    yield a

def diffs(n):
  repeat = 10**5
  distance = 0
  alist, blist = rand(n), rand(n)
  for i in range(repeat):  
    a,b = next(alist), next(blist)
    for j in range(n):
      distance += abs(a.index(j) - b.index(j))
  print(f"{n} {(distance/repeat):.4},  {(1/3)*((n**2)-1):.4}")
  
start = time.time()
for i in range(2,21):
  diffs(i)
end = time.time()
print('Time:', end-start)