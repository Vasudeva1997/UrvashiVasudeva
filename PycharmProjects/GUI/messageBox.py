from tkinter import *
import tkinter.messagebox
root=Tk()

answer=tkinter.messagebox.askquestion('WARNING','This filters needs you to select the other image.\nDo you want to continue??')

if answer == 'yes':
    print("Fuck with ur silly faces")
else:
    print("Fuck without a silly faces")
root.mainloop()