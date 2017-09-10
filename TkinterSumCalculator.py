# Create a sum calculator using Tkinter with Derek Banas.

from tkinter import *
from tkinter import ttk
# How events work with Tkinter

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())

    sum = num1 + num2
    ## The sumEntry.delete will erase the last result
    sumEntry.delete(0,"end")
    
    sumEntry.insert(0, sum)


root = Tk()
# Keeping it simple using .pack for this example
num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

# The .bind the left mouse button (<Button-1>) when ever is clicked
# The get_sum will find the function that is going to be executed with
#    the click of the mouse left button.
equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()
