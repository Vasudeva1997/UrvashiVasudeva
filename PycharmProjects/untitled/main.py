from tkinter import *
from PIL import Image,ImageTk,ImageChops,ImageEnhance,ImageFilter
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
filename=""
i=0
def save(img):
    global i
    i=i+1
    str = "ImageFilters"+i.__str__()+".jpg"
    img.save(str,"PNG")
    tkinter.messagebox._show('SAVED SUCCESSFULLY','Your image( '+str+' ) has been save succesfully\nThank You.')

def filter1(filename,root3):
    root3.destroy()
    root4 = Tk()
    img = Image.open(filename)
    img.thumbnail((700, 700))
    r, g, b = img.split()
    img = Image.merge("RGB", (r, b, b))
    photo = ImageTk.PhotoImage(img)
    label4 = Label(root4, image=photo)
    label4.pack()
    b1 = Button(text="    BACK    ", command=lambda: openfilters(filename, root4))
    b1.place(x=15, y=440)
    b2 = Button(text="    SAVE    ",command = lambda : save(img))
    b2.place(x=90, y=440)
    root4.mainloop()

def filter2(filename,root3):
    root3.destroy()
    root4 = Tk()
    img = Image.open(filename)
    img.thumbnail((700, 700))
    r, g, b = img.split()
    img = r
    photo = ImageTk.PhotoImage(img)
    label4 = Label(root4, image=photo)
    label4.pack()
    b1 = Button(text="    BACK    ", command=lambda: openfilters(filename, root4))
    b1.place(x=15, y=440)
    b2 = Button(text="    SAVE    ",command = lambda : save(img))
    b2.place(x=90, y=440)
    root4.mainloop()

