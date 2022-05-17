import random

digit1 = random.randint(1,100)

digit2 = random.randint(1,100)

goodAwnser = digit1 + digit2

awnser = int(input(f"What is the sum of {digit1} + {digit2}? "))

if awnser == goodAwnser:
    print("You got the correct awnser!")

elif awnser != goodAwnser:
    print(f"The correct awnser for the following question was {goodAwnser}.")
