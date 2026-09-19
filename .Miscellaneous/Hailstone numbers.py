import time

def hail(n):
  c = 0
  while n > 1:
    if not n%2:
      n = n/2
    else:
      n = 3*n+1
    c +=1
  return c

print("Started")
start = time.time()
for i in range(1000000):
  #print(i, hail(i))
  hail(i)
end = time.time()
print(end-start)

print('While loop')