import random
gene = ("A","T","C","G")
inf = float("inf")
nan = float("nan")
numstr = 20
lenstr = 100
lensub = 5
strings = {j+1: ''.join([random.choice(gene) for i in range(lenstr)]) for j in range(numstr)}

for k,v in strings.items():
  print(k,v)
print()

def search(a, b):
  print(f"{''*10} String {a} --- String {b}\n")  
  
  string1 = strings[a]
  string2 = strings[b]
  if string1 == string2:
    print(" Same String \n")
    return (a,b,nan,nan)
  
  diff = 0
  matches = 0
  for j in range(1,lenstr):         #Iterate through every size
    for i in range(lenstr+1-j):     #Iterate through substring of size
      clip = string1[i:i+j]         
      if clip in string2 and len(clip) >= lensub:
        ind = string2.index(clip)
        print(clip,i,ind)
        matches += 1
        diff += (i-ind)**2
        #diff += abs(i-ind)

  diff = diff**(1/2)
  avg = diff/matches if matches else nan
  stat = (a,b,matches,avg)

  print()
  print("Total", matches)
  print("Average", avg)
  print()

  return stat

# Compare 1 string to the rest individually
def compare_all(strings, a):
  return [search(a,i) for i in strings]
  
# Compare each unique combination
def compare_everything(strings):
  return [search(i,j+1) for i in strings for j in range(i,len(strings))]


# Prints the sequence with dividers 
# every "10" characters to find indices better
def print_seq(string,split=10):  
  new = "|".join([string[i:i+10] for i in range(0,len(string),split)])
  print(new)

# Prints out the number of matches, distance average, 
# and accuracy of each comparison from a list of stats
# Highlights the 2 strings with the highest accuracy
# returns the 2 strings (a,b)
def print_stats(stats):
  print()
  print("SUMMARY:")
  print("Full String Size:", lenstr)
  print("Substring Size:  ", lensub)

  print("-------- Matches -- Avg -------- Accuracy")

  maxpair = ""
  max_accuracy = 0
  for a,b,matches,avg in stats:
    accuracy = matches/avg if avg else nan
    sub = str(a) + "-" + str(b) + ":"
    print(f"{sub:8} {matches:<10} {avg:.3f} \t {accuracy:.3f}")
    if accuracy > max_accuracy: 
      max_accuracy = accuracy
      maxpair = a,b

  a,b = maxpair
  print()
  print(f"String {a} and {b} have the highest accuracy of {max_accuracy}")

  print(a, strings[a])
  print(b, strings[b])
  #print_seq(strings[a])
  #print_seq(strings[b])
  print()
  search(a,b)
  print()
  return (a,b)



best_a, best_b = print_stats(compare_all(strings,1))
#print_stats(compare_everything(strings))

# Checks matching letters in matching indices
# Returns a string highlighting the matches
def match(a,b):
  string1 = strings[a]
  string2 = strings[b]
  matched = []
  num_matches = 0
  for i,j in zip(string1,string2):
    if i == j:
      matched.append(i)
      num_matches += 1
    else:
      matched.append("-")
  matched = "".join(matched)
  print(f"{100*num_matches/len(string1)}% match")
  return matched
  

print(match(best_a,best_b))

