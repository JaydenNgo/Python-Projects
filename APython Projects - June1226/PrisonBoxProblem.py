# https://www.youtube.com/watch?v=vIdStMTgNl0
# https://www.youtube.com/watch?v=iSNsgj1OCLA
import random
import time

def speed(func, value):
  start = time.time()
  output = func(value)
  end = time.time() - start
  print(f"Function took {end} seconds")
  return output, end 

def make_boxes():
  a = list(range(1,101))
  random.shuffle(a)
  return {index:i for index,i in enumerate(a,1)}

def gen_boxes():
  a = list(range(1,101))
  while True:
    random.shuffle(a)
    yield {index:i for index,i in enumerate(a,1)}
    

def search(target, boxes):
  checked = []
  ntarget = target
  for _ in range(50):
    opens = boxes[ntarget]
    if opens in checked:
      #print("Looped", i+1)
      return -1
    if opens == target:
      #print("FOUND", i+1)
      return 1
    #print(opens)
    checked.append(opens)
    ntarget = opens
  else:
    #print("Not found")
    return -1

def experiment(n):
  count = {"Succes":0, "Failed":0}
  for _ in range(n):
    boxes = make_boxes()
    for i in range(1,101):
      if search(i,boxes) != 1:
        #print("Failed")
        count["Failed"] += 1
        break
    else:
      #print("Succes")
      count["Succes"] += 1
  print(count)
  return count


def experiment2(n):
  count = {"Succes":0, "Failed":0}
  all_boxes = gen_boxes()
  for j in range(n):
    boxes = next(all_boxes)
    for i in range(1,101):
      if search(i,boxes) != 1:
        #print("Failed")
        count["Failed"] += 1
        break
    else:
      #print("Succes")
      count["Succes"] += 1
  print(count)
  return count
# experiment(10000)


repeats = 100000

count2, speed2 = speed(experiment2, repeats)
print()

count0, speed0 = speed(experiment, repeats)
print()

