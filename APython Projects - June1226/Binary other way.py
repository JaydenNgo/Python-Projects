import time
def bin(n):
  a = [0 for i in range(n)]
  yield a
  while a != [1 for i in range(n)]:
    for i in range(n):
      if 0 not in a[i:]:
        a[i-1:] = [1] + [0 for i in range(n-i)]
        yield a
        break
    else:
      a[-1] = 1
      yield a

start = time.time()

for j in bin(15):
  print(j)
end = time.time()
print(end-start)