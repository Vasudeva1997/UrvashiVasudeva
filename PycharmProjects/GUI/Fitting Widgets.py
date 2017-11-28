from tkinter import *;

root=Tk()

l1=Label(root,text="One",bg="red",fg="white")#fg= foreground bg=backgroung
l1.pack()
two=Label(root,text="Two",bg="green",fg="black")
two.pack(fill=X)# this will fill the X axis
three=Label(root,text="Three",bg="blue",fg="white")
three.pack(fill=Y,side=LEFT)# this will fill the Y axis and wil be on the left

root.mainloop()


