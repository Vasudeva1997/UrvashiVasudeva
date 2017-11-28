from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk()

fileName = askopenfilename (filetypes = (("VASU","*.vc"),("All Files","*.*")),initialdir="C:\\",title="YOYO")
print(fileName)
root.mainloop()