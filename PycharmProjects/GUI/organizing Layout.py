from tkinter import *

root=Tk()
tframe=Frame(root)
tframe.pack()

bframe=Frame(root)
bframe.pack(side=BOTTOM)

tlabel=Label(text="this will be on the top")
blabel=Label(bframe,text="this will be on the bottom")

button1=Button(tframe, text="Top Frame", fg="red")#fg=foreground colour
button2=Button(bframe, text="Bottom Frame", fg="green")

button1.pack()
button2.pack()

tlabel.pack()
blabel.pack()
root.mainloop()
