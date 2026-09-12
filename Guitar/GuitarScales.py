conv = {'A':0, 'A#':1, 'B':2, 'C':3, 'C#':4, 'D':5, 'D#':6, 'E':7, 'F':8, 'F#':9, 'G':10, 'G#':11}
rconv = {v:k for k,v in conv.items()}

def shift(note, num):
  return rconv[(conv[note]+num)%12]


major = [0,2,4,5,7,9,11,12]
minor = [0, 2, 3, 5, 7, 8, 10, 12]
harm_minor = [0, 2, 3, 5, 7, 8, 11, 12]
melo_minor = [0, 2, 3, 5, 7, 9, 11, 12]

def scale_translate(pattern):
  #Translates ["W","W","H","W","W","W","H"]
  a = [0]
  for i in pattern:
    if i == "W":
      a.append(a[-1]+2)
    elif i == "H":
      a.append(a[-1]+1)
    else:
      a.append(a[-1]+3)
  return a

def root_scale(root,scale):
  notes = [shift(root,i) for i in scale]
  return notes

def printlist(lists):
  for i in lists:
    print(i, end=' ')
  print()
  

root = "C"

cM = root_scale(root, major)
cm = root_scale(root, minor)
hm = root_scale(root, harm_minor)
mm = root_scale(root, melo_minor)

print(f"{root} Major scale: ", end ='')
printlist(cM)

print(f"{root} Minor scale: ", end ='')
printlist(cm)

print(f"{root} Harmonic minor: ", end ='')
printlist(hm)

print(f"{root} Melodic minor: ", end ='')
printlist(mm)
print()
  

def triad(scale):
  a = [scale[2*i] for i in range(3)]
  return a

def diad(scale):
  a = [scale[4*i] for i in range(2)]
  return a

#printlist(triad(cM))
#printlist(triad(cm))
#print()

standard = ['E', 'A', 'D', 'G', 'B', 'E']

def print_chord(chord):
  printlist(standard)
  board = [['-' for i in range(6)] for j in range(12)]
  for index,i in enumerate(chord):
    if i == "X":
      board[0][index] = i
    else:
      board[i][index] = i
  for i in board:
    printlist(i)

  return board

#FIX G MAJOR OPEN CHORD
def open_chord(root,scale):
  full_scale = root_scale(root, scale)
  chord = []
  rooted = False
  for i in standard:
    for j in range(4):
      note = shift(i,j)
      if rooted == False:
        if note == root:
          rooted = True
          
      if rooted == True:
        if note in triad(full_scale):
          chord.append(j)
          break
    else:
      chord.append('X')
  return chord

#Open root power chord vs freted root power chord
def power_chord(root):
  full_scale = root_scale(root,major)
  chord = []
  rooted = False
  size = 0
  for i in standard:
    for j in range(8):
      note = shift(i,j)
      if (rooted == False) and (note == root) and j <= 5:
          rooted = True
          pos = j
          chord.append(j)
          break
        
      if (rooted == True) and (j == pos+2) and (note in diad(full_scale)):
          chord.append(j)
          break
    else:
      chord.append('X')
  return chord



root = "A"

print(triad(root_scale(root,major)))
print(diad(root_scale(root,major)))
for i in standard:
  chord = power_chord(i)
  print(i,chord)

  

power_chord(root)
def barre_chord(newroot,root,scale):
  if root not in ("A","E"):
    print("DNE")
    return
  og = open_chord(root,scale)
  if newroot == root:
    return og
  print(og)
  diff = conv[newroot]-conv[root]
  if diff < 0:
    diff += 12
  print(diff)
  newchord = [i+diff if isinstance(i,int) else i for i in og]
  print(newchord)
  return newchord
  
'''
z = open_chord(root,major)
print()
print_chord(z)
'''




  