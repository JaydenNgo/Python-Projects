import random
num_col = 6
num_row = 7
empty = '-'
board = [[empty for i in range(num_row)] for j in range(num_col)]
#------------------------------------------------------------------------
def print_row(a):
  for i in a:
    print(i, end=' ')
  print()

#------------------------------------------------------------------------
def print_board(a):
  print()
  #print_row(range(1,num_row+1))
  for i in a:
    print_row(i)
  for i in range(1,8):
    print(i,end=' ')
  print()
#------------------------------------------------------------------------
def check_win(x,y,token):
  fourcorners = []

def inbound(a,b):
    if (0 <= a < num_col) and (0 <= b < num_row):
        return True
    else:
        return False

def diag(a,b,mode):
    if mode == 'l':
        b1 = -1
    if mode == 'r':
        b1 = 1

    line = []
    for i in range(3):
        if inbound(a-1,b+b1):
            a,b = a-1,b+b1
            continue
        else:
            break
    for i in range(7):
        if inbound(a,b):
            line.append(board[a][b])
            a,b = a+1,b+(-b1)
        else:
            break
    return line


def star(a,b,token):
  rows = []
  column = [i[b] for i in board]
  row = board[a]
  rows.append(column)
  rows.append(row)
  rows.append(diag(a,b,'l'))
  rows.append(diag(a,b,'r'))
  return rows
  
    
def sublist(sub,main):
  for i in range(len(main)-len(sub)+1):
    if main[i:i+len(sub)] == sub:
      return True
  else:
    return False


#------------------------------------------------------------------------

token = ['O','X']
unsolved = True
while unsolved:
  for i in token:
    if unsolved == False:
      break
    solved = [i for k in range(4)]
    while True:
      print_board(board)
      c = input(f'{i} Pick a column ')
      if len(c) <= 0:
        continue
      else:
        c = int(c)
      print()
      #c = random.randint(1,7)
      if c < 1 or c > num_row:
        print('Invalid')
        continue
      
      for ind,row in enumerate(board[::-1]):
        if row[c-1] == empty:
          row[c-1] = i
          r1 = c-1
          c1 = 5-ind
          for j in star(c1,r1,i):
            if sublist(solved,j):
              unsolved = False
              print(f'{i} WINS!')
              break
          break
      else:
        print('Column full')
        continue
      break
print_board(board)

