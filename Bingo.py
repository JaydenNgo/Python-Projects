import random
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def shuffle(list):
    random.shuffle(list)
    return list


'''
    bingo = []
    for j in range(0,75,15):
        col = [i+j for i in range(1,15+1)]
        random.shuffle(col)
        print(col[:5])
        bingo.append(col[:5])
    '''

def make_bingo_board():
    bingo = [shuffle([i+j for i in range(1,15+1)])[:5] for j in range(0,75,15)]
    bingo = [list(row) for row in zip(*bingo)]
    bingo[2][2] = 'x'
    return bingo

def call_number():
    numbers = list(range(1,75+1))
    random.shuffle(numbers)
    for i in numbers:
        yield i


class Bingo:
    def __init__(self):
        self.board = make_bingo_board()
        self.marked = 1
        self.flat = [num for row in self.board for num in row]
        self.find = {num:index for index,num in enumerate(self.flat)}

    def print_board(self):
        print("B   I   N   G   O")
        for row in self.board:
            print(row)
        print()

    def clear_num(self, row, col):
        self.board[row][col] = 'x'
        self.marked += 1

    def check_bingo(self):
        pass

    def check_blackout(self):
        return self.marked == 25

def bingo_trials(repeats):
    rounds = {i:0 for i in range(24,76)}
    numbers = list(range(1,76))
    for _ in range(repeats):
        bingo = Bingo()    
        random.shuffle(numbers)
        for index, num in enumerate(numbers,1):
            if num in bingo.find:
                indice = bingo.find[num]
                bingo.clear_num(indice//5, indice%5)
                if bingo.check_blackout():
                    rounds[index] += 1
                    break
    return rounds



if __name__ == "__main__":
    start = time.perf_counter()

    num_workers = 8
    results = []
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(bingo_trials, 100_000) for _ in range(num_workers)]
        for future in futures:
            results.append(future.result())

    end = time.perf_counter() - start

    total = {i:0 for i in range(24,76)}
    for counts in results:
        for k,v in counts.items():
            total[k] += v
    


    print(f"{end//60} minutes and {end%60} seconds")


    with open("data.txt", "w") as file:
        for k,v in total.items():
            print(k,v)
            file.write(f"{k},{v}\n")