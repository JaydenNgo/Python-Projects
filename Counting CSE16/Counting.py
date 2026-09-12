def permute(elements):
    if len(elements) == 0:
        yield []
    else:
        for i, x in enumerate(elements):
            remainder = elements[:i] + elements[i+1:]
            for p in permute(remainder):
                yield [x] + p


count = 0
for i in permute([0,0,0,0,0,1,1,1,1]):
  count += 1

print(count)