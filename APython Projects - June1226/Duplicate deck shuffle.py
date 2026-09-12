import random
import time
def random_shuffle(n):
  ogdeck = [i for i in range(n)]
  deck = [i for i in range(n)]
  random.shuffle(deck)
  c = 0
  while ogdeck != deck:
    random.shuffle(deck)
    c += 1
  return c  

def avg_shuffle(leng,rep):
  sum = 0
  for i in range(rep):
    sum += random_shuffle(leng)
  print(leng, (sum/rep))
  
  return sum/rep

for i in range(1,15):
  start = time.time()
  count = random_shuffle(i)
  end = time.time()
  print(f"Length: {i} took {count} shuffles {end-start} seconds")