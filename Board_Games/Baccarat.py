import random
deck = [i for i in range(1,11) for j in range(4)] + [10 for i in range(12)]
random.shuffle(deck) 
    
def move(a,b,t=1,n=0):
    for i in range(t):
        b.append(a[n])
        a.remove(a[n])

def score(l):
    return sum(l)%10

#num_players = int(input('How many players ')) 
num_players = 4

players = {f'Player {i}': [] for i in range(1,num_players+1)}
#print(players)
print()

for player,hand in players.items():
    banker = []
    move(deck,banker,2)
    print('Banker: ', banker, score(banker))

    move(deck,hand,2)
    print(player,hand, score(hand))
    print()

    if score(banker) > score(hand):
        print('Banker Wins!')
    elif score(banker) < score(hand):
        print(player, 'Wins!')
    else:
        print('Tie')
    print()








    

