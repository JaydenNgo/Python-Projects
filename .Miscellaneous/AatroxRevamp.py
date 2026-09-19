import random

#Aatrox health = x
#Player health = y

e_hp = 50
p_hp = 100
z = 0

def print_health():
  print()
  print("Aatrox Health: ", str(int(e_hp)))
  print("Player Health: ", str(int(p_hp)))
  print()

#Aatrox Action = BA 
#1 = Aatrox
#Aatrox moves

while e_hp > 0 and p_hp > 0:
  Aatroxaction = random.randint(0,1)
  BA = "attack"
  if Aatroxaction == 1:
    BA = "heal"

#Player input

  #action = str.lower(input("What will you do? attack, heal, or block: "))
  action = 'a'
  print('-'*50)
  print()
  options = ('a', 'h', 'b', 'attack', 'heal', 'block')
  if action not in options:
    print("Invalid Move")
    print()
  action = action[0]
  attack = random.randint(15,30)
    
    
#if Aatrox attacks
  if BA in ("attack","heal"):
    e_attack = random.randint(10+(z*5),30+(z*5))

    if BA == "attack" and action == "block":
      print("Aatrox attacked you but you blocked the attack")
    if BA == "attack" and action != "block":
      p_hp -= e_attack
      e_hp += e_attack//4
      print(f"Aatrox attacked you for {e_attack} damage and healed for {(e_attack//4)}!")

    if BA == "heal":
      if action == "block":
        print("You blocked nothing")
      e_heal = e_attack*(1+(z*0.5))//1
      e_hp += e_heal
      print(f"Aatrox healed for {e_heal} health!")

    if action == "a":
      e_hp -= attack
      print(f"You attacked for {attack} damage!" )
    
    if action == "h":
      p_hp += attack
      print(f"You healed for {attack} health!")

    print_health()

  '''
  #if Aatrox blocks
    
    if BA == "block":
      if action == "a":
        p_hp -= attack//2+1
        e_hp -= attack//2-1
        print("Aatrox reflected some of the attack")
      
      if action == "h":
        p_hp += attack
        print(f"You healed for {attack} health!")
        print()
        print("Aatrox didn't block anything")

      if action == "b":
        print("Quit standing there fight!")
        print()

      print_health()
  '''    
  #Evolve

  if e_hp <= 20 and z == 0:
    z += 1
    e_hp += 30
    print("Aatrox has awakened the Darkin and is now Aatrox the World Ender!")
    print_health()
    
  if e_hp <= 10 and z == 1:
    z += 1
    e_hp += 50
    print("Aatrox has unleashed the fury within and is now Aatrox the Darkin Godslayer!!!")
    print_health()

#Outcome

if p_hp <= 0:
  print("You Lose!")

if e_hp <= 0:
  print("You Win!")





