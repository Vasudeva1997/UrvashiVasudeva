from PIL import Image
from PIL import ImageOps #fro flipping of the image

img=Image.open("IMG_9620.jpg")

print("Rotation sequence")
print("1.Left\n2.Right\n3.upside\n4.Manual\n5.Flipping the image")

i=int(input())

if(i==1):
    img.rotate(90).show()
if(i==2):
    img.rotate(-90).show()
if(i==3):
    img.rotate(180).show()
if(i==4):
    print("Enter the angle you want to rotate the picture")
    a=int(input())
    img.rotate(a).show()
if(i==5):
    ImageOps.mirror(img).show()