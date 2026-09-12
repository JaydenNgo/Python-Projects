numc = 3
numr = 3
board = [['-' for i in range(numr)] for j in range(numc)]

def print_row(a):
  for i in a:
    print(i, end=' ')
  print('')

def print_board(a):
  print('') 
  print('  ',end = ' ')
  print_row(range(1,numr+1))
  for ind,i in enumerate(a):
    print(ind+1, end = '  ')
    print_row(i)
  print('')  
  
print_board(board)

def insert(i,x,y):
  board[x-1][y-1] = i

def check_board(board, tokens):
  win_con = [tokens for i in range(3)]
  alls = [i for i in board]
  for i in range(3):
    alls.append([j[i] for j in board])
  alls.append( [board[i][i] for i in range(3)]   )
  alls.append( [board[i][2-i] for i in range(3)] ) 
  
  if win_con in alls:
    return True
  return False

win = False
token = ['O','X']
while True:
  if win == True:
    break
  for i in token:
    if win == True:
      break
      
    while True:
      pos = list(input(f'{i} Place piece x,y '))
      if len(pos) != 3:
        print('Invalid input')
        continue
      pos = [int(i) for i in pos if i.isdigit() == True]
      x = pos[0]
      y = pos[1]
      if x < 0 or x > 3 or y < 0 or y > 3:
        print('Invalid Postion')
        continue
      if board[x-1][y-1] == '-':
        insert(i,pos[0],pos[1])
        if check_board(board,i) == True:
          print('')
          print(f'Player {i} Wins!')
          win = True
          break
      else:
        print('Spot taken')
        continue
      print_board(board)
      break


print_board(board)

