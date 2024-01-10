i = 2 + 3
print(i)
i = i + 7
print("i = ", i)
p = 10 * 2
print("p = ", p)
x = 2**(32)
print("The power is: ", x)
avg=(23+15+18+21)/4
print("The average of these numbers is ", avg)
pi=3.14159
area=(pi*(3**2))
print("The area of the circle is ", area)

#limit=1000000**100000000
#print(limit)
#I tried to compute 1000000 to the power of 100000000, but the error messages are printed; the result doesn't appear in the Shell Area.
#Therefore, I believe there is a limit on the size of numbers

limits=1000**1000
print(limits)

#When I tried 1000 to the power of 1000, the python could calculate it.
#However, when I tried 1000**10000, the python says that I exceeded the limit (4300) for integer string.
#I guess this 4300 means the maximum digits of numbers that python can print. 
