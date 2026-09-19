import random
import time

length = 3
'''
2 nodes
2,1
3,4
4,7
5,12
6,
'''

'''
3 nodes
2,2
3,9

'''



def set_board(length):
  #'y':(1,length), 'a':(length,1)
  coord = {'x':(1,1), 'y':(1,length),'z':(length,length)}
  board = [[[] for i in range(length)] for j in range(length)]
  for k,v in coord.items():
    x,y = v
    board[x-1][y-1] = [k]
  print_board(board,coord)
  return coord,board

def print_board(a,coord):
  return
  #Print each coordinate
  for k,v in coord.items():
    print(k,tuple(v))
    
  for i in a:
    for j in i:
      if len(j) == 0:
        print("[.]", end=' ')
      else:
        print(f"[{(j[0])}]", end=' ') 
    print("\n")
    #print()
  print()


def delta(num):
  num += random.randint(-1,1)
  if num < 1: num = 1
  elif num > length: num = length
  return num

def shift(p):
  x,y = coord[p]                    #Current coord
  board[x-1][y-1].remove(p)               #Remove it
  coord[p] = (delta(x), delta(y))   #New coord
  x,y = coord[p]                    
  board[x-1][y-1].append(p)               #Add to new coord
  #print(coord[p])

def all_collide():
  #Get first dictionary item
  for v in coord.values():
    norm = v
    break
  #print("Here", norm)
  for v in coord.values():
    if v != norm:
      return False
  else:
    return True



check = {}
for j in range(10**5):
  count = 0
  coord,board = set_board(length)
  while all_collide() is False:
    for i in coord:
      shift(i)
    print_board(board,coord)
    count += 1
    #time.sleep(1.5)

  #print("Time:", count)
  if count not in check:
    check[count] = 1
  else:
    check[count] += 1

check = dict(sorted(check.items()))

maxi = 0
max = 0
with open("CollisionData.txt",'w') as file:
  for k,v in check.items():
    file.write(f"{k},{v}\n")
    if v > max:
      maxi,max = k,v

print("Argmax:", maxi)