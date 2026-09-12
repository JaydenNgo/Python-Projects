def prime():
  primes = [2]
  yield 2
  num = 3
  while True:
    for prime in primes:
      # Not prime
      if num//prime == num/prime:
        num += 1
        break
    else:
      primes.append(num)
      yield num
      num += 1


num_per_file = 10000
num_file = 1
max_num = num_per_file*num_file
filenum = 0
file = open(f"primedata{filenum}.txt","w")

for (index, val) in enumerate(prime()):
  curr_filenum = index//num_per_file
  # If passed threshhold, close file and break loop
  if index > max_num-1:
    file.close()
    break
  # Change file
  if curr_filenum > filenum:
    filenum += 1
    file.close()
    file = open(f"primedata{filenum}.txt","w")
  
  #file.write(f"{val},{index+1}\n")
  file.write(f"{index+1},{val}\n")
