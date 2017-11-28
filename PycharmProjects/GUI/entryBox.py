
from tkinter import *;

root=Tk()
l1=Label(root,text="One",bg="red",fg="white")#fg= foreground bg=backgroung
l1.place(x=0,y=0)
e=Entry(root)
e.place(x = 50, y=0 , width="200",height ="20")
print(e.get())
root.mainloop()