import random
numc = 3
numr = 3
printit = False

def print_row(a):
  if printit == False:
    return
  for i in a:
    print(i, end=' ')
  print('')

def print_board(a):
  if printit == False:
    return
  print('') 
  print('  ',end = ' ')
  print_row(range(1,numr+1))
  for ind,i in enumerate(a):
    print(ind+1, end = '  ')
    print_row(i)
  print('')  

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

repeat = 10000
count = {'O': 0, 'X': 0, 'Tie': 0}
for i in range(repeat):
  board = [['-' for i in range(numr)] for j in range(numc)]
  #print_board(board)
  available = [(i,j) for i in range(1,4) for j in range(1,4)]
  win = False
  token = ['O','X']
  while True:
    if win == True:
      break
    for i in token:
      if win == True:
        break
        
      while True:
        pos = available[random.randint(0,len(available)-1)]
        available.remove(pos)
        #print(pos)
        
        x = pos[0]
        y = pos[1]
        
        if board[x-1][y-1] == '-':
          insert(i,pos[0],pos[1])
          if len(available) <= 0:
            #print('')
            #print('Tie')
            count['Tie'] += 1
            win = True
            break
          if check_board(board,i) == True:
            #print('')
            #print(f'Player {i} Wins!')
            count[i] += 1
            win = True
            break

        
        else:
          continue
        print_board(board)
        break

print_board(board)
for k,v in count.items():
  print(k,':',v, (v*100/repeat),'%')
