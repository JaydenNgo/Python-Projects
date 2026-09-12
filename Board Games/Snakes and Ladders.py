import random
def dice_roll():
    return random.randint(1,6)

def avg(list):
    return sum(list)/len(list)

snakes = {32:10, 36:6, 48:26, 62:18, 88:24, 95:56, 97:78}
ladders = {1:38, 4:14, 8:30, 21:42, 28:76, 50:67, 71:92, 80:99}
#average of 34 turns
snakediff = avg([v-k for k,v in snakes.items()])
ladderdiff = avg([v-k for k,v in ladders.items()])

#print(snakediff)
#print(ladderdiff)

def single_player():
    pos = 0
    num_turns = 0
    while pos < 100:
        pos += dice_roll()
        if pos in snakes:
            pos = snakes[pos]
            #print(f'Down to {pos}')
            
        elif pos in ladders:
            pos = ladders[pos]
            #print(f'Up to {pos}')
        num_turns += 1
    return num_turns
    
        
total_rolls = 0
repeat = 100000
for i in range(repeat):
    total_rolls += single_player()

print(total_rolls/repeat)
print(snakediff,ladderdiff)
