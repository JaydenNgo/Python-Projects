import random
gene = {1:'A', 2:'T', 3:'C', 4:'G'}

numstr = 15
lenstr = 75
lensub = 3
strings = {j: ''.join([gene[random.randint(1,4)] for i in range(lenstr)]) for j in range(1,numstr+1)}
stat= []

for k,v in strings.items():
  print(k,v)
print('')
#------------------------------------------------------------------------------

def inall(nest, clip): #[ [],[],[] ]
  for i in nest:
    if clip not in i:
      return False
  return True

#(1,2,3)
def search(tuples):
  group = [strings[i] for i in tuples]
  
  if len(strings) < 2:
    print('Error')
    return
  
  diff = 0
  string1 = strings[tuples[0]]
  index = []
  
  for j in range(1, lenstr):
    for i in range(lenstr+1-j):
      clip = string1[i:i+j]

      if inall(group, clip) == True and len(clip) >= lensub:
        indexes = []
        for k,v in strings.items():
          if k in tuples:
            ind = v.index(clip)
            indexes.append(ind)
            diff += abs(i-ind)
        
        index.append((clip,indexes))
      
  print(f'{" "*10} Strings {tuples}')

  for clip, lists in index:
    print(clip, end= ' ')
    for i in lists:
      print(i, end =' ')
    print('')
    
  lenind = len(index)
  if lenind == 0:
    avgg = 'None'
  else:
    avgg = round((diff/lenind),3)
  stat.append((tuples)+(lenind,avgg))
  print('')
  print('Total', lenind)
  print('Average', avgg)
  print('')

#Compare 1 string to the rest
def compare_all(a):
  for i in strings:
    if i == a:
      continue
    else:
      search((a,i))

#compare_all(2)

#All combinations of pairs
def compare_everything(strings):
  for i in strings:
    for j in range(i+1,len(strings)+1):
      search((i,j))
  return

#compare_everything(strings)

search(tuple(i for i in range(1,numstr+1)))


'''
def lennum(a):
  return len(str(a))
  
print('------- Matches ----- Avg')
for a,b,leng,diff in stat:
  print(f'{a}-{b}:{" "*(3-(lennum(a)+lennum(b)))}   {leng} {" "*(11-lennum(leng))} {diff}')
'''
  


