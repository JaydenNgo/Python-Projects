import random
bases = ("A","T","G","C")

# Generates a random sequence of introns and extrons
# Introns are lowercase, Exons are uppercase
# num_codes: Number of subsequences (Intron/Exons)
# code_len: Length of codon, default 3
# min_len/max_len: Min and Max number of codons per subsequence
def random_seq(num_codes,min_len,max_len,code_len=3):
    full = ''
    for i in range(num_codes):
        sub = "".join([random.choice(bases) for i in range(code_len*random.randint(min_len,max_len))])
        # 50/50 chance of being an Intron or Exon
        if random.randint(0,1):
            sub = sub.lower()
        full += sub
    return full


# Splices strings depending on the upper/lower case
# Returns list of splices
def splice_seq(seq):
    front = 0
    splices = []
    # set mode depending on casing of first letter
    mode = 0 if seq[0].islower() else 1
    # Find each time the case changes and save the substring
    for index,i in enumerate(seq):
        if (not mode and i.isupper()) or (mode and i.islower()):
            mode = not mode
            sub = seq[front:index]
            splices.append(sub)
            front = index

    sub = seq[front:len(seq)]
    splices.append(sub)
    return splices



full = random_seq(10,3,5)
print(full)
print()
for i in splice_seq(full):
    print(f"{'Exon' if i.isupper() else 'Intron'}\t {i}")
print("\n\n\n")

bio = "TACgtaagtatcttttacagAACCTAAACAATgtatgatcctttctagCGGCTTTTTgtaagtttttcccagACATTGTAAgtattttttctttcagAGAACAAAAgtatgtttgttttcagCTATGCTACACT"

for i in splice_seq(bio):
    print(f"{'Exon' if i.isupper() else 'Intron'}\t {i}")