alpha = ['A','B','C','D','E','F','G','A#','C#','D#','F#','G#']

while True:
  numstr = input('How many strings? ')
  if numstr.isdigit():
    numstr = int(numstr)
    break
  else:
    print('Not a number')
    continue

print('')
print('Input strings from Highest to Lowest')
print('If you have a repeated letter, use the letter twice, (A and AA, A# and AA#)')

def add_string():
  strings = {}
  while len(strings) < numstr:
    y = input('Add string ').upper()
    if y in strings:
      print('Already added')
      continue
    if y in alpha:
      pass
    elif y[-1:] in strings and y[-2] == y[-1]:
      pass
    elif y[-2:] in strings and y[-3] == y[-2]:
      pass
    else:
      print('Invalid string')
      continue
    strings[y] = []
  return strings

while True:
    strings = add_string()
    print('')
    for i in strings:
      print(i)
    print('')
    reset = input('Confirm (Y/N) ').upper()
    if reset == 'Y' or reset == 'YES':
      break
    else:
      continue

#print('')
#print(strings)
print('')
#-----------------------------------------------------------------
def true_note(strings):
  notes = []
  for i in strings:
    if i[-1] in alpha:
      notes.append(i[-1])
    elif i[-1] == '#':
      notes.append(i[-2:])
    else:
      print('ERROR')
  return notes

strings_note = true_note(strings)

#print(strings_note)
#------------------------------------------------------------------------------
print('')
def tab(strings):
  maxlen = len(max(strings))
  for k,v in strings.items():
    print(f'{k}{" "*(maxlen-len(k)+2)}{"".join(v)}')
print('Original Tab')
tab(strings)
print('')
#----------
piano = []
conv = {'A':0, 'A#':1, 'B':2, 'C':3, 'C#':4, 'D':5, 'D#':6, 'E':7, 'F':8, 'F#':9, 'G':10, 'G#':11, 'AA':12}
rconv = { v:k for k,v in conv.items()}
#------------------------------------------------------------------------
print('Type the string and fret w/ no space (G12) ')
print('If you want to do multiple of the same note do (G12x4)')
print('')
lstrings = [k for k in strings.keys()]
cur_string = 0

while True:
  print('Current string:', lstrings[cur_string])
  fret = input('Fret ').upper()
  if len(fret) == 0:
    break

  if fret == 'GAP':
    for i in strings:
      strings[i].append('-')
    tab(strings)
    continue

  if fret == 'UNDO':
    for v in strings.values():
      del v[-1]
      if v[-1].isdigit():
        for v in strings.values():
          del v[-1]
    tab(strings)
    continue
    
  if fret == 'UP' or fret == 'U':
    if cur_string <= 0:
      print("Can't go higher")
    else:
      cur_string -= 1
    continue

  if fret == 'DOWN' or fret == 'D':
    if cur_string >= numstr-1:
      print("Can't go lower")
    else:
      cur_string += 1
    continue

  fret = list(fret)
  multi = 1
  if 'X' in fret:
    find_x = fret.index('X')
    multi = fret[find_x+1:]
    if len(multi) <= 0:
      print('Invalid multiplier')
      continue
    multi = int("".join(multi))
    del fret[find_x:]
    
  fret = "".join(fret)
  if fret.isdigit():
    fret = int(fret)
  else:
    print('Not a number')
    continue

  if (0 <= fret <= 28) == False:
    print('Fret does not exist')
    continue
#-------------------------------------------------------------------------------  
  stringl = lstrings[cur_string]
  for j in range(multi):
    for i in strings:
      if i == stringl:
        notee = rconv[(conv[stringl] + fret)%12]
        piano.append(notee)
        piano.append(' ')
        strings[stringl].append(str(fret))
        strings[stringl].append('-')
      else:
        if fret > 9:
          strings[i].append('--')
        else:
          strings[i].append('-')
        strings[i].append('-')
  tab(strings)
#-------------------------------------------------------------------------------
print()
print(piano)
print(''.join(piano))


  
