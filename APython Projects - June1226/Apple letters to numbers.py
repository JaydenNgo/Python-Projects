word = input("Word ").lower()
a = [letter for letter in word]
b = []
c = []
print(a)

for i in a:
  if i in ('a','b','c'):
    b.append(2)
  elif i in ('d','e','f'):
    b.append(3)
  elif i in ('g','h','i'):
    b.append(4)
  elif i in ('j','k','l'):
    b.append(5)
  elif i in ('m','n','o'):
    b.append(6)
  elif i in ('p','q','r','s'):
    b.append(7)
  elif i in ('t','u','v'):
    b.append(8)
  elif i in ('w','x','y','z'):
    b.append(9)
    
print(b)

lib = {"abc": 2, "def": 3, "ghi": 4, "jkl": 5, 
       "mno": 6, "pqrs": 7, "tuv": 8, "wxyz": 9}

for i in a:
  for j in lib:
    if i in j:
      c.append(lib[j])
      break

print(c)