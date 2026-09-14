import random
num_col = 6
num_row = 7
empty = '-'
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
def check_space(a):
  for i in a:
    if empty in i:
      return True
  else: 
    return False

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
count = {'O':0,'X':0,'T':0}
token = ['O','X']
repeats = 100000
for p in range(repeats):
  board = [[empty for i in range(num_row)] for j in range(num_col)]
  unsolved = True
  while unsolved:
    for i in token:
      solved = [i for k in range(4)]
      if unsolved == False:
        break
      if check_space(board) == False:
        count['T'] += 1
        unsolved = False
        #print()
        #print("TIED GAME----------------")
        break
        
      while True:
        #print_board(board)
        c = random.randint(1,7)
        for ind,row in enumerate(board[::-1]):
          if row[c-1] == empty:
            row[c-1] = i
            r1 = c-1
            c1 = 5-ind
            for j in star(c1,r1,i):
              if sublist(solved,j):
                unsolved = False
                #print()
                #print(f'{i} WINS! {r1+1},{6-c1}')
                count[i] += 1
                break
            break
        else:
          #print('Column full')
          continue
        break
  #print_board(board)

for k,v in count.items():
   print(k,v,100*v/repeats,"%")
