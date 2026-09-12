import random
import time
start = time.time()
def f(r,t):
  b = 0
  for i in range(t):
    a = random.randint(-r,r)
    b += a
  return b

counts = {} 
ranges = [f(5,3) for i in range(1000000)]
for i in ranges:
  if i not in counts:
    counts[i] = 1
  elif i in counts:
    counts[i] += 1

sorts = sorted([i for i in counts.keys()])
new_counts = {k:counts[k] for k in sorts }
for k,v in new_counts.items():
  print(k,v)
end = time.time()
print(end-start)