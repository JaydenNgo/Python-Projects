import random
import time
from concurrent.futures import ProcessPoolExecutor



def make_bingo_board():
    bingo = [num for j in range(0,75,15) for num in random.sample([i+j for i in range(1,15+1)],5) ]
    bingo.pop(12)
    return set(bingo)


class Bingo:
    def __init__(self, owner):
        self.board = make_bingo_board()
        self.marked = 1
        self.owner = owner

    def clear_num(self, num):
        if num in self.board:
            self.marked += 1
            return True
        return False
    

def n_boards(n):
    return [Bingo("") for _ in range(n)]



#print_game(game)

def play_bingo(num_board1, num_board2):
    game = {"p1":n_boards(num_board1), "p2":n_boards(num_board2)}
    numbers = list(range(1,76))
    random.shuffle(numbers)
    states = {player:False for player in game}
    game_end = False
    #print_game(game)
    for num in numbers:
        for player, boards in game.items():
            for board in boards:
                if board.clear_num(num):
                    if board.check_blackout():
                        #print_game(game)
                        states[player] = True
                        game_end = True
        if game_end:
            break

    # for player, state in states.items():
    #     print(player,state)

    if states["p1"] and states["p2"]:
        #print("Tie")
        return "tie"

    elif states["p1"] and not states["p2"]:
        #print("Player 1 got blackout!")
        return "p1"

    elif not states["p1"] and states["p2"]:
        #print("Player 2 got blackout!")
        return "p2"

def new_play_bingo(num_board1, num_board2):
    p1_boards = [Bingo("p1") for _ in range(num_board1)]
    p2_boards = [Bingo("p2") for _ in range(num_board2)]
    all_boards = p1_boards + p2_boards

    numbers = list(range(1,76))
    random.shuffle(numbers)

    states = {"p1":False, "p2":False}
    game_end = False

    for num in numbers:
        for board in all_boards:
            if board.clear_num(num):        #If removed
                if board.marked == 25:
                    states[board.owner] = True
                    game_end = True
        if game_end:
            break


    if states["p1"] and states["p2"]:
        return "tie"

    #elif states["p1"] and not states["p2"]:
    elif states["p1"]:
        return "p1"

    #elif not states["p1"] and states["p2"]:
    else:
        return "p2"

def dual_trials(repeats):
    count = {"p1":0, "p2":0, "tie":0}
    for _ in range(repeats):
        count[play_bingo(1,10)] += 1
    return count

def new_dual_trials(repeats):
    count = {"p1":0, "p2":0, "tie":0}
    for _ in range(repeats):
        count[new_play_bingo(1,10)] += 1
    return count



#Original unflatten, 8 thread, 25k repeat --> 200_000 ~ 26 seconds
if __name__ == "__main__":
    start = time.perf_counter()

    results = []
    num_workers = 8
    repeats = 125_000
    print(f"Total trials: {num_workers*repeats:,}")
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(new_dual_trials, repeats) for _ in range(num_workers)]
        for future in futures:
            results.append(future.result())

    counts = {"p1":0, "p2":0, "tie":0}
    for count in results:
        for k,v in count.items():
            counts[k] += v
    
    for k,v in counts.items():
        print(f"{k}, {100*v/(repeats*num_workers)}")

    end = time.perf_counter() - start

   


    print(f"{end//60} minutes and {end%60} seconds")
    print()
    #print(f"{6/22}, {13/22}, {3/22}")



'''
#Prob of Tie is half of 1 board

1:1 --> (40:40:20) (2/5 : 2/5: 1/5)
1:2 --> (27.4 : 59.1: 13.5) {6/22}, {13/22}, {3/22}
1:3 --> (20.6 : 69.1: 10.3)
1:4 --> (16.4 : 75.34: 8.26)
1:5 --> (13.6 : 79.4: 7.0)
1:6 --> (11.7 : 82.3: 6.0)
1:7 --> (10.2 : 84.5: 5.3)
1:8 --> (8.06 : 86.21: 4.72)
1:9 --> (8.2 : 87.55: 4.25)
1:10 --> (7.4 : 88.7: 3.9)


'''