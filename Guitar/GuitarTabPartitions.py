#TO DO
#Add restart
#Add title to display and file
#Check out to the Hellfire chorus
#Check why DT Winter isnt showing more subtunings
#Add sub sections
#Add chords

#Arrow so you know which line?
#Insertion and deletion in the middle of the tab
#also with cursor


conversion = {'A':0, 'A#':1, 'B':2, 'C':3, 'C#':4, 'D':5, 'D#':6, 'E':7, 'F':8, 'F#':9, 'G':10, 'G#':11}
rconv = {v:k for k,v in conversion.items()}

# Returns a note shifted up n semitones
def shift(note: str, n: int):
    return rconv[(conversion[note]+n) % 12]

# returns standard tuning for n strings (4-7)
def standards(n: int):
    standard = ['B','E', 'A', 'D', 'G', 'B', 'E']
    if   n == 4: return standard[1:5]
    elif n == 5: return standard[:5]
    elif n == 6: return standard[1:7]
    elif n == 7: return standard

# Returns drop or standard tuning depending on root note and # of strings
def tuning(root: str, version: str, num_strings: int):
    standard = standards(num_strings)
    diff = conversion[root] - conversion[standard[0]]
    if version == "standard":
        d = [shift(i,diff) for i in standard]

    elif version == "drop":
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
                num_strings = y[spaces[1]+1:]

            #Standard Tuning
            if 'STANDARD' in y:
                if len(y) < 12:
                    print("Missing value (E Standard 6)")
                    continue
                loc_note = y.index('STANDARD')
                mode = 'standard'
                note = y[:loc_note-1]
                num_strings = y[loc_note+9:]
        
            #Error Checking
            if int(num_strings) > 7:
                print("Too many strings\n")
                continue
            if note not in conversion:
                print("Invalid tuning")
                continue
            if num_strings.isdigit() == False:
                print("Missing number of strings")
                continue
            else:
                num_strings = int(num_strings)
                for i in tuning(note,mode,num_strings)[::-1]:
                    if i in strings:
                        strings[i[0]+i] = []    #If open string note shows up multiple times
                    else:
                        strings[i] = []
                break

        #Manually add Tuning
        if len(y) == 0:
            break
        if y in strings:
            print('Already added')
            continue
        if y in conversion:
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

# Take user input Tuning and confirmation
def get_tuning():
    while True:
        strings = add_strings()
        print()
        for i in strings:
            print(i)
        print()
        reset = input('Confirm (Y/N) ').upper()
        if reset in ("Y","YES"):
            return strings
        else:
            continue

#Get notes for calculation
def true_notes(strings: dict):
    notes = []
    for string in strings:
        if string[-1] in conversion:
            notes.append(string[-1])
        elif string[-1] == '#':
            notes.append(string[-2:])
        else:
            print('ERROR')
    return notes

# Print out tab
def print_tab(strings: dict):
    for string, notes in strings.items():
        print(f'{string:4}{"".join(notes)}')
    print("\n")

#Clear file
def create_tab():
    file_name = input("Give this tab a name \n")
    target_file = f"tabs/{file_name}.txt"
    with open(target_file, "w") as file:
        file.write(file_name)
        file.write(" Tabs \n\n")
        print()
    return target_file

def write_to_tab(strings: dict, file_name: str):
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

def add_to_tab(strings: dict ):
    list_of_strings = [i for i in strings]
    num_strings = len(list_of_strings)
    stringptr = 0

    while True:
        print('Current string:', list_of_strings[stringptr])
        fret = input('Fret ').upper()
        print()
        if fret == "DONE":
            break
        #if len(fret) == 0: break   
        
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
    
        # Use the multiplier
        target_string = list_of_strings[stringptr]
        for _ in range(multi):              
            if fret == 'GAP':
                for i in strings:
                    strings[i].append('-')

            elif fret == 'UNDO':
                rep = 1
                for v in strings.values():
                    if len(v) <= 0:
                        print("No more tab left \n")
                        rep = 0                   #Flag error
                        break
                if rep <= 0: 
                    break
        
                # If last entry is number and buffer, delete 2
                for v in strings.values():
                    if v[-2].isdigit(): 
                        rep = 2 
                        break
            
                for i in range(rep):
                    for v in strings.values():
                        if len(v) <= 0: 
                            break
                        else: 
                            del v[-1] 
        
        #Add to tab
        else:
            for i in strings:
                if i == target_string:
                    strings[target_string].append(str(fret))
                    strings[target_string].append('-')
                else:
                    if fret > 9:
                        strings[i].append('--')
                    else:
                        strings[i].append('-')
                    strings[i].append('-')
        print_tab(strings)
        print()
    return strings

