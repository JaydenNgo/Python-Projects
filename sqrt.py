import math
num = 2356578679

def guess_sqrt(num, guess, iterations):
    if iterations <= 1:
        return guess
    else:
        return guess_sqrt(num, 0.5*(guess+num/guess), iterations-1)

def guess_sqrt_iter(num):
    estimate = int(math.sqrt(num))
    x = 0
    guess = num//2
    while int(guess) != estimate:
        x += 1
        guess = 0.5*(guess+num/guess)

    return x

with open("data.txt", "w") as file:
    for i in range(10, 100_000):
        p = f"{i}, {guess_sqrt_iter(i)}\n"
        print(p, end = '')
        file.write(p)
