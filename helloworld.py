from tkinter import *

root = Tk()

myLabel = Label(root, text = "EEEEE")

myButton = Button(root, text = "Ahsan is bad") 

def myClick():
    myE = Label(root, text = "Yes he is", fg = "red")
    myE.pack()
    
    
    
myLabel.pack()
myButton.pack()

root.mainloop() 