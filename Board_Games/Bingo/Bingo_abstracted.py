import random
import time
from concurrent.futures import ProcessPoolExecutor



def make_bingo_board():
    bingo = [num for j in range(0,75,15) for num in random.sample([i+j for i in range(1,15+1)],5) ]
    bingo.pop(12)
    return set(bingo)


class Bingo:
    def __init__(self):
        self.board = make_bingo_board()
        self.marked = 1

    def clear_num(self, num):
        if num in self.board:
            self.marked += 1
            return True
        return False

    

def play_bingo(num_board1, num_board2):
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
                if board.check_blackout():
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

def bingo_trials(repeats):
    rounds = {i:0 for i in range(25,76)}
    numbers = list(range(1,76))
    
    for _ in range(repeats):
        bingo = Bingo()    
        random.shuffle(numbers)
        for index, num in enumerate(numbers,1):
            if bingo.clear_num(num):
                if bingo.marked == 25:
                    rounds[index] += 1
                    break
    return rounds
        


if __name__ == "__main__":
    start = time.perf_counter()

    results = []
    num_workers = 8
    repeats = 1_2500_000
    totals = num_workers * repeats
    print(f"Total trials: {totals:,}")
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(bingo_trials, repeats) for _ in range(num_workers)]
        for future in futures:
            results.append(future.result())

    end = time.perf_counter() - start

    total_count = {i:0 for i in range(25,76)}
    for counts in results:
        for k,v in counts.items():
            total_count[k] += v

    allow = False
    for k,v in total_count.items():
        if v == 0:
            continue
        else:
            allow = True
        if allow:
            print(f"{k}, {v:,}")

    print(f"{end//60} minutes and {end%60} seconds")


    with open("data.txt", "w") as file:
        for k,v in total_count.items():
            row = f"{k}, {100*v/totals:.8f}\n"
            #print(row, end = '')
            file.write(row)



