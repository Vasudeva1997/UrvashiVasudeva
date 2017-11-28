from tkinter import *
 # *********Menu*************
def doNothing():
    print("ok ok I wont.......")
root=Tk()

menu= Menu(root)
root.config(menu=menu)

subMenu =Menu(menu)
menu.add_cascade(label="file",menu=subMenu)
subMenu.add_command(label="Now Project.....",command=doNothing)
subMenu.add_command(label="Now Project",command=doNothing)
subMenu.add_command(label="Now",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=doNothing)

editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)
save=Menu(editMenu)
editMenu.add_separator()
editMenu.add_cascade(label="Save",menu=save)

#***********toolbar************

tb= Frame(root,bg="blue")
insertButt=Button(tb,text="Insert the image",command=doNothing)
insertButt.pack(side=LEFT, padx=2,pady=2)
printButt=Button(tb,text="Print the image",command=doNothing)
printButt.pack(side=LEFT, padx=2,pady=2)

tb.pack(side=TOP,fill=X)

#***********Status bar************

status=Label(root,text="Preparing to do nothing",bd=1, relief=SUNKEN,anchor=W)#bd=border
status.pack(side=BOTTOM,fill=X)

root.mainloop()