import random

def p(n):
    sums = 0
    for i in range(n):
        sums += random.uniform(-1,1)**2
    #print(sums)
    return sums

# n dimensions
# t times
def large(n, t):
    yes = 0
    no = 0
    for i in range(t):
        if p(n) <= 1:
            yes += 1
        else:
            no += 1

    print(yes,no)
    return (yes,no)

large(9,1000000)