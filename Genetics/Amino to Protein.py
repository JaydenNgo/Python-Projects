letter_to_fullname = { 
  "A": "Alanine",
  "R": "Arginine",
  "N": "Asparagine",
  "D": "Aspartic acid",
  "C": "Cysteine",
  "Q": "Glutamine",
  "E": "Glutamic acid",
  "G": "Glycine",
  "H": "Histidine",
  "I": "Isoleucine",
  "L": "Leucine",
  "K": "Lysine",
  "M": "Methionine",
  "F": "Phenylalanine",
  "P": "Proline",
  "S": "Serine",
  "T": "Threonine",
  "W": "Tryptophan",
  "Y": "Tyrosine",
  "V": "Valine"
}


# If any last nulceotide #, if uc or ag, ! for except
U_codon = { 
            "UUuc": "Phe (F)",
            "UUag": "Leu (L)",
            "UC#" : "Ser (S)",
            "UAuc": "Tyr (Y)",
            "UAag": "STOP",
            "UGuc": "Cys (C)",
            "UGA" : "STOP",
            "UGG" : "Trp (W)"
          }

C_codon = { 
            "CU#" : "Leu (L)",
            "CC#" : "Pro (P)",
            "CAuc": "His (H)",
            "CAag": "Gln (Q)",
            "CG#" : "Arg (R)"
          }

A_codon = { 
            "AU!G": "Ile (I)",
            "AUG" : "Met (M)",
            "AC#" : "Thr (T)",
            "AAuc": "Asn (N)",
            "AAag": "Lys (K)",
            "AGuc": "Ser (S)",
            "AGag": "Arg (R)",
          }

G_codon = { 
            "GU#" : "Val (V)",
            "GC#" : "Ala (A)",
            "GAuc": "Asp (D)",
            "GAag": "Glu (E)",
            "GG#" : "Gly (G)",
          }

Codon_key = {"U": U_codon, "C": C_codon, "A": A_codon, "G": G_codon}

print()
# Takes in a triplet codon and returns the 3 letter and 1 letter abbreviation of the corresponding Amino Acid
def codon_to_amino(code):
  code = code.upper()
  if len(code) != 3:
    return "Not a codon"
  
  # Check if valid Codon UCAG
  for i in code:
    if i not in Codon_key:
      return "Not a codon"

  # Grabs codons from the Starting Letter
  lib = Codon_key[code[0]]
  #print(lib)

  #If specific catch it early
  if code in lib:
    return lib[code]
  
  for key,value in lib.items():
    # If they share the same first two
    if code[:2] == key[:2]:
      tail = key[2:]
      #print(key,value)
      if tail == "#": return value
      elif "!" in tail: return value
      elif tail == "uc" and code[-1] in "UC": return value
      elif tail == "ag" and code[-1] in "AG": return value


'''
# Check that codon_to_amino() works
for i in Codon_key:
  for j in Codon_key:
    for k in Codon_key:
      codes = i+j+k
      print(codes, codon_to_amino(codes))
      #codon_to_amino(i+j+k)
'''

a = "3' - TAC … AAC CTA AAC AAT … CGG CTT TTT … ACA TTG TAA … AGA ACA AAA … CTA TGC TAC ACT - 5'"
primes = {"5":"3", "3":"5"}

# Finds the compliment of a DNA/RNA sequence
# Returns (5'/3' front, Sequence)
def compliment(seq, typee):
  seq = seq.upper()
  head = "5" if seq[0] == "3" else "3"
    
  if typee == "R": base = "U"
  else:            base = "T"

  pairs = {"A":base, "T":"A", "C":"G", "G":"C"}
  comp = ''
  for i in seq:
    if i in pairs:
      comp += pairs[i]

  return (head, comp)

# Returns a sequence with only nucleotides
# Returns (5'/3' front, Sequence)
def format(seq,typee):
  seq = seq.upper()
  head = "3" if seq[0] == "3" else "5"
    
  if typee == "R": base = "U"
  else:            base = "T"

  codes = (base,"A","G","C")
  comp = ''
  for i in seq:
    if i in codes:
      comp += i
  return (head, comp)


# Read DNA sequence's codons into Amino Acids
def seq_to_amino(seq):
  aminos = []
  for i in range(0,len(seq),3):
    triple = seq[i:i+3]
    amino = codon_to_amino(triple)
    
    print(triple,amino, end = ' ')
    letter = amino[-2]

    if letter in letter_to_fullname:
      print(letter_to_fullname[letter])
      aminos.append(letter)

    if amino == "STOP":
      print()
      break
  return aminos

def print_seq(message='', prime="5", seq=''):
  print(f"{message} {prime}' - {seq} - {primes[prime]}'")

print(a)
print_seq("RNA Compliment\t", *compliment(a,"R"))
print_seq("DNA Compliment\t",*compliment(a,"D"))
print_seq("Normal sequence\t",*format(a,"T"))
print()
frontc, comp_R = compliment(a,"R")

acids = seq_to_amino(comp_R)

print()
print(acids)