def string_is_empty(notes: list):    
    for i in notes:
        if i not in ('-','--','#'):
            return False
    return True

# removes strings that aren't used
# returns whether strings were cut or not
def cut_tab(strings: dict):
    to_cut = [k for k,v in strings.items() if string_is_empty(v)]
  
    if len(to_cut) > 0:
        for i in to_cut:
            del strings[i]
        return True
    return False

def get_new_tuning(og_strings: dict):
    while True:
        new_tuning = add_strings()
        print()
        if len(new_tuning) < len(og_strings):
            print('Not enough strings')
            continue
        for i in new_tuning:
            print(i)
        print()
        reset = input('Confirm (Y/N) ').upper()
        if reset in ("Y","YES"):
            return list(new_tuning)
        else:
            continue

def translate(og_strings: dict, new_tuning: list):
    #For each subtuning
    print_tab(og_strings)
    num_strings = len(og_strings)
    size_diff = len(new_tuning) - num_strings

    for i in range(size_diff+1):
        print(new_tuning)
        sub_tuning = new_tuning[i:i+num_strings]
        print(sub_tuning)

        new_strings = {j:[] for j in sub_tuning}
        newtune_notes = true_notes(new_strings)

        # Clones tab w/ new tuning names
        for x,y in zip(og_strings, new_strings):
            new_strings[y] = [k for k in og_strings[x]]
    
        #print("New"); tab(new_strings)
        #print("OG"); tab(stog_stringsrings)

        #Find the distances between each string
        diff_list = []
        for x,y in zip(strings_notes, newtune_notes):
            diff = conversion[x]-conversion[y]
            if diff < 0:
                diff += 12
            diff_list.append(diff)

        all_frets = set()
        for newstring, diffs in zip(new_strings, diff_list):
            frets = new_strings[newstring]
            for index, note in enumerate(frets):
                if note.isdigit():
                    new = int(note)+diffs
                    all_frets.add(new)
                    # if single digit -> double digit
                    if int(note) <= 9 and new > 9:
                        for k,v in new_strings.items():
                            if k == newstring:
                                pass
                            else:
                                v[index] = '--'
                    frets[index] = str(new)
                    
        print()
        print('New Tab')
        print_tab(new_strings)
        write_to_tab(new_strings, target_file)
        print()
        print()
    #-----------------------------------------------------------------------
        #print(all_frets)
        
        # If all frets are 12+, also show lower on the fretboard
        all_two_digit = all(num >= 12 for num in all_frets)
        if all_two_digit:
            for newstring in new_strings:
                frets = new_strings[newstring]
                for index,note in enumerate(frets):
                    if note.isdigit():
                        new = int(note)-12
                        frets[index] = str(new)
                        if new < 10:
                            for k,v in new_strings.items():
                                if k == newstring:
                                    pass
                                else:
                                    v[index] = '-'
        
        print()
        print('Shifted Down 12, Lower Octave')
        print_tab(new_strings)
        write_to_tab(new_strings,target_file)
        for i in range(4):
            print()

#------------------------------------------------------------------------------------
print()
print('Input strings from Highest to Lowest')
print('If you have a repeated letter, use the letter twice, (A and AA, A# and AA#)')
print('You can also type presets like "Drop G 7" or "E Standard 6"')
print()

strings = get_tuning()
strings_notes = true_notes(strings)
print()

print('Original Tuning')
print_tab(strings)

target_file = create_tab()
write_to_tab(strings, target_file)


print('You start on the highest string')
print('You can use "u"/"up" and "d"/"down" to traverse the strings')
print('Then type the fret on the given string')
print('If you want to do multiple of the same note do (12x4)')
print('"Gap" if you want to make spaces between notes (gapx3)')
print('"Undo" to remove the latest note (undox3)')
print('"Break" to create segments in the tabs')
print('"Done" to stop the program and translate the tabs')
print('Not case sensitve =D')
print()


add_to_tab(strings)
print()
print('Original Tab')
print_tab(strings)
print()
  
# Cut out strings that aren't used
if cut_tab(strings):
    print()
    print("Cut strings")
    print_tab(strings)
    write_to_tab(strings, target_file)

print('\nPlease add the New tuning\n')
new_tuning = get_new_tuning(strings)

print("\n\n\n")
print("TRANSLATION\n")

translate(strings, new_tuning)
print("Done")
  
