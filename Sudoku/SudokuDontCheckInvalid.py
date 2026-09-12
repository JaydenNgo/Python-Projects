import time
a = [[list(range(1,10)) for i in range(9)] for j in range(9)]

#Print board with all possibilities
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
#Help figure out which square you are in
def bound(num):
  a = 3*(num//3)
  return (a,a+3)

clear_count = 0
#17944061
def clear_all(board,num,x,y):
  row = [board[x][i] for i in range(9)]
  col = [board[i][y] for i in range(9)]
  square = [board[i][j] for j in range(*bound(y)) for i in range(*bound(x))]
  all = (row,col,square)
  #all = (row,square,col)
  
  for seq_type in all:
    save = []
    for seq in seq_type:
      # global clear_count; clear_count+= 1
      if len(seq) == 1:
        if seq in save: return False              #If duplicate found, raise error     
        else: save.append(seq); continue          #Otherwise save to be checked and skip remove
      if num in seq: seq.remove(num)
  
  return True


#Take input and clear new inputs
script = [
          '4,1', '5,2',
          'D', '7,5', '6,7', 
          'D', '2,8', '8,9', 
          'D', '9,4', '5,5', 
          'D', '8,2', '6,3',
          'D', '2,2', '6,4',
          'D', '4,7', '7,8', '6,9', 
          'D', '7,2', '4,5', '5,6', 
          'D', '8,3', '9,6', 
          'D'
        ]

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

size_count = 0
#Returns total number of options of a board
#Use to check if size changes
def size(a):
  count = 0
  for i in a:
    for j in i:
      count += len(j)
      global size_count; size_count += 1
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

empty_count = 0
#Find the next square with mutliple options
def find_empty(boards,ptr):
  for i in range(ptr,9):
    for j in range(9):
      global empty_count
      empty_count += 1
      if len(boards[i][j]) != 1:
        return (i,j)
      
multi_count = 0
solutions = []

def multiscan(board,checks,ptr):
  i,j = find_empty(board,ptr)
  #print(i,j)
  #print_board_clean(board)
  sq = board[i][j]
  for k in sq:                                      #Assert that each option is correct/valid
    b = clone(board)
    b[i][j] = [k]

    global multi_count; multi_count += 1
    #print("Count",multi_count)

    new_board,new_checks,solved = scan(b,checks)      #Split the returned values: unsolved vs solved
    if not new_board: continue                        #If board produced error, skip the option
    #print_board_clean(new_board)

    if not solved: multiscan(new_board,new_checks,i)    #Recursively move to the next square and transfer new checked lis
    else: solutions.append(new_board)                   #Save if solved  


           
test = True
if test:
  start = time.time()
  multiscan(board,precheck,0)
  end = time.time()
  print()
  print(len(solutions), "Solutions")
  
  duration = end-start
  print(f"Runtime: {duration//60} min {duration%60:.3} s")
  print("Checked/Clone count", multi_count)
  print("Increments from size()", size_count)
  print("Clears checks", clear_count)
  print("Increments from find_empty", empty_count)

  print()
  print(f"~ {multi_count/duration:.7} boards checked per second")
  print("\n\n\n")

'''
Increments from size() 67571496
Clears checks 0
Increments from find_empty 750891
'''


'''
for i in solutions:
  print_board_clean(i)
'''
