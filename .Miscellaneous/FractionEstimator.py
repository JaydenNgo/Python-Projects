import math

pi = math.pi
e = math.e

# fract: largest denominator
# precision: digits of accuracy
def fract(target, fract, precision):
  target %= 1
  for i in range(1,fract):
    for j in range(1,i):
      diff = j/i-target
      if abs(diff) < 10**(-precision):
        #print(diff, j, i)
        print(f"{diff}, {j}/{i}")
      if diff-target > 0:
        break

#fract(pi, 500, 6)

fract(27.35, 100, 4)

