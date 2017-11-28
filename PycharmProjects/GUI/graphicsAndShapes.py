from tkinter import *

root=Tk()

canvas= Canvas(root,width=400,height=300)
canvas.pack()

blackline=canvas.create_line(0,0,400,150,fill="green")#top left corner axis
redline=canvas.create_line(0,150,400,150,fill="red")
greeBox=canvas.create_rectangle(25,25,130,60,fill="blue")
canvas.delete(redline)
canvas.delete(ALL)

root.mainloop()