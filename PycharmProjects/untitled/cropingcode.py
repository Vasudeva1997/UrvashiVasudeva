from PIL import Image
img=Image.open("IMG_0296.jpg")
print(img.size)
print(img.format)
img.show()
print("The image you seleceted is shown.\nIf you want to crop by default, press \n1. Crop from all side\n2. For left crop\n3. for right crop"
      "\n4. Streth from 2 sides(left and right)\n5. Stretch from 2 sides(top and bottom)\n6. Custom Crop\n0. Exit ")
while 1:
    cc = int(input())
    if cc == 1:  # all side crop
        s = img.size[0] / 100
        e = img.size[1] / 100
        st = img.size[0] - s * 10
        et = img.size[1] - e * 10
        area = (s, e, st, et)
    if cc == 2:  ## left crop
        s = img.size[0] / 100
        e = img.size[1] / 100
        st = img.size[0] / 3
        et = img.size[1]
        area = (0, 0, st, et)
    if cc == 3:  # right crop
        s = img.size[0] / 2
        st = img.size[0]
        et = img.size[1]
        area = (s, 0, st, et)
        crop_img = img.crop(area)
    if cc == 4:  # strect to centre(left and right will be cut)
        s = img.size[0] / 4
        st = img.size[0] - s
        et = img.size[1]
        area = (s, 0, st, et)

    if cc == 5:  # strech from top and bottom
        e = img.size[1] / 5
        st = img.size[0]
        et = img.size[1] - e
        area = (0, e, st, et)
    if cc == 6:  # custom crop
        s = int(input("Enter the start of the X-axis from the top left of the pic"))
        e = int(input("Enter the start of the Y-axis from the top left of the pic"))
        st = int(input("Enter the end of the X-axis from the top left of the pic"))
        et = int(input("Enter the end of the Y-axis from the top left of the pic"))
        area = (s, e, st, et)
    if cc==0:
        break
    crop_img = img.crop(area)
    crop_img.show()