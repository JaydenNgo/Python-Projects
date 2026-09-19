import random
import time
def square(n):
  a = [i for i in range(n**2)]
  random.shuffle(a)
  b = [a[i:i+n] for i in range(0,n**2,n)] 
  
  #for i in b:
    #print(i)
  #print('')
  return b

#Find num in list
def find(num, lists):
  for ind,list in enumerate(lists):
    if num in list:
      #print((ind,list.index(num)))
      return ((ind,list.index(num)))

def distance(tuple1,tuple2):
  dist0 = abs(tuple1[0]-tuple2[0])
  dist1 = abs(tuple1[1]-tuple2[1])
  return (dist0**2+dist1**2)**(1/2)

def diffs(n):
  repeat = 10**4
  d = 0
  for j in range(repeat):
    a = square(n)
    b = square(n)
    c = 0
    for i in range(n**2):
        dist = distance(find(i,a),find(i,b))
        #print(dist)
        c += dist
    d += (c/n**2)
  print('')  
  print(f'Stats for', n)  
  print(d/repeat)
  print('')

start = time.time()
for i in range(2,11):
  diffs(i)
end = time.time()
print('Time:', end-start)