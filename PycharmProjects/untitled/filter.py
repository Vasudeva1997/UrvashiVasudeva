from PIL import ImageEnhance
from PIL import Image
from PIL import ImageFilter


img=Image.open("IMG_0296.jpg")
img2 = Image.open("IMG_9620.jpg")
img = img.filter(ImageFilter.GaussianBlur(radius=8))
img.thumbnail((700,700))
img.show()



