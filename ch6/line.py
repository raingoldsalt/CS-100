from image import *
import random
   
myWin = ImageWin(300, 300, "Class image")
   
# create a new image which we modify
img = EmptyImage(300,300)
   
# diagonal pixels are colored black
for i in range(300):

    # create a new pixel object with (red, green, blue) values
    blackPixel = Pixel(0,0,0)

    # note: setPixel(columnPosition, rowPosition, pixelObject)
    # set pixel at given columnPosition and rowPosition to be the color of pixelObject
    img.setPixel(i,i,blackPixel) 
       
# YOUR CODE HERE (change image before it is displayed & saved)

for i in range(100):
    for j in range(100):
        redPixel = Pixel(255,0,0)
        img.setPixel(i,j,redPixel)
        
for i in range(100, 300):
    for j in range(100):
        randInt = random.randint(0,255)
        randInt2 = random.randint(0,255)
        randInt3 = random.randint(0,255)
        randPixel = Pixel(randInt, randInt2, randInt3)
        img.setPixel(i,j,randPixel)

# displays the image
img.draw(myWin)
   
# saves image to the given file name
img.save("classImg.gif")
   
# when you click anywhere on the window, it closes
myWin.exitOnClick()