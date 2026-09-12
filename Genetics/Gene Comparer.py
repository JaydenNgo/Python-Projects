import random
gene = {1:'A', 2:'T', 3:'C', 4:'G'}

numstr = 10
lenstr = 50
lensub = 4
strings = {j+1: ''.join([gene[random.randint(1,4)] for i in range(lenstr)]) for j in range(numstr)}
stat= []

for k,v in strings.items():
  print(k,v)
print()

def search(a, b):
  if a == b:
    print(f'{" "*10} String {a} --- String {b} Same String')
    print()
    return 
  diff = 0
  string1 = strings[a]
  string2 = strings[b]
  match = []
  for j in range(1,lenstr):         #Iterate through every size
    for i in range(lenstr+1-j):     #Iterate through substring of size
      clip = string1[i:i+j]         #
      if clip in string2 and len(clip) >= lensub:
        ind = string2.index(clip)
        match.append((clip,i,ind))
        diff += abs(i-ind)
      #print(a, clip)
      
  print(f'{" "*10} String {a} --- String {b}')
  for word,i,j in match:
    print(word,i,j)
  num_matches = len(match)

  if num_matches == 0:
    avgg = 'None'
  else:
    avgg = round((diff/num_matches),3)
  stat.append((a,b,num_matches,avgg))

  print()
  print('Total', num_matches)
  print('Average', avgg)
  print()

# Compare 1 string to the rest individually
def compare_all(a):
  for i in strings:
    search(a,i)

#compare_all(1)

# Compare each unique combination
def compare_everything(strings):
  for i in strings:
    for j in range(i,len(strings)):
      search(i,j+1)
  return

compare_everything(strings)

def lennum(a):
  return len(str(a))
  
print('------- Matches ---- Avg')

for a,b,leng,diff in stat:
  print(f'{a}-{b}:{" "*(3-(lennum(a)+lennum(b)))}   {leng} {" "*(11-lennum(leng))} {diff}')
#numstr choose 2 outputs
  


