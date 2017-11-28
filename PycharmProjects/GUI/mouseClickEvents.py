from tkinter import *

root=Tk()

def lc(event):
    print("Left Click")


def rc(event):
    print("right Click")


def mc(event):
    print("middle Click")

l=Label(root,text="Text appears on the console")
frame=Frame(root,width=400,height=400)
frame.bind("<Button-1>",lc)#left click
frame.bind("<Button-2>",mc)#scroll button
frame.bind("<Button-3>",rc)#right click
frame.grid(row=1)
l.grid(sticky=W,row=0,column=0)

root.mainloop()

