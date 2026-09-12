def happy(n):
  m = n
  while True:
    squares = 0
    while n > 0:
      r = n%10
      squares += r**2
      n //= 10
    n = squares
    if n == 1:
      print(m, "is happy")
      return True
    elif n == 4:
      print(m, 'is sad')
      return False

happy_family = []
for i in range(1,100):
  if happy(i):
    happy_family.append(i)

print(happy_family)