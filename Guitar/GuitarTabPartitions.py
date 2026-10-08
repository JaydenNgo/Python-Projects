# TO DO
# Add restart
# Check out to the Hellfire chorus
# Check why DT Winter isnt showing more subtunings
# Add chords / Multiple strings in a single note

# Insertion and deletion in the middle of the tab
# also with cursor
# Keep or remove the # lines for break ?
# add f 12 for quick and easy additions------
# should I add strip for certain things?

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
    if version == "STANDARD":
        tune = [shift(i,diff) for i in standard]

    elif version == "DROP":
        tune = [shift(i,diff+2) for i in standard]
        tune[0] = root
        
    return tune

# Allows user to input tuning for tab
# Returns dictionary: 
# Key  =  each note
# Value = empty list
def add_strings():
    strings = {}
    while True:
        y = input('Add string: ').upper()
        if 'DROP' in y or 'STANDARD' in y:
            inp = y.split()
            if len(inp) != 3:
                print("Invalid Tuning \n")
                continue 

            #Drop tuning
            if 'DROP' in y:
                mode, note, num_strings = inp

            #Standard Tuning
            if 'STANDARD' in y:
                note, mode, num_strings = inp
        
            #Error Checking
            if not num_strings.isdigit():
                print("Missing number of strings")
                continue
            if int(num_strings) > 7:
                print("Too many strings\n")
                continue
            if int(num_strings) < 4:
                print("Not enough strings\n")
                continue
            if note not in conversion:
                print("Invalid note")
                continue
            
            else:
                num_strings = int(num_strings)
                for i in tuning(note, mode, num_strings)[::-1]:
                    if i in strings:
                        strings[i[0]+i] = []    #If open string note shows up multiple times
                    else:
                        strings[i] = []
                break

        #Manually add Tuning
        if len(y) == 0:
            if len(strings) == 0:
                print("There are no strings, please add some :D")
                continue
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
        print_tab(strings)
    print()
    return strings

# Take user input Tuning and confirmation
def get_tuning():
    while True:
        strings = add_strings()
        for i in strings:
            print(i)
        print()
        reset = input('Confirm (Y/N) ').upper()
        if reset in ("Y","YES"):
            return [strings]
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
def print_tab(strings: dict, current_string: str = None):
    for string, notes in strings.items():
        print(f'{string:4}{"".join(notes)}', end = '')
        if string == current_string:
            print(" <--")
        else:
            print()
    print("\n")

#Initialize tab file
def create_tab_file():
    file_name = input("Give this tab a name \n")
    target_file = f"tabs/{file_name}.txt"
    with open(target_file, "w") as file:
        file.write(file_name)
        file.write(" Tabs \n\n")
        print()
    return target_file

def write_to_tab_file(strings: dict, file_name: str):
    #Create a copy
    copied_strings = {k:[i for i in v] for k,v in strings.items()}
    maxlen = max(len(v) for v in copied_strings.values())

    #Remove all buffers
    for i in range(maxlen-1,-1,-1):
        line = [frets[i] for frets in copied_strings.values()]
        if line == ['-' for _ in copied_strings]:
            for frets in copied_strings.values():
                del frets[i]

    #Write tab so you can copy to Google Sheets =D
    max_string_name = len(max(strings))
    with open(file_name, "a") as file:
        for string, frets in copied_strings.items():
            file.write(f'{string}{" "*(max_string_name-len(frets))} \t')
            for i in frets:
                if i.isdigit() or i == '#': 
                    file.write(i)
                file.write("\t")
            file.write("\n")
        file.write("\n")


def get_input_for_fulltab(tabs = list[dict]):
    segment_ptr = 0
    current_subtab = tabs[segment_ptr]
    tuning = list(current_subtab)
    while True:
        inp = get_input_for_subtab(current_subtab)
        if inp == "Done":
            break

        if inp == "Split":
            tabs.append({string:[] for string in tuning})
            segment_ptr = len(tabs)-1
            current_subtab = tabs[segment_ptr]
            #print_tab(current_subtab)

        if isinstance(inp, int):
            if not (1 <= inp <= len(tabs)):
                print(f"Segment does not exist, try {1}-{len(tabs)}!")
                continue
            segment_ptr = inp-1
            current_subtab = tabs[segment_ptr]
            #print_tab(current_subtab)

    print("\n\n\n")
    print("-"*50)
    full_tab = {string:[] for string in tuning}
    for count, subtab in enumerate(tabs,1):
        print(f"Segment {count}:")
        print_tab(subtab)
        ask = input("continue? (Y/N)?").upper()
        print()
        if ask not in ("Y", "YES"):
            return get_input_for_fulltab(tabs)
        for string, frets in subtab.items():
            full_tab[string] += frets
    print_tab(full_tab)
    #Add check for if they like full tab
    
    return full_tab


