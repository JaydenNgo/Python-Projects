import csv
import random

# To Do
# Split property into 3
# Need to test buying houses
# selling house
# hotels 
# mortgage
# trading?
# get out of jail free cards


#Converts numeric strings to numbers
def numerate(a):
  for i in range(len(a)):
    if a[i].isdigit():
      a[i] = int(a[i])
  return tuple(a)

# Returns result of 2 dice rolls
def dice_roll():
  return (random.randint(1,6),random.randint(1,6))

class Buyable:
  def __init__(self, name):
    self.name = name
    self.mortgage = self.price//2
    self.owner = None
    self.ismortgaged = False

  def isowned(self):
    return self.owner != None
  
class Property(Buyable):
  def __init__(self, name, color, rent, h1, h2, h3, h4, hotel, price, build_cost):
    self.color = color
    self.price = price
    self.rent = rent

    self.house_rent = [h1, h2, h3, h4]
    self.hotel = hotel
    self.build_cost = build_cost
    self.house_count = 0
    self.has_hotel = False
    super().__init__(name)
  

class Railroad(Buyable):
  def __init__(self, name):
    self.price = 200
    self.rent = 25
    super().__init__(name)

class Utility(Buyable):
  def __init__(self, name):
    self.price = 150
    self.rent = 0
    super().__init__(name)


community_chest = [
"Advance to 'Go'. (Collect $200)",
"Bank error in your favor. Collect $200",
"Doctor's fees. Pay $50",
"From sale of stock you get $50.",
"Get Out of Jail Free.",
"Go to Jail. Go directly to jail. Do not pass Go, Do not collect $200.",
"Grand Opera Night. Collect $50 from every player for opening night seats",
"Holiday Fund matures. Receive $100.", 
"Income tax refund. Collect $20.",
"It is your birthday. Collect $10 from every player.",
"Life insurance matures. Collect $100",
"Hospital Fees. Pay $50.",
"School fees. Pay $50.",
"Receive $25 consultancy fee.", 
"You are assessed for street repairs: Pay $40 per house and $115 per hotel you own.", 
"You have won second prize in a beauty contest. Collect $10.",
"You inherit $100.",
]
chances = [
"Advance to 'Go'. (Collect $200)",
"Advance to Illinois Avenue. If you pass Go, collect $200.",
"Advance to St. Charles Place. If you pass Go, collect $200.",
"Advance token to the nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 10 (ten) times the amount thrown.",
"Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rent to which they are otherwise entitled. If Railroad is unowned, you may buy it from the Bank. (There are 2 of these.)", 
"Bank pays you dividend of $50.",
"Get out of Jail Free. This card may be kept until needed, traded, or sold.",
"Go Back Three 3 Spaces.",
"Go to Jail. Go directly to Jail. Do not pass GO, do not collect $200.",
"Make general repairs on all your property: For each house pay $25, For each hotel $100.",
"Take a trip to Reading Railroad. If you pass Go, collect $200.",
"Advance to Boardwalk.",
"You have been elected Chairman of the Board. Pay each player $50.",
"Your building loan matures. Receive $150."
]


