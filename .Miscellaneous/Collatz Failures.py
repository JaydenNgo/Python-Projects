import json
import statistics as stat
# fixed floating pint 13.0 issue

def hail(x):
  # print(x)
  local = {x}
  while x not in failed and x > minn:
    # if odd          if even
    x = int(3*x+1) if x%2 else int(x/2)
    # if infinite loop then solved!
    if x in local:
      return
    local.add(x)
  failed.update(local)
  # print(len(local))

file_name = "Collatz.json"

# Reset file
'''
with open(file_name, 'w') as file:
   file.write('')
'''

# If list exists, import it
try:
    with open(file_name, 'r') as file:
        loaded = json.load(file)
        failed = set(loaded[1])
        minn = loaded[0]
        
    print("List loaded")

# If DNE, start from scratch
except (FileNotFoundError, json.JSONDecodeError):
    failed = {1}
    minn = 0
    print("Starting from 1")



print("Lower bound is:", minn)
# Change in size
oglength = len(failed)

maxx = 5000000
for i in range(minn,maxx+1):
  hail(i)

print("done")
newlength = len(failed)
print(oglength, newlength)

# Your are guranteed to have discovered 0 - maxx
# So you check maxx - newlength for lower bound
for i in range(maxx,newlength):
   print(i)
   if i not in failed:
      minn = i-1
      print("New Lower bound is:", minn)
      break

# set lower bounds so we don't have to store that many numbers
# filter out all the numbers below the lower bound
failed = [x for x in failed if x > minn]
print("Length filtered", len(failed))
print("Largest value:", max(failed))
print("Spread: ", stat.stdev(failed))

if newlength != oglength:
    export = [minn, failed]
    with open(file_name, "w") as file:
        json.dump(export, file)
