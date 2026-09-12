a = "SsYyWW"
b = "SsYy"

# Boolean, checks whether a and b are the same letter no matter of casing
def same_letter(a,b):
  return a == b.upper() or a == b.lower()

# Checks a string and makes sure it is a possible string of alleles
# Returns boolean
def isallele(a):
  length = len(a)
  # if Odd
  if length % 2:
    print("Not Even error")
    return False

  for i in range(0,length,2):
    first = a[i]
    second = a[i+1]
    if not same_letter(first,second):
      print("Not binary error")
      return False
  return True

# Returns a list of every letter used for traits of a string
def getTraits(a):
  phenos = []
  for i in range(0,len(a),2):
    first = a[i]
    second = a[i+1]
    if same_letter(first,second):
      #print(first,second)
      phenos.append(first.upper())
    else:
      print("ERROR")
      break

  #print(phenos)
  return phenos

# Checks whether or not two strings use the same letters for traits
# Returns boolean
def checkTraits(a,b):
  if isallele(a) and isallele(b):
    return getTraits(a) == getTraits(b)
  else:
    print("Not an allele")
    return False
  
if checkTraits(a,b):
  print("Match")

#------------------------------------------------------------

# Splits string into allele pairs
# Returns list of len2 strings
def splits(string):
  return [string[i]+string[i+1] for i in range(0,len(string),2)]

# Generates allele combinations
def comb(a):
  if len(a) == 1:
    for i in a[0]:
      yield i
  else:
    for i in comb(a[:-1]):
      for j in a[-1]:
        yield i + j


allele = [i for i in comb(splits(a))]
print(allele)

# Returns sorted version of string
def sort_string(string):
  return "".join(sorted(string))

# Prints tab-space items of a list in 1 line
def print_list(list):
  for i in list:
    print(f"\t{i}", end = ' ')
  print()

# Creates punnett square for alleles a and b
# Returns list of combinations for allele1, allele2 and nested list of each cross
def punnett(a,b):
  allele1 = [i for i in comb(splits(a))]
  allele2 = [i for i in comb(splits(b))]
  square = [["".join([sort_string(x+y) for x,y in zip(i,j)]) for i in allele1] for j in allele2]
  return (allele1,allele2,square)

# Prints out punnett square
# pass any nested list for different charts
def print_square(a1,a2,square):
  print_list(a1)
  for i,j in zip(a2,square):
    print(i, end = ' ')
    print_list(j)
  print()

# Determines Dominant or Recessive for each allele
# replaces Dominant with D and Recessive with r
def phenotype(string):
  pheno = ''
  for i in splits(string):
    if i[0].isupper():
      pheno += "D" 
    else:
      pheno += "r"
  return pheno

# Determines Homo/Heterozygous for each allele
# replaces Homo-Dominant with  D
# replaces Homo-Recessive with R
# replaces Heterozygous with   H
def genotype(string):
  gene = ''
  for i in splits(string):
    if i[0].isupper() and i[1].isupper():
      gene += "D"
    elif i[0].islower() and i[1].islower():
      gene += "R"
    else:
      gene += "H"
  return gene


a = "SsYyWW"
b = "SsYyWw"

a1, a2, square = punnett(a,b)
print_square(*punnett(a,b))

phen = [[phenotype(i) for i in j] for j in square]
geno = [[genotype(i) for i in j] for j in square]
print_square(a1,a2,phen)
print_square(a1,a2,geno)



def count_analyze(lists):
  features = ["D","H","R"]
  # counts = {i:{} for i in features}
  counts = {"D":{},"H":{},"R":{}}
  for i in lists:
    for j in i:
      first = j[0]
      rest = j[1:]
      #print(first,rest)
      
      if first in counts:
        outer = counts[first]
        if rest in outer:
          outer[rest] += 1
        else:
          outer[rest] = 1

  print("\tD\tH\tR")
  for i in counts["D"]:
    print(i, end = '\t')
    for j in features:
      print(counts[j][i], end = '\t')
    print()
  print()
  
  


count_analyze(geno)

print("\n\n\n")