# Name: Jun Kang
# HW 2
import turtle

# Q1 [1 pts]
# Modify the drawSquare function definition so that it draws a rectangle
# whose horizontal width is twice the vertical width
def drawSquare(myTurtle, sideLength):
    myTurtle.forward(sideLength*2)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength*2)
    myTurtle.right(90)
    myTurtle.forward(sideLength)

# Q2 [1 pts]
# Create a new function called drawRectangle that takes three parameters:
# myTurtle, width, and height. Use myTurtle to draw the rectangle with
# the given width and height. Uncomment out the function call to drawRectangle
# to test the function.
    
def drawRectangle(myTurtle,width,height):
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(height)
    myTurtle.right(90)
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(height)

# Q3 [1 pts]
# Add code to the function definition for question3.
# Use the range function to print out all numbers from -10 to 10, inclusive.
# Uncomment out the function call to question3 to test the function.
def question3():
    print("Answer to Q3: All numbers from -10 to 10")
    # Put your code here
    for x in range(-10,11,1):
        print(x)

# Q4 [1 pts]
# Add code to the function definition for question4.
# Use the range function to print out all numbers from 10 to -10, inclusive.
# Uncomment out the function call to question4 to test the function.
def question4():
    print("Answer to Q4: All numbers from 10 to -10")
    # Put your code here
    for y in range(10,-11,-1):
        print(y)
    
# Q5 [1 pts]
# The drawDoubleSpiral function currently only has two parameters: firstTurtle and maxSide.
# The firstTurtle draws a spiral where each side is of length maxSide.
# Modify the function definition to take three parameters: firstTurtle, secondTurtle, and maxSide.
# The secondTurtle will create a second spiral going in the opposite direction,
# where each side is of length maxSide.
# Uncomment out the function call to drawDoubleSpiral to test the function.
def drawDoubleSpiral(firstTurtle, secondTurtle, maxSide):
    for sideLength in range(10, maxSide+1, 5):
        firstTurtle.forward(sideLength)
        firstTurtle.right(130)
        secondTurtle.forward(sideLength)
        secondTurtle.left(130)

# Q6 [1 pts]
# Modify the function definition for question6.
# Use the given turtle to plot the function y = x/3 - 300.
# Use x-coordinates from -100 to 100. Uncomment out the function call to test it.
def question6(myTurtle):
    print("Answer to Q6: Plotted function y = x/3 - 300")
    # Put your code here
    myTurtle.penup()
    myTurtle.setposition(-100,-1000/3)
    print("The turtle's location is" ,myTurtle.position())
    myTurtle.pendown()
    #myTurtle.goto(100,-800/3)
    for x in range(-100,100+1):
        myTurtle.goto(x,(x/3-300))        
    print("The turtle's location is" ,myTurtle.position())




#####################################################################################
# Everything below this part calls the functions up above.
#
# DO NOT CHANGE ANY CODE BELOW EXCEPT TO COMMENT OUT / UNCOMMENT LINES OF CODE
# Some code is commented out because it won't work until you've correctly
# implemented the function definitions up above. Work on the homework one
# question at a time, and then uncomment out the function call which corresponds
# to that question when you're ready to test it.
#
# Do not change any code below these lines other than to uncomment it or comment it out.
#####################################################################################
ivy = turtle.Turtle()
ivy.color('red')
ivy.speed('fastest')
ivy.begin_fill()

# Q1
drawSquare(ivy, 200)
ivy.end_fill()

# Q2
width = 50
height = 100
ivy.color('black')
drawRectangle(ivy, width, height)

# Q3
question3()

# Q4
question4()

# Q5
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.color('green')
turtle2.color('blue')
turtle1.speed('fastest')
turtle2.speed('fastest')
drawDoubleSpiral(turtle1, turtle2, 300)

# Q6
bob = turtle.Turtle()
question6(bob)