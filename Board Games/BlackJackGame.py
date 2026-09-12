#Everyone starts with 2, but dealer only shows one (Change odds based on hidden card?)
#After everyone declares Dealer adds until 17+
#ace = 11 until sum > 11
#Add split and double down

#add splitting maybe
import random
face = {'a':1, 'j':10, 'q':10,'k':10}
deck = [i for i in range(1,11) for j in range(4)] + [10 for i in range(12)]
random.shuffle(deck)

'''
#Input number of players
while True:
  num_players = input('Number of players?: ')
  if num_players.isdigit() == False:
    print("Not a number")
    continue
  num_players = int(num_players)
  if not (0 < num_players < 7):
    print("Number of players Invalid")
    continue
  break
'''

num_players = 3

def remain(n):
  c = 0
  for i in deck:
    if i <= n:
      c += 1
  return c

def count_ace(hand):
  count = 0
  for i in hand:
    if i == 1:
      count += 1
  return count

def draw(hand):
  hand.append(deck.pop())

downed = []
busted = []
blackjack = []

def odds(hand):
  return round(100*remain(21-sum(hand))/len(deck),3)
  

def print_hands(reveal=False):
  print()
  if reveal == False: print("Dealers hand", [dealer[0]])
  if reveal == True:  print("Dealers hand", dealer, sum(dealer))
  for k,v in hands.items():
      if k in blackjack: print(k, v, "has hit blackjack")
      elif k in busted: print(k, v, sum(v), "has busted")
      else: print(k, v, sum(v), odds(v), "%")
  print()
  
hands = {f'Player {i+1}': [] for i in range(num_players)}
dealer = []

for i in range(2):
  draw(dealer)
  for v in hands.values():
    draw(v)

print_hands(False)
print_hands(True)




for player,hand in hands.items():                                               #For each player
  print('-'*50)
  while True:
    if odds(hand) >= 25: card = 'h'
    elif odds(hand) <= 25: card = 's'
    else: card = input(f'What would {player} like to do (hit,stand): ').lower()    #Player Input
      
    if card not in ('h','hit','s','stand'):
      print("Invalid input")
      continue
    
    if card in ('s','stand'): break
    if card in ('h','hit'):
      draw(hand)
      print(f"{player} drew a {hand[-1]}")
      

    if sum(hand) > 21: 
      busted.append(player)
      print_hands()   
      break
          #Ace and 10                             or  blackjack
    if (count_ace(hand) == 1 and sum(hand) == 11) or sum(hand) == 21: 
      blackjack.append(player)
      print_hands()   
      break

    else:
      print_hands()      
      continue

for i in busted: del hands[i]





if sum(dealer) >= 17: print("Dealer is at 17")
else:
  while sum(dealer) < 17:
    draw(dealer)
    print("Dealer: ", dealer, sum(dealer))
if sum(dealer) > 21: print("Dealer busted!")
if sum(dealer) == 21: print("Dealer hit blackjack")

print()
print("GAME FINISHED","-"*30)
print_hands(True)
print()

if len(blackjack) > 0:
  for i in blackjack:
    print(f"{i} hit blackjack with {hands[i]}")
elif len(hands) <= 0:
  print("Everyone busted, Dealer Wins")
  
    
print()

#Compare all hands

#print(deck)


