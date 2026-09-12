import random
import time
infinites = 0
sum = 0
repeat = 10000
start = time.time()

def move(fromm, too, n=0):
  too.append(fromm.pop(n))

# Returns list of players with the larger card in war
def victor(owner, war):
  return [k for k,v in owner.items() if v == max(war)]
  

for _ in range(repeat):
  deck = [i for i in range(2,15) for j in range(4)]
  random.shuffle(deck)
  n = 10
  #n = int(input('Number of players'))
  players = {str(n):[] for n in range(1,n+1)}

  # Hand everyone their hands
  while len(deck) > 0:
    for player,hand in players.items():
      if len(deck) == 0:
        break
      move(deck,hand)

  leftover = False
  # Every player has ‘equal’ part of the deck
  round = 0
  while True:
    round += 1
    length = [len(hand) for hand in players.values()]

    owner = {}
    war = []
    if leftover is False:
      spoils = []
  
    #Everyone puts a card into battle
    for player,hand in players.items():
      if len(hand) == 0:
        continue
      owner[player] = hand[0]
      move(hand,war)
 
    winner = victor(owner, war)
   
    # If 1 winner, shuffle the pile and give it to them
    if len(winner) == 1:
      random.shuffle(war)
      players[winner[0]] += war
   
   
    if len(winner) > 1:
      owner = {}
      spoils += war
      war = []

      for i in winner:
        hand = players[i]
        if len(hand) >= 3:
          move(hand, spoils)
          move(hand, spoils)
          owner[i] = hand[0]
          move(hand, war)
           
        elif len(hand) == 0:
          continue
       
        elif len(hand) < 3:
          owner[i] = hand[-1]
          move(hand, war, -1)
          while len(hand) != 0:
            move(hand, spoils)
  
      winner = victor(owner, war)
      spoils += war

      if len(winner) == 0:
        leftover = True
        continue
      random.shuffle(spoils)
      players[winner[0]] += spoils

    if max(length) >= 52:
      break
    if round > 5000:
      infinites += 1
      break

  sum += round


print(f"\nRESULTS:{sum/repeat}\n")
print(time.time()-start)