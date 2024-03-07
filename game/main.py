import random


class city():
    def __init__(self, pop, police, entropy):
        self.pop = pop
        self.police = police
        # Police
        self.entropy = entropy
        # population impacts price, police impacts police, entropy impacts random encounters.

    def buy(self, item):
        self.item = item

    def sell(self, item):
        self.item = item
    def store(self, inventory):
        self.inventory = inventory
        print("NOT FINISHED")
    def storegenerate(self):
        if self in citylist:
            print(self)
            # print("success")
            # print(self.pop, self.police, self.entropy)
            ## the former 2 lines are for testing
            self.store.inventory = ""
            iter = self.pop
            while iter > 0:
                self.store.inventory = self.store.inventory.append(random.getrandbits(1))
                iter -= 1
                #append inventory with 1 or 0 for inventory. 101 equals true false true
        else:
            print(self)
            print("failure")

bug = city(pop=3,police=0, entropy=1)
bug2 = city(pop=5,police=.3, entropy=.6)
citylist = [bug, bug2]
print()
prompt = input("city name\n")
if prompt == "bug":
    storegen = bug
elif prompt ==  "bug2":
    storegen = bug2
else:
    storegen = f'invalid city name "{prompt}"'
city.storegenerate(storegen)
print(city.store.inventory)

class stuff():
    def __init__(self, id, name, price, rarity, variance):
        self.id = id
        self.name = name
        self.price = price
        self.rarity = rarity
        self.variance = variance