history = {}

def hail(n):
  a = []
  b = []
  c = 0
  while n > 1:
    if n % 2 == 0:
      n = n/2
    else:
      n = (3*n)+1
    c+=1
    a.append((n,c))
  #print(a)
  for k,v in a:
    b.append((int(k),c-v))
    history[int(k)] = c-v
  return b
  

print(hail(5))
print(history)
print(hail(6))
