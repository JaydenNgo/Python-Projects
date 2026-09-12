import time


#Convert lists to sets
# find a way to access the only item in a set




# make multiscan return the list of solutions
def shrink(l):
  n = [str(i) if i in l else "." for i in range(1,9) ]
  #print(n)
  return ''.join(n)


def new_board():
  return [[set(range(1,10)) for i in range(9)] for j in range(9)]


#[1,2,3][4,5,6][7,8,9]
#Help figure out which square you are in
def bound(num):
  a = 3*(num//3)
  return (a,a+3)


def clone(board):
  return [[j.copy() for j in i] for i in board]


def first_item(iter):
  for i in iter:
    break
  return i


def print_board_clean(board):
  for i in board:
    for j in i:
      if len(j) == 1:
        print(j, end=' ')
      else:
        print("[.]", end=' ')
    print()
  print()


find_empty_count = 0
clear_count = 0
class Board:
  def __init__(self, board, size, next_empty, checked):
    self.board = board
    self.size = size
    self.next_empty = next_empty
    self.checked = checked


  #Print board with all possibilities in list format
  def print_board(self):
    for i in self.board:
      print(i)
      print()
    print()
 
  # Prints board with all possibilities in string format
  def print_board_smol(self):
    for i in self.board:
      string = [shrink(j) for j in i]
      print(string)
      print()
    print()
 
  #Print board as if it was a real sudoku board
  def print_board_clean(self):
    for i in self.board:
      for j in i:
        if len(j) == 1:
          print(j, end=' ')
        else:
          print("[.]", end=' ')
      print()
    print()


  #Clones board without changing original
  def deep_clone(self):
    return Board(clone(self.board), self.size, self.next_empty, self.checked.copy())
 
  # Sets square to 1 number, Adjust self.size, automatically calls clear_all()
  def insert(self,num,x,y):
    self.size -= len(self.board[x][y])-1
    self.board[x][y] = {num}
    self.clear_all(num,x,y)


  # Clears row, column, and square of a coordinate of num
  # returns False if clearing creates a duplicate/contradiction
  # returns True if successful
  def clear_all(self,num,x,y):
    row =    [self.board[x][i] for i in range(9)]
    col =    [self.board[i][y] for i in range(9)]
    square = [self.board[i][j] for j in range(*bound(y)) for i in range(*bound(x))]
    self.checked.add((x,y))
   
    #(row,col,square)
    for seq_type in (row,col,square):
      save = set()
      for seq in seq_type:
        global clear_count; clear_count+= 1
        if len(seq) == 1:
          singleton = first_item(seq)
          if singleton in save:
            return False                        #If duplicate found, raise error    
          else:
            save.add(singleton)                 #Otherwise save to be checked and skip remove
            continue                            #?
       
        elif num in seq:
          seq.discard(num)
          self.size -= 1
       
    return True
 
  # Clears the board until no more changes can be made
  # returns False if board is still not solved
  # returns True if board is solved
  def scan(self):
    while True:
      prev = self.size                                       #Save previous size
      for i in range(9):
        for j in range(9):
          if (i,j) in self.checked:                          #If coordinate in checked, skip
            continue
          if len(self.board[i][j]) == 1:
            if not self.clear_all(first_item(self.board[i][j]),i,j):  #If produced error, raise unsolvable to Multiscan()
              return None
      new = self.size
      if new == prev: return False                           #If size doesn't change, return unsolved
      if new == 81: return True                              #If board is full, flag as solved
      #else scan again  


  # Returns coordinate of next square that isn't determined
  def find_empty(self):
    for i in range(self.next_empty,9):
      for j in range(9):
        global find_empty_count; find_empty_count += 1
        if len(self.board[i][j]) != 1:
          return (i,j)


  # Recursively tries all combinations of given board and addes them to solutions
  def multiscan(self, solution):
    i,j = self.find_empty()
    for k in self.board[i][j]:                #Assert that each option is correct/valid
      b = self.deep_clone()
      b.insert(k,i,j)
      solved = b.scan()
      global multi_count; multi_count += 1


      if solved is None:                      #If board produced error, skip the option
        continue                              
      elif not solved:                        #Recursively move to the next square and transfer new checked list
        b.next_empty = i
        b.multiscan(solution)                        
      else:                                   #Save if solved  
        #solutions.append(b.deep_clone())
        solution.append(b.board)
       
  # Calls multiscan() and returns list of all solutions
  def all_solutions(self):
    solutions = []
    self.multiscan(solutions)
    return solutions






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




original = Board(new_board(), 9**3, 0, set())  #New board


row = 1
while 0 < row < 10:
  for coord in script:
    if coord in ("u","U"):
      row -= 1
    elif coord in ("d","D"):
      row += 1
    else:
      num, col = int(coord[0]), int(coord[2])
      original.insert(num, row-1, col-1)
  break




#print(precheck)
print("Original Board")
original.print_board_clean()
#original.print_board_smol()
print()
#original.print_board()




'''
row = 1
while 0 < row < 10:
  while True:
    coord = input(f"Row {row}: ")
    if len(coord) not in [1,3]:
      continue
    if coord in ("u","U"):
      row -= 1
    elif coord in ("d","D"):
      row += 1
    else:
      num, col = int(coord[0]), int(coord[2])
      original.insert(num,row-1, col-1)
    break
'''




multi_count = 0
solutions = []
#9,489,072 (col,row,square)
#9,528,410 (row,col,square)


test = True
if test:
  for i in range(1):
    start = time.perf_counter()
    solulu = original.all_solutions()
    duration = time.perf_counter()-start


   
    print(f"\n{len(solulu)} Solutions")
    print(f"Runtime: {duration//60} min {duration%60:.3} s\n")
    print(f"~ {multi_count/duration:.7} boards checked per second")
    print(f"Find empty checks {find_empty_count:,}")
    print(f"Clear checks {clear_count:,}")
    print("\n\n\n")
    original.print_board_clean()




'''
for board in solutions:
  print_board_clean(board)
'''





