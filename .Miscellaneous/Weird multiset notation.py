sets = []
while True:
  a = str(input('Enter set'))
  sets.append(a)
  if len(a) == 0:
    break
  
string = str(input('String'))

point = 0
a = []
for i in string:
  if i != sets[point]:
    a.append('|')
    point += 1
  a.append('*')
print(a)