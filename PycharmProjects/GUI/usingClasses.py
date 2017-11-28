from tkinter import *

class buttons:

    def __init__(self,master):# passing the object of the other class
        frame=Frame(master)
        frame.pack()

        self.b=Button(frame,text="Print messages",command=self.printmessage)
        self.b.pack(side=LEFT)

        self.q=Button(frame,text="Quit",command=frame.quit)
        self.q.pack()

    def printmessage(self):
        print("HI")


root=Tk()
b=buttons(root)
root.mainloop()