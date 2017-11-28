from PIL import Image
from PIL import ImageChops

img=Image.open("IMG_9620.jpg")
img2=Image.open("IMG_0296.jpg")
a=img.size[0];
b=img.size[1];
print(a)
print(b)
print(img.size)
r2,g2,b2=img2.split()
r,g,b=img.split()

img.thumbnail((200,200))
img.show()