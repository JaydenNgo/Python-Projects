def miss(current, rate, times):
  for i in range(times):
    missing_hp = 100-current
    new_hp = current + (missing_hp*(rate/100))
    current = new_hp
  print(new_hp)
  return new_hp


for i in range(0,100,10):
  print('Sundered')
  miss(i,6,3)
  print('')
  print('Voli')
  miss(i,20,1)
  print('')
