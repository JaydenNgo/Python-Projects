import random

def rlist(n):
  a = [random.randint(1,10) for i in range(n)]
  #print(a)
  return a

def sums(a):
  if len(a) == 1:
    return a[0]
  else:
    a = [a[i-1]+a[i] for i in range(len(a))]
    a = a[1:]
    #print(a)
    return sums(a)

count = {}
n = 2
for i in range(100000):
  num = sums(rlist(n))
  if num not in count:
    count[num] = 1
  else:
    count[num] += 1

for i in range(n,max(count)+1):
  if i not in count:
    print(i, 0)
  else:
    print(i, count[i])