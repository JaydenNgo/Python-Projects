import math
import numpy as np
import time

def numpy_integrate(func, a, b, n, method):
    dx = (b-a) / n
    total = 0

    if method == 'left':
        indices = np.arange(n, dtype=float)
    elif method == 'right':
        indices = np.arange(1, n+1, dtype=float)
    elif method == 'midpoint':
        indices = np.arange(0.5, n+0.5, dtype=float)
    elif method == "trapezoid":
        indices = np.arange(1, n, dtype=float)
        total += func(a) + func(b)
        total *= dx/2

    indices *= dx
    indices += a
    indices[:] = func(indices)
    indices *= dx
        
    return total + np.sum(indices)

def jump_search(func, a, b, mode, jump):
    # DONT start at 0
    sub_n = 1
    
    while jump >= 1:
        while abs(actual - numpy_integrate(func, a, b, sub_n, mode)) > margin_of_error :
            sub_n += jump
        
        sub_n -= jump
        jump /= 10

    return int(sub_n + 10 * jump)
        
    


#  f ( ((1...n) b-a/n ) + a ) * b-a/n

modes = ["left", "right", "trapezoid", "midpoint"]
a = 0
b = 1
actual = 2/3


margin_of_error = 1e-6

print(actual)
for mode in modes:
    sub_n = jump_search(np.sqrt, 0, 1, mode, 1e6)
    print(f"{mode:9}: {sub_n:,}")



        




