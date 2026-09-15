import random
import time
from concurrent.futures import ProcessPoolExecutor



BINGO = [[i+j for i in range(1,15+1)] for j in range(0,75,15)]
def make_bingo_board():
    B = random.sample(BINGO[0], 5)
    I = random.sample(BINGO[1], 5)
    N = random.sample(BINGO[2], 4)
    G = random.sample(BINGO[3], 5)
    O = random.sample(BINGO[4], 5)
    return set().union(B,I,N,G,O)


class Bingo:
    def __init__(self):
        self.board = make_bingo_board()
        self.marked = 1

    def clear_num(self, num):
        if num in self.board:
            self.marked += 1
            return True
        return False



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
    repeats = 1_250_000
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



