import math

a = int(input("What is the length of triangle leg (a)?: "))

b = int(input("What is the length of triangle leg (b)?: "))

u = input("What unit are you measuring in?: ")

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"The lenght of the hypotenuse is {c} {u}")