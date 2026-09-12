import random
print('')
def dist(point0,point1):
    length = (((point0[0]-point1[0])**2+(point0[1]-point1[1])**2)**(1/2))
    return length

def avg(lists):
    sum = 0
    for i in lists:
        sum += i
    return sum/len(lists)

numpoints = 10
sqr = 5
a = [(random.randint(-sqr,sqr),random.randint(-sqr,sqr)) for i in range(numpoints)]
print(a)
avgx = sum([i[0] for i in a])/len(a)
avgy = sum([i[1] for i in a])/len(a)


def avg_dist(point,group):
    b = avg([dist(point,i) for i in group])
    return round(b,3)

min_val = (2*(sqr**2))**(1/2)
min_point = 0
for y in range(sqr,-sqr-1,-1):
    row = {(x,y):avg_dist((x,y),a) for x in range(-sqr,sqr+1)}
    for k,v in row.items():
        if v < min_val:
            min_point = k
            min_val = v
    print(row)
print('Actual', avgx,avgy)
print('Estimate', min_point)