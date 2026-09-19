import math

inf = math.inf 

def f(x):
    return x**3

def scientific(x):
    deg = 0
    neg = True if x < 0 else False
    if neg:
        x = -x
    while x > 9:
        x /= 10
        deg += 1
    #print(x, deg)
    if neg:
        return f"{-x} * 10^{deg}"
    return f"{x} * 10^{deg}"
    
def degree(x):
    deg = 0
    neg = True if x < 0 else False
    if neg:
        x = -x
    while x > 9:
        x //= 10
        deg += 1
    #print(x, deg)
    return deg


# func^n(x0)
def dyn(func, n, x0):
    seq = []
    for i in range(n):
        x0 = func(x0)
        if x0 in seq:
            print(f"\t{len(seq)} cycle")
            break
        seq.append(x0)
    return x0

def gen_dyn(func, n, x0):
    seq = []
    for i in range(n):
        x0 = func(x0)
        if x0 in seq:
            print(f"\t{len(seq)} cycle")
            break
        seq.append(x0)
        yield x0

# Order of magnitude to consider divergence
inf_threshold = 500

def limit(func,n,x):
    for n0,i in enumerate(gen_dyn(func,n,x)):
        deg = degree(i)
        #print(deg)
        if deg > inf_threshold:
            print(f"n = {n0}, inf")
            return "div"
l = limit(f,10,2)
print(l)

'''
precision = 10
for i in range(-5*precision,(5+1)*precision):
    a = dyn(f,11,i)
    deg = degree(a)
    if deg > inf_threshold:
        deg = inf
    #print(scientific(a))
    print(i, deg)
'''
