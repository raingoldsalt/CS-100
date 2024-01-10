import turtle

bob = turtle.Turtle()
print( bob )

print( "Orig. pos: ", bob.position() )

bob.forward(100)
bob.right(90)
bob.forward(50)

print( "Later pos: ", bob.position() )
print( "Direction: ", bob.heading() )

def drawSquare(myTurtle,sideLength):
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)

bob = turtle.Turtle()
bob.pencolor('red')
bob.fillcolor('yellow')
bob.begin_fill()
drawSquare(bob, 150)
bob.end_fill()

drawSquare(bob, 300)

def drawTriangle(myTurtle,sideLength):
    myTurtle.forward(sideLength)
    myTurtle.right(120)
    myTurtle.forward(sideLength)
    myTurtle.right(120)
    myTurtle.forward(sideLength)

bob.pencolor('blue')
bob.fillcolor('gray')
bob.begin_fill()
drawTriangle(bob, 200)
bob.end_fill()

def drawPentagon(myTurtle,length):
    myTurtle.forward(length)
    myTurtle.right(72)
    myTurtle.forward(length)
    myTurtle.right(72)
    myTurtle.forward(length)
    myTurtle.right(72)
    myTurtle.forward(length)
    myTurtle.right(72)
    myTurtle.forward(length)


bob.pencolor('green')
bob.fillcolor('orange')
bob.begin_fill()
drawPentagon(bob,50)
bob.end_fill()
bob.pencolor('purple')
drawPentagon(bob,100)