import math

def art(layer:int):
    first = "+-+"
    second = "| |"
    first2 = "+-"
    for i in range(layer):
        print(first)
        print(f"{'  '*i}{second}")
        print(f"{'  '*i}{first2}", end="")
    print("+")

sums = 0
for i in range(1,int(1e8)):
    #print(i, sums)
    sums += 1 / (i*i)
print(i, sums)

"""
+-+
| |
+-+-+
  | |
  +-+-+
    | |



"""