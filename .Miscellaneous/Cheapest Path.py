# https://www.youtube.com/watch?v=h7EmrFyTCmw&list=LL&index=79
import random
# Currently tries ever path, add cost and memoization or tabulation

n = 4
a = [[random.randint(1,9) for i in range(n)] for j in range(n)]
cost = 0
posx, posy = 1,1
final_path = []
lowest_cost = (9*n)+1

def print_board(board):
  for i in board:
    print(i)
  print()

arrows = {(0,-1): "\u2191",   #Up
          (0,1): "\u2193",    #Down
          (-1,0): "\u2190",   #Left
          (1,0): "\u2192",    #Right
          (1,1): "\u2198",    #Down right
          (1,-1): "\u2197",   #Upper right
          (-1,1): "\u2199",   #LL
          (-1,-1): "\u2196"   #UL
          }

def print_path(msg, path):
  print(msg, end= ' ')
  for i in path:
    print(arrows[i], end=' ')
  print()

def print_point(grid,x,y):
  point = grid[x-1][y-1]
  # print(f"Current point: {point}: {y} {x}")
  return point

def neighbors(grid,x,y):
  vector = [-1,0,1]
  available = []
  for i in vector:
    for j in vector:
      if not (i or j):
        continue
      if not (0 < x+i <= n) or not (0 < y+j <= n):
        continue
      if grid[x+i-1][y+j-1] == 0:
        continue
      
      # print("Available", grid[x+i-1][y+j-1], (i,j))
      available.append((i,j))
  #print(available)
  return available
      
def move_point(grid,x,y,dx,dy,cost):
  cost += grid[x-1][y-1]
  # print("Direction", arrows[(dx,dy)])
  grid[x-1][y-1] = 0
  return (x+dx,y+dy,cost)


def search(grid,x,y,cost,path):
  neighbor = neighbors(grid,x,y)
  

  if (x,y) == (n,n):
    cost += grid[n-1][n-1]
    grid[n-1][n-1] = 0
    #print("Reached")
    #print_board(grid)
    #print("Final cost: ", cost)
    #print_path("Final path: ", path)
    global final_path
    global lowest_cost
    if cost < lowest_cost:
      lowest_cost = cost
      final_path = path

    return    #return cost?

  if len(neighbor) == 0:
    #print("Dead End\n")
    return
  
  for v in neighbor:
    dx,dy = v
    clone = [[j for j in i] for i in grid]
    copy_path = [i for i in path]
    copy_path.append(v)
    # print("Cost so far: ", cost)
    newx,newy,costs = move_point(clone,x,y,dx,dy,cost)
    #print_point(grid,x,y)
    #print_board(grid)
    search(clone,newx,newy,costs,copy_path)   


search(a,posx,posy,0,[])
print("\nOriginal")
print_board(a)

print(lowest_cost)
print_path("Solution Path", final_path[::-1])
