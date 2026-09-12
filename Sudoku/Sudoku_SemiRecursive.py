import time
from concurrent.futures import ProcessPoolExecutor, as_completed

# make multiscan return the list of solutions
def shrink(l):
  n = [str(i) if i in l else "." for i in range(1,10) ]
  #print(n)
  return ''.join(n)

def new_board():
  return [[list(range(1,10)) for i in range(9)] for j in range(9)]

#[1,2,3][4,5,6][7,8,9]
#Help figure out which square you are in
def bound(num):
  a = 3*(num//3)
  return (a,a+3)

def clone(board):
  return [[[k for k in j] for j in i] for i in board]

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
call_count = 0
sub_count = 0
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

  def print_board_thirds(self):
    print(f"|{'-'*13}|{'-'*13}|{'-'*13}|")
    for index_row,i in enumerate(self.board,1):
      for index_col,j in enumerate(i,1):
        if index_col == 1:
          print("|", end=' ')
        if len(j) == 1:
          print(j, end=' ')
        else:
          print("[.]", end=' ')
        if not index_col%3:
          print("|", end=' ')
      print()
      if not index_row%3:
        vert = "|" + "-" * 13
        print(f"{vert*3}|")
        print("", end = "")
    print()

  #Clones board without changing original
  def deep_clone(self):
    return Board(clone(self.board), self.size, self.next_empty, self.checked.copy())
  
  # Sets square to 1 number, Adjust self.size, automatically calls clear_all()
  def insert(self,num,x,y):
    self.size -= len(self.board[x][y])-1
    self.board[x][y] = [num]
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
          singleton = seq[0]
          if singleton in save:
            return False                        #If duplicate found, raise error     
          else:
            save.add(singleton)                 #Otherwise save to be checked and skip remove
            continue                            #?
        
        elif num in seq: 
          seq.remove(num)
          self.size -= 1
        
    return True
  
  # Clears the board until no more changes can be made
  # returns False if board is still not solved
  # returns True if board is solved
  # returns None if clearing resulted in error/contradiction
  def scan(self):
    while True:
      prev = self.size                                       #Save previous size
      for i in range(9):
        for j in range(9):
          if (i,j) in self.checked:                          #If coordinate in checked, skip
            continue
          if len(self.board[i][j]) == 1:
            if not self.clear_all(self.board[i][j][0],i,j):  #If produced error, raise unsolvable to Multiscan()
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
    global sub_count; sub_count += 1
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


  def main_scan(self, solution):
    global call_count; call_count += 1
    i,j = self.find_empty()
    
    for k in self.board[i][j]:                #Assert that each option is correct/valid
      start = time.perf_counter()
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
      end = time.perf_counter()-start
      print(f"{k} took {end:.3f} seconds")

  def threaded_main_scan(self, solution):
    i,j = self.find_empty()
    pool_start_time = time.perf_counter()
    with ProcessPoolExecutor() as executor:
      futures = {
        executor.submit(sub_scan, self, k, i, j): k 
        for k in self.board[i][j]
      }
      
      # Collect and merge results as they finish
      for future in as_completed(futures):
        k = futures[future]
        elapsed_time = time.perf_counter() - pool_start_time
        
        # Directly retrieve results and print completion info
        local_solutions = future.result()
        print(f"Branch choice {k} completed in {elapsed_time:.4f} seconds.")
        global sum_total; sum_total += elapsed_time

        if local_solutions:
          solution.extend(local_solutions)
      
  # Calls multiscan() and returns list of all solutions
  def all_solutions(self):
    solutions = []
    self.threaded_main_scan(solutions)
    return solutions

def sub_scan(board, k, i, j):
  b = board.deep_clone()
  b.insert(k, i, j)
  solved = b.scan()
  local_solutions = []
  
  if solved is None:
      return local_solutions
  elif not solved:
      b.next_empty = i
      b.multiscan(local_solutions)
      return local_solutions
  else:
      local_solutions.append(b.board)
      return local_solutions


#Take input and clear new inputs
'''
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

script = [
          '8,1', '2,2', '6,4', '1,9',
          'D', '8,6', 
          'D', '2,5', '9,6', 
          'D', '7,1', '6,3', '4,6', '1,8', 
          'D', '9,1', '4,3', '3,5', '8,8',
          'D', '3,3', '5,7',
          'D', '2,3', '3,4', '9,5', '5,6', '6,9',
          'D', '9,2', '8,4', '1,7', 
          'D', '2,4', '7,6', '9,8',
          'D'
        ]

print()
row = 1
while 0 < row < 10:
  for coord in script:
    if coord in ("u","U"):
      row -= 1
    elif coord in ("d","D"):
      row += 1
    else:
      num, col = int(coord[0]), int(coord[2])
      print(row-1,col-1,num)
      original.insert(num, row-1, col-1)
  break
  

# Michelle
a = [
  [8, 2, x, 6, x, x, x, x, 1], 
  [x, x, x, x, x, 8, x, x, x], 
  [x, x, x, x, 2, 9, x, x, x], 
  [7, x, 6, x, x, 4, x, 1, x], 
  [9, x, 4, x, 3, x, x, 8, x], 
  [x, x, 3, x, x, x, 5, x, x], 
  [x, x, 2, 3, 9, 5, x, x, 6], 
  [x, 9, x, 8, x, x, 1, x, x], 
  [x, x, x, 2, x, 7, x, 9, x]
]

'''
# '4,1','5,2','D', '2,3', '7,5', '6,7', 'D', '2,8', '8,9', 'D', '9,4', '5,5', 'D', '8,2', '6,3', '2,7', 'D', '2,2', '6,4', '7,7', '5,8', 'D', '4,7', '7,8', '6,9', 'D', '7,2', '4,5', '5,6', 'D', '8,3', '9,6', 'D']

'''
a = [
  [x, x, x, x, x, x, x, x, x], 
  [x, x, x, x, x, x, x, x, x], 
  [x, x, x, x, x, x, x, x, x], 
  [x, x, x, x, x, x, x, x, x], 
  [x, x, x, x, x, x, x, x, x], 
  [x, x, x, x, x, x, x, x, x], 
  [x, x, x, x, x, x, x, x, x], 
  [x, x, x, x, x, x, x, x, x], 
  [x, x, x, x, x, x, x, x, x]
]

start_board = [
  [4, 5, x, x, x, x, x, x, x], 
  [x, x, x, x, 7, x, 6, x, x], 
  [x, x, x, x, x, x, x, 2, 8], 
  [x, x, x, 9, 5, x, x, x, x], 
  [x, 8, 6, x, x, x, x, x, x], 
  [x, 2, x, 6, x, x, x, x, x], 
  [x, x, x, x, x, x, 4, 7, 6], 
  [x, 7, x, x, 4, 5, x, x, x], 
  [x, x, 8, x, x, 9, x, x, x]
]
'''

x = 'x'

start_board = [
  [4, 5, x, 2, x, x, x, x, x], 
  [x, x, x, x, 7, x, 6, x, x], 
  [x, x, x, x, x, x, x, 2, 8], 
  [x, x, x, 9, x, x, x, x, x], 
  [x, x, 6, x, x, x, x, x, x], 
  [x, 2, x, 6, x, x, x, x, x], 
  [x, x, x, x, x, x, x, 7, 6], 
  [x, 7, x, x, 4, x, x, x, x], 
  [x, x, 8, x, x, 9, x, x, x]
]



original = Board(new_board(), 9**3, 0, set())  #New board

for row, listt in enumerate(start_board):
  for col, num in enumerate(listt):
    if num != x:
      original.insert(num,row,col)


multi_count = 0
solutions = []
sum_total = 0
#9,489,072 (col,row,square)
#9,528,410 (row,col,square)

test = True
if __name__ == "__main__":
  #print(precheck)
  print("Original Board")
  original.print_board_clean()
  original.print_board_smol()
  print()
  #original.print_board()

  if test:
    start = time.perf_counter()
    solulu = original.all_solutions()
    duration = time.perf_counter()-start

    print(f"\n{len(solulu)} Solutions")
    print(f"Runtime: {duration//60} min {duration%60:.3} s\n")
    
    print(f"Would have been {sum_total//60} min {sum_total%60:.3} s")
    print("\n\n")


'''
for board in solulu:
  print_board_clean(board)
'''



