import time

def hail(x):
    #print(x)
    if x <= 1:
        return 0
    if x%2 == 0:
        return hail(x//2) + 1
    if x%2 == 1:
        return hail(3*x+1) + 1   
    
def hail_cache(x,cache):
    #print(x)
    if x <= 1:
        return 0
    if x in cache:
        return cache[x]
    if not x%2:
        turns = hail_cache(x//2,cache) + 1
        cache[x] = turns
        return turns
    else:
        turns = hail_cache(3*x+1,cache) + 1
        cache[x] = turns
        return turns

def timeit(func, parameter):
  start = time.perf_counter()
  result = func(*parameter)
  end = time.perf_counter() - start
  print(f"{end:.7f} seconds")
  return result
    
    
max = 5*10**6
'''
start = time.perf_counter()
for i in range(1,max+1):
    a = hail(i)
    # print(i,a)
    # print(f"{i} takes {a} turns")
end = time.perf_counter() - start
print(a)
print("Took",end,"seconds")
'''
cache = {}
start = time.perf_counter()
for i in range(1,max+1):
    a = hail_cache(i,cache)
    # print(i,a)
    # print(f"{i} takes {a} turns")

end1 = time.perf_counter() - start
print(a)
print("Took",end1,"seconds")

with open("HailstoneCache.txt", "w") as file:
    for k,v in cache.items():
        file.write(f"{k},{v}\n")
#print(cache)
print()

'''
with open("File.txt", "w") as file:

    start = time.perf_counter()
    for i in range(1,max+1):
        a = hail(i)
        # print(i,a)
        #print(f"{i} takes {a} turns")
    end = time.perf_counter() - start
    print("Took",end,"seconds")

    start = time.perf_counter()
    cache = {}
    for i in range(1,max+1):
        a = hail_cache(i,cache)
        # print(i,a)
        file.write(f"{i},{a}\n")
        #print(f"{i} takes {a} turns")
    print(a)
    end1 = time.perf_counter() - start
    print("Took",end1,"seconds")
    #print(cache)
    print()
'''