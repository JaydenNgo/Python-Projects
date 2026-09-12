import math
pi = math.pi

h = float(input("What is your height?: "))
r = float(input("What is your radius?: "))
s = int(input("How many segments?: "))

  
print()
volume = pi*h*r**2/3
print("Total volume is ", str(volume))
print()

for i in range(1,s+1):
  a0 = volume*(i/s)**3
  a1 = volume*((i-1)/s)**3
  ratio = a0-a1
  print(f"Layer {i} has a volume of {ratio}, {round(100*ratio/volume,3)} %")
print()
