
import random
gene = {1:'A', 2:'T', 3:'C', 4:'G'}

numstr = 2
lenstr = 30
strings = {j+1: ''.join([gene[random.randint(1,4)] for i in range(lenstr)]) for j in range(numstr)}

def rotate(string,times=1):
  times = times%len(string)
  return string[times:] + string[:times]

def comp(base,side):
  for i in range(lenstr):
    rot = rotate(side,i)
    matches = 0
    pos = []
    for j in range(lenstr):
      if base[j] == rot[j]:
        matches += 1
        pos.append(j)
    print(matches,pos)
    print(base)
    print(rot)
    print()
    

for k,v in strings.items():
  print(k,v)
print()

#print(rotate(string,8))
comp(strings[1],strings[2])