def get_input_for_subtab(strings: dict):
    list_of_strings = [i for i in strings]
    num_strings = len(list_of_strings)
    string_ptr = 0

    while True:
        target_string = list_of_strings[string_ptr]
        print_tab(strings, target_string)
        print(f"Current string: {target_string}")
        fret = input('Fret ').upper()
        print()

        if fret == "DONE":
            return "Done"
        
        if fret in ("U","UP"):
            if string_ptr <= 0:
                print("Can't go higher")
            else:
                string_ptr -= 1
            continue

        if fret in ("D","DOWN"):
            if string_ptr >= num_strings-1:
                print("Can't go lower")
            else:
                string_ptr += 1
            continue
    
        if fret in ("SPLIT","BREAK"):
            #Add minimum split size
            for v in strings.values():
                if len(v) == 0:
                    print("No values to split")
                    break
                v += ["-","#","-"]
            print()
            print_tab(strings, target_string)
            return "Split"

        if fret[:9] == "SWITCH TO":
            target_segment = fret[9:].strip()
            if target_segment.isdigit():
                return int(target_segment)
            else:
                print("Not a segment number")
                continue

        #Retrieve Multiplier
        multiplier = 1
        if 'X' in fret:
            print(fret.split("X"))
            if len(fret.split("X")) != 2:
                print("Too many inputs")
                continue

            fret, multiplier = fret.split("X")
            print(multiplier, multiplier.isdigit())
            if not multiplier.isdigit():
                print("Invalid multiplier")
                continue
            multiplier = int(multiplier)
            if multiplier <= 0:
                print("Please have a positive multiplier")
                continue

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

        # Add to Tab ------------------------------
        for _ in range(multiplier):              
            if fret == 'GAP':
                for i in strings:
                    strings[i].append('-')
    
            elif fret == 'UNDO':
                repeats = 1
                for v in strings.values():
                    if len(v) <= 0:
                        print("No more tab left \n")
                        repeats = 0                   #Flag error
                        break
                if repeats <= 0: 
                    break
        
                # If last entry is number and buffer, delete 2
                for v in strings.values():
                    if v[-2].isdigit(): 
                        repeats = 2 
                        break
            
                for i in range(repeats):
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
    
        print_tab(strings, target_string)
        print() 
    





def string_is_empty(notes: list[str]):    
    for i in notes:
        if i not in ('-','--','#'):
            return False
    return True
    # return all(char in ('-','--','#') for char in notes)

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
        if len(new_tuning) < len(og_strings):
            print('Not enough strings')
            continue

        for i in new_tuning:
            print(i)
        print()

        reset = input('Confirm (Y/N) ').upper()
        if reset in ("Y","YES"):
            return list(new_tuning)
        continue

def translate(og_strings: dict, new_tuning: list[str], target_file: str):
    #For each subtuning
    print_tab(og_strings)
    num_strings = len(og_strings)
    size_diff = len(new_tuning) - num_strings
    strings_notes = true_notes(og_strings)

    for i in range(size_diff+1):
        #print(new_tuning)
        sub_tuning = new_tuning[i:i+num_strings]
        print(sub_tuning)

        new_strings = {j:[] for j in sub_tuning}
        newtune_notes = true_notes(new_strings)

        # Clones tab w/ new tuning names
        for x,y in zip(og_strings, new_strings):
            new_strings[y] = [k for k in og_strings[x]]

        #Find the distances between each string
        diff_list = []
        for x,y in zip(strings_notes, newtune_notes):
            diff = conversion[x]-conversion[y]
            if diff < 0:
                diff += 12
            diff_list.append(diff)

        # Translate the subtuning
        all_frets = sub_translate(new_strings, diff_list, target_file)

        # If all frets are 12+, also show lower on the fretboard
        if all(num >= 12 for num in all_frets):
            down_an_octave(new_strings, target_file)
        

def sub_translate(new_strings: dict, diff_list: list[str], target_file: str):
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
    write_to_tab_file(new_strings, target_file)
    print("\n")
    
    return all_frets

def down_an_octave(new_strings: dict, target_file: str):
    # If all frets are 12+, also show lower on the fretboard
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
    write_to_tab_file(new_strings,target_file)
    print("\n\n\n")

    return None
#------------------------------------------------------------------------------------
print()
print('Input strings from Highest to Lowest')
print('If you have a repeated letter, use the letter twice, (A and AA, A# and AA#)')
print('You can also type presets like "Drop G 7" or "E Standard 6"')
print()

strings = get_tuning()
print()

print('Original Tuning')
print_tab(strings[0])

target_file = create_tab_file()
write_to_tab_file(strings[0], target_file)


print('You start on the highest string')
print('You can use "u"/"up" and "d"/"down" to traverse the strings')
print('Then type the fret on the given string')
print('If you want to do multiple of the same note do (12x4)')
print('"Gap" if you want to make spaces between notes (gapx3)')
print('"Undo" to remove the latest note (undox3)')
print('"Break" to create segments in the tabs')
print('"Switch to n" to move between segment n')
print('"Done" to stop the program and translate the tabs')
print('Not case sensitve =D')
print()


full_strings = get_input_for_fulltab(strings)
# Many inputs later
print()
print('Original Tab')
print_tab(full_strings)
print()
  
# Cut out strings that aren't used
if cut_tab(full_strings):
    print()
    print("Cut strings")
    print_tab(full_strings)
    write_to_tab_file(full_strings, target_file)

print('\nPlease add the New tuning\n')
new_tuning = get_new_tuning(full_strings)

print("\n\n\n")
print("TRANSLATION\n")

translate(full_strings, new_tuning, target_file)
print("Done")
  
