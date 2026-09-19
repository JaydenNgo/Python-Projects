import csv
anions = ['Chloride', 'Bromide', 'Iodide', 'Oxide', 'Sulfide', 'Hydroxide', 'Carbonate', 'Chromate', 'Sulfate', 'Acetate', 'Nitrate']
cations = ['Ammonium', 'Sodium', 'Potassium', 'Magnesium', 'Calcium', 'Barium', 'Manganese(II)', 'Iron(II)', 'Iron(III)', 'Copper(II)', 'Nickel(II)', 'Cadmium', 'Zinc', 'Tin(II)', 'Mercury(II)', 'Lead(II)', 'Silver']

numbered_anions = {i:ind for ind,i in enumerate(anions)}
numbered_cations = {i:ind for ind,i in enumerate(cations)}
#print(numbered_anions)
#print(numbered_cations)
print()

Mid = 0.5
conversion = {"TRUE":True, "FALSE":False, "0.5":Mid, "None":None}

with open('Solubility.csv', 'r') as file:
  chart = [[conversion[j] for j in i[1:]] for i in csv.reader(file)]


def is_soluble(cation,anion):
   return chart[numbered_cations[cation]][numbered_anions[anion]]

def experiment(ions):
   cats = [i for i in ions if i in cations]
   ans =  [i for i in ions if i in anions]
   precipitates = []
   for i in cats:
      for j in ans:
         solubility = is_soluble(i,j)
         print(f"{i} {j}\t{solubility}")
         if solubility == False:
            precipitates.append(f"{i} {j}")
   print()
   if len(precipitates):
      for i in precipitates:
         print(f"{i} is a precipitate")
   else:
      print(f"All soluble")
   
#name = input("What ionic compounds are being dissolved")
#print(name)
name = "silver nitrate + potassium chromate"
name = [i[0].upper() + i[1:] for i in name.split()]
experiment(name)
print()
