def fib():
  x = 0
  y = 1
  while True:
    yield x
    x,y = y,x+y

for i in fib():
  if i >= 10**27:
    break
  print(i)