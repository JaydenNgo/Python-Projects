def permute(elements):
    if len(elements) == 0:
        yield []
    else:
        for i, x in enumerate(elements):
            remainder = elements[:i] + elements[i+1:]
            for p in permute(remainder):
                yield [x] + p



def find(search,elements):
  count = 0
  for j in permute(elements):
      for ind,num in enumerate(j):
        if j[ind:ind+len(search)] == search:
          count += 1
          break
  print(count)

find(([0,0,0,0,0,1,1,1,1]), [i for i in range(8)])