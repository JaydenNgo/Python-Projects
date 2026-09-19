import random
import math

def dist(point0,point1):
    x0, y0 = point0
    x1, y1 = point1
    dx, dy= (x0-x1), (y0-y1)
    length = math.sqrt((dx*dx)+(dy*dy))
    return length

def avg(lists):
    return sum(lists)/len(lists)

numpoints = 10
sqr = 5
a = [(random.randint(-sqr,sqr),random.randint(-sqr,sqr)) for _ in range(numpoints)]
print(a)
avgx = sum([i[0] for i in a])/len(a)
avgy = sum([i[1] for i in a])/len(a)


def avg_dist(point,group):
    b = avg([dist(point,i) for i in group])
    return round(b,3)

min_val = math.sqrt(2*sqr*sqr)
min_point = 0
for y in range(sqr,-sqr-1,-1):
    row = {(x,y):avg_dist((x,y),a) for x in range(-sqr,sqr+1)}
    for k,v in row.items():
        if v < min_val:
            min_point = k
            min_val = v
    print(row)
print('Actual', avgx, avgy)
print('Estimate', min_point)