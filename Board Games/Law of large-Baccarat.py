import random

def move(deck,person,t=1):
    for _ in range(t):
        person.append(deck.pop())

def score(l):
    return sum(l)%10

#num_players = int(input('How many players ')) 
num_players = 1

Banker_count = 0
Player_count = 0
Tie_count = 0
repeats = 1000000


for i in range(repeats):
    deck = [i for i in range(1,11) for j in range(4)] + [10 for i in range(12)]
    random.shuffle(deck) 
    players = {f'Player {i}': [] for i in range(1,num_players+1)}

    for player,hand in players.items():
        banker = []
        move(deck,banker,2)
        move(deck,hand,2)
        
        if score(banker) > score(hand):
            Banker_count += 1
        elif score(banker) < score(hand):
            Player_count += 1
        else:
            Tie_count += 1

def stats(n):
    percent = round(n*100/(repeats*num_players),2)
    print(n, percent, '%')

print()
stats(Banker_count)
stats(Player_count)
stats(Tie_count)
print()







    

