import turtle 

def drawShape1(bob):
    for i in range(50):
        bob.forward(i * 10)
        bob.right(144)

def drawShape2(bob):
    for i in range(180):
        bob.forward(100)
        bob.right(30)
        bob.forward(20)
        bob.left(60)
        bob.forward(50)
        bob.right(30)
        
        bob.penup()
        bob.setposition(0, 0)
        bob.pendown()
        bob.right(2)

def drawShape3(bob):
    bob.pencolor("blue")
    for i in range(50):
        bob.forward(50)
        bob.left(123)
        
    bob.pencolor("red")
    for i in range(50):
        bob.forward(100)
        bob.left(123)

def drawShape4(bob):
    colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green']
    for x in range(360):
        bob.pencolor(colors[x % 6])
        bob.width(x / 5 + 1)
        bob.forward(x)
        bob.left(20)


coolBob = turtle.Turtle()
coolBob.speed(100)

# Call each function individually and comment the others out to see what it does.
#drawShape1(coolBob)
#drawShape2(coolBob)
drawShape3(coolBob)
#drawShape4(coolBob)