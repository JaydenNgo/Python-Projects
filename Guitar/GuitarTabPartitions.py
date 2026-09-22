import copy
#TO DO
#Add restart
#Add title to display and file
#Check out to the Hellfire chorus
#Check why DT Winter isnt showing more subtunings
#Add sub sections
#Add chords

#Arrow so you know which line?


conv = {'A':0, 'A#':1, 'B':2, 'C':3, 'C#':4, 'D':5, 'D#':6, 'E':7, 'F':8, 'F#':9, 'G':10, 'G#':11}
rconv = {v:k for k,v in conv.items()}

# Returns a note shifted up n semitones
def shift(note, n):
    return rconv[(conv[note]+n)%12]

# returns standard tuning for n strings (4-7)
def standards(n):
    standard = ['B','E', 'A', 'D', 'G', 'B', 'E']
    if   n == 4: return standard[1:5]
    elif n == 5: return standard[:5]
    elif n == 6: return standard[1:7]
    elif n == 7: return standard

# Returns drop or standard tuning depending on root note and # of strings
def tuning(root,version,numstr):
    standard = standards(numstr)
    diff = conv[root]-conv[standard[0]]
    if version == 'standard':
        d = [shift(i,diff) for i in standard]

    elif version == 'drop':
        d = [shift(i,diff+2) for i in standard]
        d[0] = root
        
    return d

# Allows user to input tuning for tab
# Returns dictionary: 
# Key = each note
# Value = empty list
def add_strings():
    strings = {}
    while True:
        y = input('Add string: ').upper()
        if 'DROP' in y or 'STANDARD' in y:
            spaces = [index for index,item in enumerate(y) if item == ' ']
            if len(spaces) != 2:
                print("Invalid Tuning \n")
                continue 

            #Drop tuning
            if 'DROP' in y:
                if len(y) < 8:
                    print("Missing value (Drop G 7)")
                    continue
                mode = 'drop'
                note = y[spaces[0]+1:spaces[1]]
                numstr = y[spaces[1]+1:]

            #Standard Tuning
            if 'STANDARD' in y:
                if len(y) < 12:
                    print("Missing value (E Standard 6)")
                    continue
                loc_note = y.index('STANDARD')
                mode = 'standard'
                note = y[:loc_note-1]
                numstr = y[loc_note+9:]
            
            #Error Checking
            if int(numstr) > 7:
                print("Too many strings\n")
                continue
            if note not in conv:
                print("Invalid tuning")
                continue
            if numstr.isdigit() == False:
                print("Missing number of strings")
                continue
            else:
                numstr = int(numstr)
                for i in tuning(note,mode,numstr)[::-1]:
                    if i in strings:
                        strings[i[0]+i] = []        #If open string note shows up multiple times
                    else:
                        strings[i] = []
                break

        #Manually add Tuning
        if len(y) == 0:
            break
        if y in strings:
            print('Already added')
            continue
        if y in conv:
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


print()
print('Input strings from Highest to Lowest')
print('If you have a repeated letter, use the letter twice, (A and AA, A# and AA#)')
print('You can also type presets like "Drop G 7" or "E Standard 6"')
print()

def get_new_tuning():
    pass

#Take user input Tuning and confirmation
def get_tuning(new = False):
    if new:
        get_new_tuning()
    while True:
        strings = add_strings()
        print()
        for i in strings:
            print(i)
        print()
        reset = input('Confirm (Y/N): ').upper()
        if reset in ("Y","YES"):
            return strings
        else:
            continue

strings = get_tuning()
#print()
#print(strings)
print()
#-----------------------------------------------------------------
#Get notes for calculation
def true_note(strings):
    notes = []
    for i in strings:
        if i[-1] in conv:
            notes.append(i[-1])
        elif i[-1] == '#':
            notes.append(i[-2:])
        else:
            print('ERROR')
    return notes

strings_note = true_note(strings)
#print(strings_note)
print()
#------------------------------------------------------------------------------
# Print out tab
def print_tab(strings):
    for k,v in strings.items():
        print(f'{k:4}{"".join(v)}')
    print("\n")

print('Original Tuning')
print_tab(strings)
#-------------------------------------------------------------------------------

#Clear file
def tab_create():
    file_name = input("Give this tab a name \n")
    target_file = f"{file_name}.txt"
    with open(target_file, "w") as file:
            file.write(file_name)
            file.write(" Tabs \n\n")
            print()
    return target_file

def tab_write(strings,file_name):
    #Create a copy
    cstrings = {k:[i for i in v] for k,v in strings.items()}
    for i in cstrings:
        maxlen = len(cstrings[i])
        break

    #Remove all buffers
    for i in range(maxlen-1,-1,-1):
        line = [v[i] for v in cstrings.values()]
        if line == ['-' for i in range(len(cstrings))]:
            for v in cstrings.values():
                del v[i]

    #Write tab so you can copy to Google Sheets =D
    maxlen = len(max(strings))
    with open(file_name, "a") as file:
        for k,v in cstrings.items():
            file.write(f'{k}{" "*(maxlen-len(k))} \t')
            for i in v:
                if i.isdigit() or i == '#': 
                    file.write(i)
                file.write("\t")
            file.write("\n")
        file.write("\n")

target_file = tab_create()
tab_write(strings,target_file)
#------------------------------------------------------------------------
print('You start on the highest string')
print('You can use "u"/"up" and "d"/"down" to traverse the strings')
print('Then type the fret on the given string')
print('If you want to do multiple of the same note do (12x4)')
print('"Gap" if you want to make spaces between notes (gapx3)')
print('"Undo" to remove the latest note (undox3)')
print('"Break" to create segments in the tabs')
print('"Done" to stop the program and translate the tabs')
#Create a done options instead of basic enter??
print('Not case sensitve =D')
print()

