import random

people = [chr(i) for i in range(65,91)]

def printcorner(state):
    print()
    for k,v in state.items():
        print(k,v)
    print()


def assign(people):
    #Give everyone still playing a corner
    picks = {i:random.randint(1,4) for i in people}

    #Create 4 corners and everyone's spot
    corners = {i:[] for i in range(1,5)}
    for k,v in picks.items():
        #print(k,v)
        corners[v].append(k)
    return corners

def eliminate(people):
    state = assign(people)
    printcorner(state)

    target = random.randint(1,4)
    print("Removingcorner: ", target)
    if len(state[target]) == 0:
        print("No one is there")
        return
    for i in state[target]:
        print(i, "eliminated")
        people.remove(i)
    print()


while (len(people) > 1):
    eliminate(people)

if len(people) == 1:   print(people[0], "is the Winner!")
elif len(people) == 0: print("Everyone eliminated")
