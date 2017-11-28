from tkinter import *;

root=Tk()

l1=Label(root,text="Name",bg="red",fg="white")
l1.grid(row=0,sticky=E)# Sticky is usedfor alignment E stands for east. N for north, W= West, S= South
two=Label(root,text="Password",bg="green",fg="black")
two.grid(row=1,sticky=E)

entry1=Entry(root)
entry2=Entry(root)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

c= Checkbutton(root,text="Keep me logged IN")
c.grid(columnspan=2)#we need this to take up the 2 coloumns we write columnspan ove here
c.select()
c.deselect()

root.mainloop()