list_of_strings = [i for i in strings]
num_strings = len(list_of_strings)
stringptr = 0

while True:
    print('Current string:', list_of_strings[stringptr])
    fret = input('Fret ').upper()
    print()
    if fret == "DONE":
        break
        
    if fret in ("U","UP"):
        if stringptr <= 0:
            print("Can't go higher")
        else:
            stringptr -= 1
        continue

    if fret in ("D","DOWN"):
        if stringptr >= num_strings-1:
            print("Can't go lower")
        else:
            stringptr += 1
        continue
    
    if fret in ("SPLIT","BREAK"):
        #Add minimum split size
        for v in strings.values():
            if len(v) == 0:
                print("No values")
                break
            v += ["-","#","-"]

        print()
        print_tab(strings)
        continue

    #Retrieve Multiplier
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

    # Allow gapx3 and undox3
    if fret in ("GAP","UNDO"):
        pass
    #Error Catching
    elif fret.isdigit():
        fret = int(fret)
        if not (0 <= fret <= 30):
            print('Fret does not exist')
            continue
    else:
        print('Not a number')
        continue
    
#-------------------------------------------------------------------------------
    # Use the multiplier
    stringl = list_of_strings[stringptr]
    for j in range(multi):                            
        if fret == 'GAP':
            for i in strings:
                strings[i].append('-')

        elif fret == 'UNDO':
            rep = 1
            for v in strings.values():
                if len(v) <= 0:
                    print("No more tab left \n")
                    rep = 0                                     #Flag error
                    break
            if rep <= 0: break
            
            # If last entry is number and buffer, delete 2
            for v in strings.values():
                if v[-2].isdigit(): 
                    rep = 2; break
                
            for i in range(rep):
                for v in strings.values():
                    if len(v) <= 0: break
                    else: del v[-1] 
            
        
        #Add to tab
        else:
            for i in strings:
                if i == stringl:
                    strings[stringl].append(str(fret))
                    strings[stringl].append('-')
                else:
                    if fret > 9:
                        strings[i].append('--')
                    else:
                        strings[i].append('-')
                    strings[i].append('-')
    print_tab(strings)
    print()
#-------------------------------------------------------------------------------
print()
print('Original Tab')
print_tab(strings)
print()

def string_empty(n):
    for i in n:
        if i not in ('-','--','#'):
            return False
    return True

#Note: Maybe only cut top and bottom, nothing in the middle?

#Remove strings that aren't used
def cut_tab(a):
    to_cut = [k for k,v in a.items() if string_empty(v)]
    
    if len(to_cut) > 0:
        for i in to_cut:
            del a[i]
        return True
    return False
    

if cut_tab(strings):
    print()
    print("Cut strings")
    print_tab(strings)
    tab_write(strings,target_file)


#--------------------------------------------------------------------------------
print()
print('Please add the New tuning')
print()
while True:
    newtuning = add_strings()
    print()
    if len(newtuning) < len(strings):
        print('Not enough strings')
        continue
    for i in newtuning:
        print(i)
    print()
    reset = input('Confirm (Y/N) ').upper()
    if reset in ("Y","YES"):
        break
    else:
        continue

for i in range(5):
    print() 
print("TRANSLATION")
print()

#For each subtuning
print_tab(strings)
sizediff = len(newtuning)-len(strings)
lnewtune = list(newtuning)
for i in range(sizediff+1):
    sub_tuning = lnewtune[i:i+len(strings)]
    print(sub_tuning)

    newtune = {j:[] for j in sub_tuning}
    newtune_note = true_note(newtune)

    
    for i,j in zip(strings,newtune):
        newtune[j] = [k for k in strings[i]]
    

    #print("New"); tab(newtune)
    #print("OG"); tab(strings)
#--------------------------------------------------------------------
    #Find the difference between each string
    difflist = []
    for i,j in zip(strings_note,newtune_note):
        diff = conv[i]-conv[j]
        if diff < 0:
            diff += 12
        difflist.append(diff)

#----------------------------------------------------------------
    all_frets = set()
    for newstring, diffs in zip(newtune,difflist):
        frets = newtune[newstring]
        for index,note in enumerate(frets):
            if note.isdigit():
                new = int(note)+diffs
                all_frets.add(new)
                if int(note) <= 9 and new > 9:
                    for k,v in newtune.items():
                        if k == newstring:
                            pass
                        else:
                            v[index] = '--'
                frets[index] = str(new)
    
    print()
    print('New Tab')
    print_tab(newtune)
    tab_write(newtune,target_file)
    print()
    print()
    #-----------------------------------------------------------------------
    #print(all_frets)
    
    #sum(1 for num in all_frets if num >= 12) == len(all_frets)
    all_two_digit = all(num >= 12 for num in all_frets)

    
    if all_two_digit:
        for newstring in newtune:
            frets = newtune[newstring]
            for index,note in enumerate(frets):
                if note.isdigit():
                    new = int(note)-12
                    frets[index] = str(new)
                    if new < 10:
                        for k,v in newtune.items():
                            if k == newstring:
                                pass
                            else:
                                v[index] = '-'
    
        print()
        print('Shifted Down 12, Lower Octave')
        print_tab(newtune)
        tab_write(newtune,target_file)
        for i in range(4):
            print()

print("Done")
    
