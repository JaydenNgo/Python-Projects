import time
import sys

sys.setrecursionlimit(2000000)

#Changes timeit returns time and value
#Make cache to expand
'''
def timeit(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    print(f"Time took: {elapsed:.6f} seconds")
    return result
'''
def timeit(func, parameter):
  start = time.perf_counter()
  result = func(*parameter)
  end = time.perf_counter() - start
  print(f"{end:.7f} seconds")
  return result
  

def stepcount(n,steps):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return sum(stepcount(n-s,steps) for s in steps)

def memsteps_cache(n,steps,cache):
    #print(n)
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in cache:
        return cache[n]
    else:
        total = sum(memsteps_cache(n-s,steps,cache) for s in steps)
        cache[n] = total
        return total


def memsteps(n,steps):
    return memsteps_cache(n,steps,{})


stairs = 5000
steps = (1,3,5)

'''
start = time.perf_counter()
for i in range(stairs+1):
    print(f"Regular time {i}: ", end='')
    reg = timeit(stepcount,(i,steps))
    #print(reg)
end = time.perf_counter() - start
print(f"{end:.7f} seconds total")
print()
'''
'''
start = time.perf_counter()
for i in range(stairs+1):
    print(f"Memo version {i}: ", end='')
    value = timeit(memsteps, (i,steps))
    #print(value)
end = time.perf_counter() - start
print(f"{end:.7f} seconds total")
print()

'''
cache = {}
start = time.perf_counter()
print("Initialize:",cache)
for i in range(stairs+1):
    #print(f"Stair {i}: ", end='')
    value = timeit(memsteps_cache,(i,steps,cache))
print(value)
#print(cache)
end = time.perf_counter() - start
print(f"{end:.7f} seconds total")
print()
