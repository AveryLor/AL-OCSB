'''

print("avery")
print("ahsan")

'''


"""
Line of block 1
Line of block 2
Line of block 3
"""


"""
A condition is a comparison.
Conditions evaluate a boolean value to be true or false.
If a condition is true, the following block of code will run.
A block  of code will be indented. 
"""


"""
Compairisons

> Greater than 
< Less than
>= Greater than or equal
<= Less than or equal 
== Equal to 
!= Not equal to 

"""
while True:
    mark = int(input("Please enter your mark:"))
    if mark >= 90:
        print("You aced it")
    elif mark >= 70:
        print("That's a B")
    elif mark >= 60:
        print("That's a C")
    elif mark >= 50:
        print("You barely made it")
    
    
    else:
        print("You failed")
        
        
    if (mark >= 0 and mark <= 100):
        print("You have a valid mark")
        
    if (mark > 100 or mark < 0):
        print("This is an invalid mark")
        
        