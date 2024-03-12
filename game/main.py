import random


class city():
    def __init__(self, pop, police, entropy, inventory):
        self.pop = pop
        self.police = police
        # Police
        self.entropy = entropy
        # population impacts price, police impacts police, entropy impacts random encounters.
        self.inventory = inventory

    def buy(self, item):
        self.item = item

    def sell(self, item):
        self.item = item
    def storegenerate(self):
        if self in citylist:
            print(self)
            # print("success")
            # print(self.pop, self.police, self.entropy)
            ## the 2 preceding lines are for testing for each city
            iter = self.pop
            while iter > 0:
              for object in self.inventory:
                object = random.randbytes(1)
                if object == 1:
                    iter -= 1
                #append inventory with 1 or 0 for inventory. 101 equals true false true
            
        else:
            print(self)
            print("failure")

bug = city(pop=3,police=0, entropy=1, inventory=(0,0,0))
bug2 = city(pop=5,police=.3, entropy=.6, inventory=(0,0,0))
citylist = [bug, bug2]
prompt = input("city name:\n")
if prompt == "bug":
    storegen = bug
elif prompt ==  "bug2":
    storegen = bug2
else:
    storegen = f'invalid city name "{prompt}"'
bug2.storegenerate()
print(bug2.inventory)
#fix to return actual data instead of memory address. Issue with my 

class stuff():
    def __init__(self, id, name, price, rarity, variance):
        self.id = id
        self.name = name
        self.price = price
        self.rarity = rarity
        self.variance = variance