def add(x,y):
    z = x+y
    return z

a = add(7,11)
print(a)

def addPrint(x,y):
    b = x+y
    print(b)
    
addPrint(7,12)

def subtract(x,y):
    s = x-y
    print(s)
    
subtract(12,5)

def hello(name):
    print("Hello, "+name)
    print("Welcome to CS 100")
    print("Have an awesome day!")
    
hello("Jun")

def mystery():
    print("A")
    print("B")
    return "123"
    print("C")
    print("D")
    
myResult = mystery()
print(myResult)
# This function prints A, B, and 123. I guess return() ends the function, so everything comes after return() will not work

def solveQuadraticEquation(a,b,c):
    #(a*(x**2))+(b*x)+c
    import math
    #x = ((-1*b) +- math.sqrt((b**2)-(4*a*c)))/(2*a)
    x=((-1*b)+math.sqrt((b**2)-(4*a*c)))/(2*a)
    x_2=((-1*b)-math.sqrt((b**2)-(4*a*c)))/(2*a)
    print("The results are " ,x, "and" ,x_2)

solveQuadraticEquation(3,10,3)
    
    