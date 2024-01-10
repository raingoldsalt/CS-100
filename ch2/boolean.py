import random

# 1
n = 10
k = 20
print( (n>10) and (k==20) )
print( (n==10) and (k==20) )
print( (n>10) or (k==20)   )
print( not( (n>10) and (k==20)) )
print( (n>10) or (k==10 or k!=5) )
print( (not(n>10)) and (not(k==20)) )
print( (n<20) or (k==20)  )
print( (n>=10) and (k<=20) )

# 2

#2.a
#((num>=0) and (num<100))

#2.b
#(((num<100) and (num>=0)) or (num==200))

#2.c
#((num>0) and (num<150))

# 3

# 3.a
#x=5
#y=11

# 3.b
#x=10
#y=11

# 3.c
x=0
y=5

if x>5:
    print("A")
elif y<10:
    print("B")
elif x==10:
    print("C")
else:
    print("D")

# 3.d
# Is there any value of x or y that will print “C”?
# No. C is supposed to be printed if X equals to 10, but when x=10, the first if statement(if x>5) is met, so it will print “A” rather than “C.”

#4

print(random.random())
print(random.random())
print(random.random())
# Why are they different?
# Because they are just printing any random number, the result would be different every time I run the code.


# 5

def threeIntegers(x,y,z):
    if (x>y) and (x>z):
        print(x)
    elif (y>x) and (y>z):
        print(y)
    elif (z>x) and (z>y):
        print(z)
    elif ((x>y) or (x>z)) and (x==y):
        print(x)
    elif ((x>y) or (x>z)) and (x==z):
        print(x)
    elif ((y>x) or (y>z)) and (y==x):
        print(y)
    elif ((y>x) or (y>z)) and (y==z):
        print(y)
    elif ((z>x) or (z>y)) and (z==x):
        print(z)
    elif ((z>x) or (z>y)) and (z==y):
        print(z)
    else:
        print("All three numbers are equal")

threeIntegers(20,30,40)

