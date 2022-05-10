newItem = 0

for i in range(10):
    item = int(input("Enter the cost of the item here: "))
    newItem += item

print(f"Cost of all items without tax: {newItem}")

print(f"Cost of taxes: {newItem * 0.13}")

print(f"Totat cost|Price of items with tax: {newItem * 1.13}")