import turtle
import math
import random

#A.1
sum=0
for x in range(51):
    sum=sum+x
print(sum)

#A.2
def fac(input):
    num=1
    for y in range(1,input+1,1):
        num=num*y
    print(num)
fac(10)

#A.3
bob = turtle.Turtle()
def ds(myTurtle,sideLength):
    for z in range(4):
        myTurtle.forward(sideLength)
        myTurtle.right(90)
        
ds(bob,300)
    
#A.4
for x in range(-10,11,1):
    print(x)

#A.5
def multiPrint(text,times):
    for k in range(times):
        print("",text,k+1,"times printed")

multiPrint("ABC",9)
        
#B.1
def plot(myTurtle):
    myTurtle.penup()
    myTurtle.setposition(0,18)
    myTurtle.pendown()
    for x in range(0,50):
        myTurtle.goto(x,(10*x+18))
plot(bob)

#B.2
def dt(myTurtle,sideLength):
    myTurtle.penup()
    myTurtle.setposition(0,0)
    myTurtle.pendown()
    myTurtle.pencolor('yellow')
    myTurtle.fillcolor('red')
    myTurtle.begin_fill()
    myTurtle.right(180)
    myTurtle.forward(sideLength)
    myTurtle.right(120)
    myTurtle.forward(sideLength)
    myTurtle.right(120)
    myTurtle.forward(sideLength)
    myTurtle.end_fill()

dt(bob,100)

#B.3
def drawRectangle(myTurtle):
    myTurtle.penup()
    myTurtle.setposition(0,0)
    myTurtle.pendown()
    myTurtle.right(30)
    myTurtle.pencolor('black')
    myTurtle.forward(100)
    myTurtle.right(90)
    myTurtle.forward(300)
    myTurtle.right(90)
    myTurtle.forward(100)
    myTurtle.right(90)
    myTurtle.forward(300)
drawRectangle(bob)


#B.4
def drawTriangle(myTurtle,side1,side2,angle):
    myTurtle.penup()
    myTurtle.setposition(50,50)
    myTurtle.pendown()
    myTurtle.left(180)
    myTurtle.pencolor('black')
    myTurtle.goto(side1+50,50)
    myTurtle.penup()
    myTurtle.setposition(50,50)
    myTurtle.pendown()
    myTurtle.right(180-angle)
    myTurtle.forward(side2)
    myTurtle.goto(side1+50,50)
drawTriangle(bob,100,200,130)
#C.1
def displayStudentInfo(name,age):
    print(name,"is a",age,"year old student.")
displayStudentInfo("Bob",20)
    
#C.2
def toCelsius(temperature):
    celsius = ((temperature-32)*(5/9))
    print(celsius)
toCelsius(59)

#C.3
def isEven(number):
    if(number%2==0):
        return True
    else:
        return False
print(isEven(21))

#C.4
def getGrade(score):
    if 90<=score<=100:
        return "A"
    elif 80<=score<=89:
        return "B"
    elif 70<=score<=79:
        return "C"
    elif 60<=score<=69:
        return "D"
    else:
        return "F"
print(getGrade(80))
print(getGrade(20))

#D.1
def b10(x):
    if x>10:
        return True
    else:
        return False
print(b10(10))

#D.3
def snowFall(sF):
    if sF>=10:
        print("there was a hurricane today")
    elif 7<sF<10:
        print("there was a lot of snow")
    elif 3<sF<=7:
        print("there was some snow I guess")
    else:
        print("not enough snow to matter")

snowFall(3)

#E.1
def isItRaining():
    a = random.random()
    print(a)
    if a>=(0.9):
        return True
    else:
        return False

print(isItRaining())

#E.2
def magicEightBallSays():
    b = random.random()
    if(b<=0.2):
        print("It is certain.")
    elif(0.2<b<=0.4):
        print("Outlook good.")
    elif(0.4<b<=0.6):
        print("Ask again that later.")
    elif(0.6<b<=0.8):
        print("Better not tell you now.")
    else:
        print("Very doubtful.")
magicEightBallSays()

#E.4
coinside=random.randint(0,1)
print(coinside)
    
#F.1
def archimedes(numSides):
    side = 2 * math.sin(math.radians(360/numSides/2.0))
    polygonCircumference = numSides * side
    return (polygonCircumference / 2)

for sides in range(0, 8):
    print(10**sides, archimedes(10**sides))     