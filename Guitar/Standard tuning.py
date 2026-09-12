#E Standard = EADGBE
conv = {'A':0, 'A#':1, 'B':2, 'C':3, 'C#':4, 'D':5, 
'D#':6, 'E':7, 'F':8, 'F#':9, 'G':10, 'G#':11}
rconv = {v:k for k,v in conv.items()}


def shift(note, num):
  return rconv[(conv[note]+num)%12]


def standards(num):
  standard = ['B','E', 'A', 'D', 'G', 'B', 'E']
  if num == 4:   return standard[1:5]
  elif num == 5: return standard[:5]
  elif num == 6: return standard[1:7]
  elif num == 7: return standard

def tuning(root,version,numstr):
  standard = standards(numstr)

  diff = conv[root]-conv[standard[0]]
  if version == 'standard':
    d = [shift(i,diff) for i in standard]
    
  elif version == 'drop':
    d = [shift(i,diff+2) for i in standard]
    d[0] = root
  #print(d)
  return d

og = tuning('E','standard',7)
new = tuning('G','drop',7)
print(og)
print(new)
sizediff = len(new)-len(og)
print(sizediff)
for i in range(sizediff+1):
  print(new[i:i+len(og)])
