import time
a = [[[i for i in range(1,10)] for j in range(9)] for k in range(9)]

#Print board with options
def print_board(a):
  for i in a:
    print(i)
    print()
  print()
  
#Print board as if it was a real sudoku board
def print_board_clean(a):
  for i in a:
    for j in i:
      if len(j) == 1:
        print(j, end=' ')
      else:
        print("[.]", end=' ')
    print()
  print()

#Clones board without changing original
def clone(board):
  return [[[k for k in j] for j in i] for i in board]

#[1,2,3][4,5,6][7,8,9]
def bound(num):
  a = 3*(num//3)
  return (a,a+3)

count = 0
def clear_all(board,num,x,y):
  row = [board[x][i] for i in range(9)]
  col = [board[i][y] for i in range(9)]
  square = [board[i][j] for j in range(*bound(y)) for i in range(*bound(x))]
  all = (row,col,square)
  
  for i in all:
    save = []
    for seq in i:
      if len(seq) == 1:
        if seq in save: return False              #If duplicate found, raise error     
        else: save.append(seq); continue          #Otherwise save to be checked and skip remove
      if num in seq: seq.remove(num)

  global count; count += 1
  return True


#Take input and clear new inputs
script = [
          'D', '7,5', '6,7', 
          'D', '2,8', '8,9', 
          'D', '9,4', '5,5', 
          'D', '8,2', '6,3', '2,7', 
          'D', '2,2', '6,4', '7,7',
          'D', '4,7', '7,8', '6,9', 
          'D', '7,2', '4,5', '5,6', 
          'D', '8,3', '9,6', 
          'D']

# '4,1','5,2','D', '2,3', '7,5', '6,7', 'D', '2,8', '8,9', 'D', '9,4', '5,5', 'D', '8,2', '6,3', '2,7', 'D', '2,2', '6,4', '7,7', '5,8', 'D', '4,7', '7,8', '6,9', 'D', '7,2', '4,5', '5,6', 'D', '8,3', '9,6', 'D']

precheck = []
board = clone(a)
row = 1
while 0 < row < 10:
  for coord in script:
    if coord in ("u","U"):
      row -= 1
    elif coord in ("d","D"):
      row += 1
    else:
      num, col = int(coord[0]), int(coord[2])
      row1, col1 = row-1, col-1
      board[row1][col1] = [num]
      clear_all(board,num,row1,col1)
      precheck.append((row1,col1))
  break
#print(precheck)


'''
row = 1
while 0 < row < 10:
  while True:
    coord = input(f"Row {row}: ")
    if len(coord) not in [1,3]:
      continue
    if coord == "u" or coord == "U":
      row -= 1
    elif coord == "d" or coord == "D":
      row += 1
    else:
      num = int(coord[0])
      col = int(coord[2])
      a[row-1][col-1] = [num]
      clear_all(num,row,col)
    break
  '''


#Returns total number of options of a board
#Use to check if size changes
def size(a):
  count = 0
  for i in a:
    for j in i:
      count += len(j)
  return count
      
#Clears the board until no more changes can be made
def scan(a,checks):
  checked = [i for i in checks]                     #Inherit the checked of the previous board
  while True:
    prev = size(a)                                  #Save previous size
    for i in range(9):
      for j in range(9):
        if (i,j) in checked:                        #If coordinate in checked, skip
          continue
        if len(a[i][j]) == 1:
          if not clear_all(a,a[i][j][0],i,j):       #If produced error, raise unsolvable to Multiscan()
            return (False,False,False)
          checked.append((i,j))                     #Otherwise add position to checked

    new = size(a)
    if new == prev: return (a,checked,False)        #If size doesn't change, flag infinite loop, return unsolved
    if new == 81: return (a,checked,True)           #If board is full, flag as solved
    #else scan again    

print("Original Board")
print_board_clean(board)
print()

def find_empty(boards,ptr):
  for i in range(9):
    if i < ptr: continue 
    for j in range(9):
      if len(boards[i][j]) != 1:
        #print(i,j)
        return (i,j)
      
counts = 0
solutions = []

def multiscan(board,checks,ptr):
  i,j = find_empty(board,ptr)                       #Find the next square with mutliple options
  sq = board[i][j]
  for k in sq:                                  #Assert that each option is correct/valid
    b = clone(board)
    b[i][j] = [k]

    global counts; counts += 1
    #print("Count",counts)

    new_board,new_checks,solved = scan(b,checks)      #Split the returned values: unsolved vs solved

    if not new_board: continue                        #If board produced error, skip the option
    #print_board_clean(new_board)

    if not solved: multiscan(new_board,new_checks,i)    #Recursively move to the next square and transfer new checked lis
    else: solutions.append(new_board)                 #Save if solved  


           
test = True
if test == True:
  start = time.time()
  multiscan(board,precheck,0)
  end = time.time()
  print()
  print(len(solutions), "Solutions")
  
  duration = end-start
  print("Runtime: ", duration//60,"min", round(duration%60,3),"s")
  print("Checked", counts)
  print("Small checks", count)
  print()
  print("~" ,round(counts/duration,3), "boards checked per second")
  #print(solved_checks)

'''
for i in solutions:
  print_board_clean(i)
'''
