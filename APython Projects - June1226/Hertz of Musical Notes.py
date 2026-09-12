octaves = [i for i in range(-5,5+1)]
note = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
semi = {n:(1/12)*i for i,n in enumerate(note)}

def oct(x):
  return (27.5)*(2**x)

def compare(n,l,r):
  leftdiff = n-l
  rightdiff = r-n

  if leftdiff < rightdiff:
    #print(l)
    return l
  else:
    #print(r)
    return r
  
hertz = {}
for i in octaves:
  for j in note:
    notestr = j+str(i)
    freq = oct(i+semi[j])
    print(f"{notestr}\t {freq:.2f} HZ")
    hertz[notestr] = freq

hertzflip = {v:k for k,v in hertz.items()}
hertz_note = list(hertz)

def find_note(hert):
  for index, note in enumerate(hertz_note):
    if hertz[note] >= hert:
      prev = hertz_note[index-1]
      closest = hertzflip[compare(hert,hertz[prev],hertz[note])]
      #print(closest)
      return closest

print()
for i in range(1,9):
  h = 100*i
  print(f"{h} ~ {find_note(h)}")
