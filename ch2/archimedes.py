# Jun Kang

import math

# The function below approximates the number Pi by using the Archimedes method for an octagon. Copy it to the top of your file. Call it to compute the value of Pi. Print the result.
def archimedesOctagon():
    side = 2 * math.sin(math.radians(45/2.0))
    polygonCircumference = 8 * side
    return (polygonCircumference / 2)

# Create another function with the function signature def archimedes(numSides). 
def archimedes(numSides):
    side = 2 * math.sin(math.radians(360/numSides/2.0))
    polygonCircumference = numSides * side
    return (polygonCircumference / 2)

# Using a for loop and an accumulator variable, compute the sum of the first 50 numbers. Print the result.
a=0
for x in range(1,51):
    a=a+x
print(a)

# Using a for loop and an accumulator variable, compute the product of the first 50 numbers. Print the result.
b=1
for y in range(1,51):
    b=b*y
print(b)

# Use a for loop to print all odd numbers between 0-100 (inclusive), each on a new line.

for z in range(1,100,2):
    print(z)


# Use a for loop to print all multiples of 4 between 0-100 (inclusive), each on a new line.
for q in range(0,101,4):
    print(q)
# 0 is also multiple of 4.

print(archimedesOctagon())

#Try your new function with the following function calls.
print('Octagon: ', archimedes(8))
print('Dodecadon: ', archimedes(12))
# Which is better?
# Dodecadon is better. It is much closer to pi-value, which is 3.141592.....


# Add the following for loop in your program and run it. What is this for loop accomplishing? Write in comments.
for sides in range(8, 100, 8):
    print(sides, archimedes(sides))
# This loop helps us approximating the value of pi by using the Archimedes method and increasing the number of sides of polygons by 8.


for sides in range(0, 8):
    print(10**sides, archimedes(10**sides))

print(math.pi)