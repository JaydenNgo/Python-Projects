import random
import math

prob = [0.3, 0.3, 0.4]

  
def grouped(prob_list):
  div = {i+1: sum(prob_list[:i+1]) for i in range(len(prob_list))}
  print(div)
  return div

def transition(group):
  a = random.random()
  #print(a)
  for k,v in group.items():
    if v > a:
      return k

print(transition(grouped(prob)))