import math
# returns largest n byte number
def max_num(n):
  return 2**(8*n)-1
  
def int_requried(n):
  return math.ceil(math.log2(n+1)/8)
  
  
numbers = [i for i in range(100000)]
# length: how many bytes (2 can hold up to 65,535)
# byteorder: 'big' or 'little' (stay consistent!)


byte = 1
largest = max_num(byte)
breakpoints = []

b = 0 # Counts # of numbers of current byte size
print(largest)
with open('simple.bin', 'wb') as f:
    f.write(b"\n")
    for n in numbers:
      # Increase byte size
      if n > largest:
        byte += 1
        largest = max_num(byte)
        breakpoints.append(b)
        b = 0
      f.write(n.to_bytes(byte, byteorder='big'))
      #print(n,byte)
      b += 1
    breakpoints.append(b)
      

''' '''
decoded = []
print(breakpoints)
c = 0
read_byte = 1
with open('simple.bin', 'rb') as f:
    # Read 2 bytes at a time until the end of the file
    a = f.readline()
    for i in breakpoints:
        for j in range(i):
            chunk = f.read(read_byte)
            num = int.from_bytes(chunk, byteorder='big')
            #print(num)
            decoded.append(num)
            c += 1
        print(read_byte)
        read_byte += 1
        



for i in decoded:
   print(i)
   pass