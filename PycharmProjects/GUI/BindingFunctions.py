
from tkinter import *

root=Tk()

def printName(event):
    print("Hi, My name is Vasudeva")


button = Button(root,text="Click me")# we can keep command=function_name to invoke the function also
button.bind("<Button-1>",printName)# here Button 1 indicates the leftclick.Note the function name houldn't contain the paranthesis
button.pack()


root.mainloop()