#add ace mechanic
#add splitting maybe

face = {'a':1, 'j':10, 'q':10,'k':10}
deck = [i for i in range(1,11) for j in range(4)] + [10 for i in range(12)]

num_players = int(input('Number of players?: '))
hands = {f'Player {i+1}': [] for i in range(num_players)}
players = [i for i in range(num_players)]

def remain(n):
  c = 0
  for i in deck:
    if i <= n:
      c += 1
  return c

def print_hands():
  print()
  for k,v in hands.items():
      cards_left = remain(21-sum(v))
      if k in blackjack: print(k, v, "has hit blackjack")
      elif k in folded: print(k, "has folded")
      elif k in busted: print(k, v, "has busted")
      else: print(f"{k} {v} cards left {cards_left} {round(100*cards_left/len(deck),3)}%")
  print()


folded = []
busted = []
blackjack = []
x = 0
while len(deck) > 0:
  if len(blackjack) != 0:
    for i in blackjack:
      print(f"{i} hit blackjack with {hands[i]}")
    break
  for k,v in hands.items():
    if k in folded or k in busted:
      continue
    while True:
      card = input(f'What card did {k} draw?: ').lower()
      if card.isdigit():
        card = int(card)

      elif card in face:
        card = face[card] 

      if card not in deck and card not in ('fold','stand'):
        print('Card not in deck')
        continue
      if card in ('fold','stand'):
        folded.append(k)
        break

      v.append(deck.pop(deck.index(card)))

      if sum(v) > 21: busted.append(k)
      if 1 in v and sum(v) == 11: blackjack.append(k)
      if sum(v) == 21: blackjack.append(k)
      break
  print_hands()
print()
print(deck)












