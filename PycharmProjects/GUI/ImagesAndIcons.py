from tkinter import *
from PIL import Image,ImageTk
root=Tk()

load=Image.open("C:\\Users\\VASUDEVA\\Desktop\\IMG_9620.JPG")
load.thumbnail((400,400))
photo=ImageTk.PhotoImage(load)


l=Label(root,image=photo)
l.pack()

root.mainloop()