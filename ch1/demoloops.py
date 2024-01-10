import turtle

#Jun Kang

# define your functions here
def drawPolygon(myTurtle, sideLength, numSide):
    turnAngle = 360 / numSide
    for i in range(numSide):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)

def drawCircle(myTurtle, radius):
    circumference = 2*3.14*radius
    sideLen = circumference / 360 # note that 360 is the number of sides
    drawPolygon(myTurtle, sideLen, 360)

def printManyThings():
    print("TODO 1")
    # If I set the range 5,100, it will not include 100. Therefore, I should set the range 5 to 101(any number greater than 101 but less than 106)
    for x in range(5,101,5):
        print(x)

def drawSpiral(myTurtle, maxSide):
    for sideLength in range(5, maxSide+1, 5):
        myTurtle.forward(sideLength)
        myTurtle.right(90)
        print(sideLength/5,"times executed")
        

# call your functions here
printManyThings()

bob = turtle.Turtle()
bob.speed('fastest') # this makes bob run really fast
drawSpiral(bob,100)
print("Answer to question 3 is: " ,20, "times")

# draw octagon!
def drawOctagon(myTurtle, sideLength):
    for x in range(8):
        myTurtle.forward(sideLength)
        myTurtle.right(45)

bob = turtle.Turtle()
bob.speed('fastest')
drawOctagon(bob,100)


def drawTriangle(myturtle, sideLength):
    for side in range(3):
        myturtle.forward(sideLength)
        myturtle.right( 360 / 3 )

# draw a triangle!
bob = turtle.Turtle()
bob.speed('fastest')
drawPolygon(bob,100,3)

# draw a hexagon!
bob = turtle.Turtle()
bob.speed('fastest')
drawPolygon(bob,100,6)

# draw a circle!
bob = turtle.Turtle()
bob.speed('fastest')
drawCircle(bob,100)