b = "\b\b\b\b"
def find_railroad(x):
  return int(10*((x/10+0.5)//1)+5) % 40

class Player:
  def __init__(self, name):
    self.name = name
    self.money = 1500
    self.property = {}
    self.railroad = {}
    self.utility =  {}
    self.sets = {i:0 for i in all_colors}
    self.num_raildraod = 0  #Change to len(railroad)?
    self.num_utility = 0
    self.pos = 0
    self.doubles = 0
    self.jailed = False
    self.total_num_houses = 0
    self.total_num_hotels = 0

  # Runs procedure for any community cheset card
  def draw_chest(self, name):
    print(f"{name}\n")
    if name == "Advance to 'Go'. (Collect $200)":
      self.pos = 0
      self.money += 200
      print(f"{self.name} Earned $200, now has ${self.money}")
    elif name == "Bank error in your favor. Collect $200":
      self.money += 200
      print(f"{self.name} now has ${self.money}")
    elif name in ("Doctor's fees. Pay $50", "Hospital Fees. Pay $50.", "School fees. Pay $50."):
      self.money -= 50
      print(f"{self.name} now has ${self.money}")
    elif name == "From sale of stock you get $50.":
      self.money += 50
      print(f"{self.name} now has ${self.money}")
    elif name == "Get Out of Jail Free.":
      pass
      #print(f"{self.name} now has ${self.money}")
    elif name == "Go to Jail. Go directly to jail. Do not pass Go, Do not collect $200.":
      self.pos = 10
      self.jailed = True
      print(f"{self.name} was sent to Jail =(")
    elif name == "Grand Opera Night. Collect $50 from every player for opening night seats":  #might need edit
      for name,obj in players.items():
        if obj != self:
          obj.money -= 50
      self.money += 50*(len(players)-1)
      print(f"{self.name} now has ${self.money}")
    elif name == "Holiday Fund matures. Receive $100." or name == "You inherit $100.":
      self.money += 100
      print(f"{self.name} now has ${self.money}")
    elif name == "Income tax refund. Collect $20.":
      self.money += 20
      print(f"{self.name} now has ${self.money}")
    elif name == "It is your birthday. Collect $10 from every player.":
      for name,obj in players.items():
        if obj != self:
          obj.money -= 10
      self.money += 10*(len(players)-1)
      print(f"{self.name} now has ${self.money}")
    elif name == "Life insurance matures. Collect $100":
      self.money += 100
      print(f"{self.name} now has ${self.money}")
    elif name == "Receive $25 consultancy fee.":
      self.money -= 25
      print(f"{self.name} now has ${self.money}")
    elif name == "You are assessed for street repairs: Pay $40 per house and $115 per hotel you own.":
      self.money -= self.total_num_houses * 40
      self.money -= self.total_num_hotels * 115
      print(f"{self.name} now has ${self.money}")
    elif name == "You have won second prize in a beauty contest. Collect $10.":
      self.money += 10
      print(f"{self.name} now has ${self.money}")
    else:
      print("Wtf did you draw",name)
  
  # Runs procedure for any chance card
  def draw_chance(self, name):
    print(f"{name}\n")
    if name == "Advance to 'Go'. (Collect $200)":
      self.pos = 0
      self.money += 200
      print(f"{self.name} Earned $200, now has ${self.money}")
    elif name == "Advance to Illinois Avenue. If you pass Go, collect $200.":
      if self.pos > 24:
        self.money += 200
        print(f"{self.name} Earned $200, now has ${self.money}")
      self.pos = 24
      self.landed()

      self.money += 200
      print(f"{self.name} now has ${self.money}")
    elif name == "Advance to St. Charles Place. If you pass Go, collect $200.":
      if self.pos > 11:
        self.money += 200
        print(f"{self.name} Earned $200, now has ${self.money}")
      self.pos = 11
      self.landed()
    elif name == "Advance token to the nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 10 (ten) times the amount thrown.":
      if (12 < self.pos < 28):
        self.pos = 28
      else:
        self.money += 200
        print(f"{self.name} Earned $200, now has ${self.money}")
        self.pos = 12

      print(f"{self.name} landed on {Board[self.pos]}")
      self.landed()
    elif name == "Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rent to which they are otherwise entitled. If Railroad is unowned, you may buy it from the Bank. (There are 2 of these.)":
      if self.pos > 35:
        self.money += 200
        print(f"{self.name} Earned $200, now has ${self.money}")
      self.pos = find_railroad(self.pos)
      print(f"{self.name} landed on {Board[self.pos]}")
      self.landed()
    elif name == "Bank pays you dividend of $50.":
      self.money += 50
      print(f"{self.name} now has ${self.money}")
    elif name == "Get out of Jail Free. This card may be kept until needed, traded, or sold.":
      pass
      #print(f"{self.name} now has ${self.money}")
    elif name == "Go to Jail. Go directly to Jail. Do not pass GO, do not collect $200.":
      self.pos = 10
      self.jailed = True
      print(f"{self.name} was sent to Jail =(")
    elif name == "Go Back Three 3 Spaces.":
      self.pos -= 3
      self.landed() 
    elif name == "Make general repairs on all your property: For each house pay $25, For each hotel $100.":
      self.money -= self.total_num_houses * 25
      self.money -= self.total_num_hotels * 100
      print(f"{self.name} now has ${self.money}")
    elif name == "Take a trip to Reading Railroad. If you pass Go, collect $200.":
      if self.pos > 5:
        self.money += 200
        print(f"{self.name} Earned $200, now has ${self.money}")
      self.pos = 5
      self.landed()
    elif name == "Advance to Boardwalk.":
      self.pos = 39
      self.landed()
    elif name == "You have been elected Chairman of the Board. Pay each player $50.":
      for name, obj in players.items():
        if obj != self:
          obj.money += 50
      self.money -= (len(players)-1) * 50
    elif name == "Your building loan matures. Receive $150.":
      self.money += 150
      print(f"{self.name} now has ${self.money}")
    else:
      print("Wtf did you draw")

  # Prints players current stats like Money, Position, and Jail status
  def printstats(self):
    print(f"""
    {b}{self.name} information:
    {b}Money: {self.money}
    {b}Position: {Board[self.pos]}
    {b}#Property owned: {len(self.property)}
    {b}In jail: {self.jailed}\n""") 
  
  # Prints all properties you own, in board order
  # ADD IF MORTGAGED
  def printproperties(self):
    print(f"{self.name} owns:")
    for name in properties:
      if name in self.property:
        obj = self.property[name]
        print(f"{name+":":22} {obj.color:10}  {obj.house_count} houses")
    print()
    for name in railroads:
      if name in self.railroad:
        obj = self.railroad[name]
        print(f"{name}")
    print()
    for name in utilities:
      if name in self.utility:
        obj = self.utility[name]
        print(f"{name}")
    print()
  
  # Returns Whether you've completed the set of a given color
  def completed(self,color):
    return (color in ("Brown", "Dark Blue") and self.sets[color] == 2) or self.sets[color] == 3
  
  # Prints all colors and whether or not you have a complete set
  # Returns dictionary key: completed color, value: list of each prop in that color
  def full_sets_owned(self):
    print(f"{self.name}'s completed sets:")
    owned = {}
    for colors in all_colors:
      print(f"{colors:12} {self.completed(colors)}")
      if self.completed(colors):
        owned[colors] = [prop for prop in properties.values() if prop.color == colors]
    print()
    return owned

  def buy_house(self):
    full_sets = self.full_sets_owned()
    if len(full_sets) <= 0:
      print(f"{self.name} doesn't have any full sets\n")
      return
    choices = {}
    count = 1
    for color, set in full_sets.items():
      need_housing = min([prop.house_count for prop in set])
      print(color)
      for prop in set:
        if (prop.house_count == need_housing) and prop.house_count < 4:
          print(f"\t{count}.{prop.name+":":25} {prop.house_count}: ${prop.build_cost}")
          choices[count] = prop
          count += 1
    print()
    if len(choices) <= 0:
      print("There are no more places to buy houses")
      return

    print("Which property would you like to buy a house for?\n")
    for ind,prop in choices.items():
      print(ind,prop.name)
    # maybe add opt-out if they say yes but don't want to
    while True:
      pick = input("\nEnter: ")
      if pick == "exit":
        return
      if not pick.isdigit():
        print("Please enter a number")
        continue
      if not (1 <= int(pick) <= 5):
        print("Not in range")
        continue
      else:
        pick = int(pick)
        break
    prop: Property = choices[pick]
    prop.house_count += 1
    self.total_num_houses += 1
    prop.rent = prop.house_rent[prop.house_count-1]
    self.money -= prop.build_cost
    self.buy_house()
    '''
    again = input("Would you like to buy more? (y|n) ").lower()
    if again in ("y", "yes"):
      self.buy_house()
    else:
      return
    '''

  def sell_house(self):
    print("SELLING HOUSE")
    if self.total_num_houses <= 0:
      print(f"{self.name} you don't own any houses")
      return
    count = 1
    choices = {}
    for name,prop in self.property.items():
      prop: Property = prop
      if prop.house_count > 0:
        print(f"{count} {name+":":23} {prop.house_count}: ${prop.build_cost//2}")
        choices[count] = prop
        count += 1
    print(f"Which house would you like to sell?")
    print("\n")


  # Runs the code to give a player a deed
  # Input: Deed: Property object, Buyable: dictionary it belongs to
  # Returns: None
  def buy_property(self, deed, buyables):
    
    if not isinstance(deed, Buyable):
      print(f"{deed} is not a buyable")
      return
    if buyables not in (properties, railroads, utilities):
      print("Wtf is this thing")
      return
    self.money -= deed.price
    deed.owner = self.name

    if buyables == railroads:
      self.railroad[deed.name] = deed
      self.num_raildraod += 1
      deed.rent = 25*(2**(self.num_raildraod-1))
      print(f"{self.name} now owns {self.num_raildraod} railraods")

    if buyables == utilities:
      self.utility[deed.name] = deed
      self.num_utility += 1
      print(f"{self.name} now owns {self.num_utility} utilities")

    if buyables == properties:
      self.property[deed.name] = deed
      color = deed.color
      self.sets[color] += 1
      print(f"{self.name} has {self.sets[color]} of the {color} set")
      if self.completed(color):
        print(f"{self.name} has completed the {color} set!")
        #Double all of the rents
        for obj in self.property.values():
          if obj.color == color:
            obj.rent *= 2

  '''
  def mortgage_it(self, deed):
    if isinstance(deed, Property):
      if deed.house_count or deed.has_hotel:
        print(f"{deed.name} has house(s)/hotel on it, please sell them first before taking a mortgage")
        return
    if deed.name not in self.property:
      print(f"{self.name} doesn't own {deed.name}")
      return
    deed.ismortgaged = True
    self.money += deed.mortgage
    
  def unmortgage_it(self, deed):
    if deed.ismortgaged == True:
      print(f"{deed.name} is not mortgaged")
      return
    if deed.mortgage * 1.1 > self.money:
      print(f"You can't afford to unmortgage {deed.name}")
      return
    deed.ismortgaged = False
    self.money -= deed.mortgage * 1.1
  '''
  # Runs code when a player lands on a tile
  # Can accept die if need for calculation
  def landed(self, dice1 = None, dice2 = None):
    landed_tile = Board[self.pos]
    print(f"{self.pos}, {self.name} landed on {landed_tile}")

    if landed_tile == "Go To Jail":
      self.pos = 10
      self.jailed = True
      print(f"{self.name} was sent to Jail =(")
      return
    
    if landed_tile == "Free Parking" or landed_tile == "Jail":
      pass
      
    if landed_tile == "Income Tax":
      self.money -= 200
      print(f"{self.name} payed the tax: {self.money}")

    if landed_tile == "Luxury Tax":
      self.money -= 100
      print(f"{self.name} payed the tax: {self.money}")

    if landed_tile == "Community Chest":
      card = community_chest.pop(0)
      self.draw_chest(card)
      community_chest.append(card)
    
    if landed_tile == "Chance":
      card = chances.pop(0)
      self.draw_chance(card)
      chances.append(card)
    
    # Checks each dictionary with stored objects
    for buyables in (properties, railroads, utilities):
      if landed_tile in buyables:
        deed = buyables[landed_tile]  # Retrieves the object
        
        if deed.isowned(): #owned pay rent
          p2 = players[deed.owner]
          if self == p2:
            print(f"{self.name} owns {deed.name}")
            break
          print(f"{deed.name} is owned by {deed.owner}")
          if deed.ismortgaged:
            print("This property is currently mortgaged, rent can't be collected")
            break

          if buyables == utilities:
            if dice1 == None:
              dice1,dice2 = dice_roll()
            deed.rent = (6*p2.num_utility-2)*(dice1+dice2)

          print(f"Rent costs ${deed.rent}")
          print(f"{self.name}: {self.money}, {p2.name}: {p2.money}")
          self.money -= deed.rent
          p2.money += deed.rent
          print(f"{self.name}: {self.money}, {p2.name}: {p2.money}")
        
        else: #Unowned
          print(f"{deed.name} is not owned and costs ${deed.price}")
          # Add check if you have enough money
          # prompt = input(f"Would you like to buy {deed.name}? (Y/N) ").upper()
          prompt = "Y"
          if prompt in ("Y","YES"):
            if self.money < deed.price:
              print(f"You don't have enough money! ${self.money}")
              break
            #give the deed to the player
            self.buy_property(deed, buyables)
            
          else: # Auction
            #break
            print(f"\n{deed.name} is up for Auction!")
            auction_price = 10
            auctioner = None
            while True:
              passes = 0
              in_auction = [player for player in players.values() if player.money >= auction_price]
              for player in in_auction:
                if auctioner != None:
                  if player.name == auctioner.name:
                    passes += 1
                    continue
                print(f"Current Price is {auction_price} by {"the Bank" if not auctioner else auctioner.name}\n")
                prompt = input(f"{player.name}, Would you like to raise or pass? ").lower()
                if prompt in ("raise","y"):
                  while True:
                    new_price = int(input(f"New price? "))
                    if new_price <= auction_price:
                      print(f"Price needs to be higher than {auction_price}")
                      continue
                    break
                  auction_price = new_price
                  auctioner = player
                  break
                else:
                  passes += 1

              if passes == len(players):    # If everyone passes, end the auction
                break
              
            if auctioner != None:
              print(f"{auctioner.name} has won the auction at {auction_price}")
              deed.price = auction_price
              self.buy_property(deed, buyables)
            else:
              print(f"No one bought the {deed.name}, back to the bank!")
        break
    else:
      print("Not buyable")

    if (dice1 == dice2):
      print(f"{self.name} rolled doubes, they go again\n")
      self.roll()

  # Rolls 2 die and move the player
  # Checks for speeding and passing go
  # Runs landed() at the end
  def roll(self, dice1 = None, dice2 = None):
    dice1,dice2 = dice_roll()
    print(f"Dice: {dice1,dice2} = {dice1+dice2}")
    
    #Check if doubles and speeding
    if (dice1 == dice2):
      self.doubles += 1
      if self.doubles == 3:
        self.pos = 10
        self.jailed = True
        print(f"{self.name} was caught speeding and sent to Jail =(")
        return
    else:
      self.doubles = 0
      
    self.pos += dice1 + dice2
    # If passed GO
    if (self.pos >= 40):
      self.pos %= 40
      self.money += 200
      print(f"{self.name} Earned $200, now has ${self.money}")

    # Run landed code
    self.landed(dice1, dice2)

  # Needs work
  # Checks jail coniditoino and (Other prompts, buying houses)
  def start_turn(self):
    if self.jailed is True:
      print(f"{self.name} is currently in Jail")
      choice = "pay"
      # Roll dobules
      if choice == "roll":
        first,second = dice_roll()
        print(f"Rolled: {first},{second}")
        if first == second:
          print(f"{self.name} rolled doubles! They are free from jail!")
          self.jailed = False
          self.roll(first,second)
      # Pay 50 bail
      elif choice == "pay":
        self.money -= 50
        self.jailed = False
        print(f"{self.name} payed bail: {self.money}")
      # Use card
    else:
      self.roll()
#-----------------------------------------------------------------------------------------------
Board = ['GO', 'Mediterranean Avenue', 'Community Chest', 'Baltic Avenue', 'Income Tax', 
         'Reading Railroad', 'Oriental Avenue', 'Chance', 'Vermont Avenue', 'Connecticut Avenue', 
         'Jail', 'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenue', 
         'Pennsylvania Railroad', 'St. James Place', 'Community Chest', 'Tennessee Avenue', 
         'New York Avenue', 'Free Parking', 'Kentucky Avenue', 'Chance', 'Indiana Avenue', 
         'Illinois Avenue', 'B. & O. Railroad', 'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 
         'Marvin Gardens', 'Go To Jail', 'Pacific Avenue', 'North Carolina Avenue', 'Community Chest', 
         'Pennsylvania Avenue', 'Short Line', 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk']

# Extracts all of the property data
# Key: Property Name
# Value: Property Object
with open('Property.csv', mode='r') as file:
  reader = csv.reader(file)
  properties = {row[0]:Property(*numerate(row)) for row in reader}

railroad_names = ["Reading Railroad", "Pennsylvania Railroad", "B. & O. Railroad", "Short Line"]
railroads = {i: Railroad(i) for i in railroad_names}
utility_names = ["Electric Company", "Water Works"]
utilities = {i: Utility(i) for i in utility_names}

all_colors = []
for i in properties:
  if properties[i].color not in all_colors:
    all_colors.append(properties[i].color)

random.shuffle(community_chest)
random.shuffle(chances)

#-----------------------------------------------------------------------------------------------
players = {}
def addplayer(name):
  a = Player(name)
  players[name] = a

addplayer("Jay")
addplayer("Diana")
for k,v in players.items():
  print(k,v)
print()

p1: Player = players["Jay"]
p2: Player = players["Diana"]


for i in range(1,200+1):
  print(f"Round {i} {'-'*35}")
  p1.start_turn()
  print()
  p2.start_turn()
  print()
'''
while (p1.money > 0 and p2.money > 0):
  print(f"Round {i} {'-'*35}")
  p1.start_turn()
  print()
  p2.start_turn()
  print()
'''

p1.buy_house()
p1.sell_house()
p2.buy_house()
print("\n\n")
p1.printstats()
p1.printproperties()
p2.printstats()
p2.printproperties()
print("\n\n")

print("DONE")
'''
for p in properties:
   print(p.name)'''