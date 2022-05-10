newNum = 0
numLst = []
for i in range(5):
    num = int(input("Insert number here: "))
    numLst.append(num)
    newNum += num

num1 = int(numLst[0])
num2 = int(numLst[1])
num3 = int(numLst[2])
num4 = int(numLst[3])
num5 = int(numLst[4])


print(f"The first number is: {num1}")

print(f"The second number is: {num2}")

print(f"The third number is: {num3}")

print(f"The fourth number is: {num4}")

print(f"The fifth number is: {num5}")

sum = num1 + num2 + num3 + num4 + num5

print(f"The sum of the numbers is: {sum}")

print(f"The average of these numbers is: {int(sum/5)}")
