nimals = ["Bird", "Fox", "Cat", "Rat", "Alligator"]


animals.append("Giraffe")

moreAnimals = ["Monkey", "Ant Eater", "Red Panda"]

animals.extend(moreAnimals)

animals.insert(4, "Snake")

animals.pop(3)

animals.remove("Snake")

del animals[2]

del animals

#deletes entire list
#del animals

for counter in animals:
    print(counter)
    

    
    