def filter3(filename,root3):

    answer = tkinter.messagebox.askquestion('WARNING',
                                            'This filters needs you to select the other image.\nDo you want to continue??')
    if answer == 'yes':
        root3.destroy()
        root4 = Tk()
        img = Image.open(filename)
        filename2 = askopenfilename(filetypes=(("Images", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")),
                                    initialdir="Desktop", title="Select File")
        img2 = Image.open(filename2)
        r ,g , b = img.split()
        r2, g2, b2 = img2.split()
        img = Image.merge("RGB",(r2,b,g2))
        img.thumbnail((700, 700))
        photo = ImageTk.PhotoImage(img)
        label4 = Label(root4, image=photo)
        label4.pack()
        b1 = Button(text="    BACK    ", command=lambda: openfilters(filename, root4))
        b1.place(x=15, y=440)
        b2 = Button(text="    SAVE    ", command=lambda: save(img))
        b2.place(x=90, y=440)
        root4.mainloop()


def filter4(filename,root3):

    answer = tkinter.messagebox.askquestion('WARNING',
                                            'This filters needs you to select the other image.\nDo you want to continue??')
    if answer == 'yes':
        root3.destroy()
        root4 = Tk()
        img = Image.open(filename)
        filename2 = askopenfilename(filetypes=(("Images", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")),
                                    initialdir="Desktop", title="Select File")
        img2 = Image.open(filename2)
        img = ImageChops.multiply(img2, img)
        img.thumbnail((700, 700))
        photo = ImageTk.PhotoImage(img)
        label4 = Label(root4, image=photo)
        label4.pack()
        b1 = Button(text="    BACK    ", command=lambda: openfilters(filename, root4))
        b1.place(x=15, y=440)
        b2 = Button(text="    SAVE    ", command=lambda: save(img))
        b2.place(x=90, y=440)
        root4.mainloop()

def filter5(filename,root3):

    answer = tkinter.messagebox.askquestion('WARNING',
                                            'This filters needs you to select the other image.\nDo you want to continue??')
    if answer == 'yes':
        root3.destroy()
        root4 = Tk()
        img = Image.open(filename)
        filename2 = askopenfilename(filetypes=(("Images", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")),
                                    initialdir="Desktop", title="Select File")
        img2 = Image.open(filename2)
        img = ImageChops.add(img, img2, 2, 2)
        img.thumbnail((700, 700))
        photo = ImageTk.PhotoImage(img)
        label4 = Label(root4, image=photo)
        label4.pack()
        b1 = Button(text="    BACK    ", command=lambda: openfilters(filename, root4))
        b1.place(x=15, y=440)
        b2 = Button(text="    SAVE    ", command=lambda: save(img))
        b2.place(x=90, y=440)
        root4.mainloop()


def filter6(filename, root3):
    root3.destroy()
    root4 = Tk()
    img = Image.open(filename)
    img.thumbnail((700, 700))
    r, g, b = img.split()
    img = ImageChops.invert(img)
    photo = ImageTk.PhotoImage(img)
    label4 = Label(root4, image=photo)
    label4.pack()
    b1 = Button(text="    BACK    ", command=lambda: openfilters(filename, root4))
    b1.place(x=15, y=440)
    b2 = Button(text="    SAVE    ", command=lambda: save(img))
    b2.place(x=90, y=440)
    root4.mainloop()

def filter7(filename, root3):
    root3.destroy()
    root4 = Tk()
    img = Image.open(filename)
    img = img.filter(ImageFilter.GaussianBlur(radius=8))
    img.thumbnail((700, 700))
    photo = ImageTk.PhotoImage(img)
    label4 = Label(root4, image=photo)
    label4.pack()
    b1 = Button(text="    BACK    ", command=lambda: openfilters(filename, root4))
    b1.place(x=15, y=440)
    b2 = Button(text="    SAVE    ", command=lambda: save(img))
    b2.place(x=90, y=440)
    root4.mainloop()


def filter8(filename, root3):
    root3.destroy()
    root4 = Tk()
    img = Image.open(filename)
    img.thumbnail((700, 700))
    b = ImageEnhance.Brightness(img)
    img = b.enhance(1.3)
    photo = ImageTk.PhotoImage(img)
    label4 = Label(root4, image=photo)
    label4.pack()
    b1 = Button(text="    BACK    ", command=lambda: openfilters(filename, root4))
    b1.place(x=15, y=440)
    b2 = Button(text="    SAVE    ", command=lambda: save(img))
    b2.place(x=90, y=440)
    root4.mainloop()

def filter9(filename, root3):
    root3.destroy()
    root4 = Tk()
    img = Image.open(filename)
    img.thumbnail((700, 700))
    c = ImageEnhance.Color(img)
    img = c.enhance(1.3)
    photo = ImageTk.PhotoImage(img)
    label4 = Label(root4, image=photo)
    label4.pack()
    b1 = Button(text="    BACK    ", command=lambda: openfilters(filename, root4))
    b1.place(x=15, y=440)
    b2 = Button(text="    SAVE    ", command=lambda: save(img))
    b2.place(x=90, y=440)
    root4.mainloop()

def filter10(filename, root3):
    root3.destroy()
    root4 = Tk()
    img = Image.open(filename)
    img.thumbnail((700, 700))
    b = ImageEnhance.Brightness(img)
    img = b.enhance(1.2)
    c = ImageEnhance.Color(img)
    img = c.enhance(1.2)
    s = ImageEnhance.Sharpness(img)
    img = s.enhance(1.3)
    photo = ImageTk.PhotoImage(img)
    label4 = Label(root4, image=photo)
    label4.pack()
    b1 = Button(text="    BACK    ", command=lambda: openfilters(filename, root4))
    b1.place(x=15, y=440)
    b2 = Button(text="    SAVE    ", command=lambda: save(img))
    b2.place(x=90, y=440)
    root4.mainloop()

def nextf(filename,root):
    root.destroy()
    root3 = Tk()
    file = Image.open(filename)
    file.thumbnail((700, 700))
    photo = ImageTk.PhotoImage(file)
    l33 = Label(root3, image=photo)
    l33.pack()
    b1 = Button(text="    Filter 7    ", command=lambda: filter7(filename, root3))
    b1.place(x=15, y=440)
    b2 = Button(text="    Filter 8    ", command=lambda: filter8(filename, root3))
    b2.place(x=90, y=440)
    b3 = Button(text="    Filter 9    ", command=lambda: filter9(filename, root3))
    b3.place(x=165, y=440)
    b4 = Button(text="    Filter 10    ", command=lambda: filter10(filename, root3))
    b4.place(x=240, y=440)
    b7 = Button(text="    C R O P    ", command=lambda: crop(filename, root3))
    b7.place(x=315, y=440)
    b8 = Button(text="    NEW IMAGE   ", command=lambda: slide2(root3))
    b8.place(x=390, y=440)
    b8 = Button(text=" <<< ", command=lambda: openfilters(filename,root3))
    b8.place(x=490, y=440)
    root3.mainloop()

def openfilters(filename,root2):
    root2.destroy()
    root3 = Tk()
    file=Image.open(filename)
    file.thumbnail((700, 700))
    photo = ImageTk.PhotoImage(file)
    l33 = Label(root3, image=photo)
    l33.pack()
    b1 = Button(text="    Filter 1    ",command = lambda :filter1(filename,root3))
    b1.place(x=15, y=440)
    b2=Button(text="    Filter 2    ",command = lambda :filter2(filename,root3))
    b2.place(x=90,y=440)
    b3 = Button(text="    Filter 3    ",command = lambda :filter3(filename,root3))
    b3.place(x=165, y=440)
    b5 = Button(text="    Filter 4    ",command = lambda :filter4(filename,root3))
    b5.place(x=240, y=440)
    b4 = Button(text="    Filter 5    ", command=lambda: filter5(filename, root3))
    b4.place(x=315, y=440)
    b6 = Button(text="    Filter 6    ", command=lambda: filter6(filename, root3))
    b6.place(x=390, y=440)
    b7 = Button(text="    C R O P    ", command=lambda: crop(filename, root3))
    b7.place(x=465, y=440)
    b8 = Button(text="    NEW IMAGE   ",command = lambda:slide2(root3))
    b8.place(x=540, y=440)
    b8 = Button(text=" >>> ", command=lambda: nextf(filename,root3))
    b8.place(x=640, y=440)
    root3.mainloop()


def crop1(filename,root):
    root.destroy()
    root2=Tk()
    img = Image.open(filename)
    img.thumbnail((700,700))
    s = img.size[0] / 100
    e = img.size[1] / 100
    st = img.size[0] - s * 10
    et = img.size[1] - e * 10
    area = (s, e, st, et)
    img = img.crop(area)
    photo = ImageTk.PhotoImage(img)
    label4 = Label(root2, image=photo)
    label4.pack()
    b5 = Button(text="    BACK    ", command=lambda: crop(filename, root2))
    b5.place(x=15, y=390)
    b5 = Button(text="    SAVE    ", command=lambda: save(img))
    b5.place(x=90,y=390)
    root2.mainloop()

def crop2(filename,root):
    root.destroy()
    root2=Tk()
    img = Image.open(filename)
    img.thumbnail((700,700))
    s = img.size[0] / 100
    e = img.size[1] / 100
    st = img.size[0] / 3
    et = img.size[1]
    area = (0, 0, st, et)
    img = img.crop(area)
    photo = ImageTk.PhotoImage(img)
    label4 = Label(root2, image=photo)
    label4.pack()
    b5 = Button(text="    BACK    ", command=lambda: crop(filename, root2))
    b5.place(x=15, y=390)
    b5 = Button(text="    SAVE    ", command=lambda: save(img))
    b5.place(x=90,y=390)
    root2.mainloop()

def crop3(filename,root):
    root.destroy()
    root2=Tk()
    img = Image.open(filename)
    img.thumbnail((700,700))
    s = img.size[0] / 2
    st = img.size[0]
    et = img.size[1]
    area = (s, 0, st, et)
    img = img.crop(area)
    photo = ImageTk.PhotoImage(img)
    label4 = Label(root2, image=photo)
    label4.pack()
    b5 = Button(text="    BACK    ", command=lambda: crop(filename, root2))
    b5.place(x=15, y=390)
    b5 = Button(text="    SAVE    ", command=lambda: save(img))
    b5.place(x=90,y=390)
    root2.mainloop()


def crop4(filename,root):
    root.destroy()
    root2=Tk()
    img = Image.open(filename)
    img.thumbnail((700,700))
    s = img.size[0] / 4
    st = img.size[0] - s
    et = img.size[1]
    area = (s, 0, st, et)
    img = img.crop(area)
    photo = ImageTk.PhotoImage(img)
    label4 = Label(root2, image=photo)
    label4.pack()
    b5 = Button(text="    BACK    ", command=lambda: crop(filename, root2))
    b5.place(x=15, y=390)
    b5 = Button(text="    SAVE    ", command=lambda: save(img))
    b5.place(x=90,y=390)
    root2.mainloop()


def crop5(filename,root):
    root.destroy()
    root2=Tk()
    img = Image.open(filename)
    img.thumbnail((700,700))
    e = img.size[1] / 5
    st = img.size[0]
    et = img.size[1] - e
    area = (0, e, st, et)
    img = img.crop(area)
    photo = ImageTk.PhotoImage(img)
    label4 = Label(root2, image=photo)
    label4.pack()
    b5 = Button(text="    BACK    ", command=lambda: crop(filename, root2))
    b5.place(x=15, y=250)
    b5 = Button(text="    SAVE    ", command=lambda: save(img))
    b5.place(x=90,y=250)
    root2.mainloop()



def crop(filename,root2):
    root2.destroy()
    root6 = Tk()
    file = Image.open(filename)
    file.thumbnail((700, 700))
    photo = ImageTk.PhotoImage(file)
    l33 = Label(root6, image=photo)
    l33.pack()
    b1 = Button(root6,text="    CROP 1    ",command = lambda : crop1(filename,root6))
    b1.place(x=15, y=440)
    b2 = Button(root6,text="    CROP 2    ",command = lambda : crop2(filename,root6))
    b2.place(x=90, y=440)
    b3 = Button(root6,text="    CROP 3    ",command = lambda : crop3(filename,root6))
    b3.place(x=165, y=440)
    b4 = Button(root6,text="    CROP 4    ",command = lambda : crop4(filename,root6))
    b4.place(x=240, y=440)
    b5 = Button(root6,text="    CROP 5    ", command=lambda: crop5(filename, root6))
    b5.place(x=315, y=440)
    b7 = Button(text="    C R O P    ", command=lambda: openfilters(filename, root6))
    b7.place(x=390, y=440)
    b8 = Button(text="    NEW IMAGE   ", command=lambda: slide2(root6))
    b8.place(x=465, y=440)
    root6.mainloop()


def slide2(root):
    filename=askopenfilename (filetypes = (("Images","*.jpg"),("PNG","*.png"),("All Files","*.*")),initialdir="Desktop",title="Select File")
    if filename is not "":
        root.destroy()
        root2=Tk()
        file=Image.open(filename)
        file.thumbnail((700,700))
        photo = ImageTk.PhotoImage(file)
        l22=Label(root2,image=photo)
        l22.pack()
        b21 = Button(root2, text="FILTERS",command=lambda :openfilters(filename,root2))
        b21.place(x=15,y=440)
        b22 = Button(root2, text="CROP", command=lambda: crop(filename, root2))
        b22.place(x=75,y=440)
        root2.mainloop()



root=Tk()
root.wm_title("Image Filters")
bi= Image.open("cssfilters1.jpg") ##bi=Background Image
photo=ImageTk.PhotoImage(bi)
l=Label(root,image=photo)
l.pack(fill=X)
l2=Label(root,text="WELCOME TO THE IMAGE FILTERS            MAKE AWESOME PICTURES HERE",fg="white",bg="black",height="150")
l2.config(font="45")
l2.pack(fill=X)
bui=Image.open("plus.jpg")
bui.thumbnail((50,50))
phot=ImageTk.PhotoImage(bui)
b=Button(l2,text="\n\nClick here",image=phot,bg="black",command = lambda :slide2(root))
b.pack()

root.mainloop()

























