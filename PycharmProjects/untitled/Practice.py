import random
from math import sqrt

x,y = 0,0
for i in range(100):
    dx,dy = random.choice([(0,1),(1,0),(0,-1),(-1,0)])
    x +=dx
    y +=dy
    dis =  (x*x)+(y*y)
    sqrt(dis)
    if dis<=sqrt(25):
        continue
    else:
        print('More than 5 blocks at '+ str(i))
        break