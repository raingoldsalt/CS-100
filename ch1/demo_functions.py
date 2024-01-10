# Jun Kang


# A function definition explains how a function works.

# prints out a hello message
def hello():
    print("Hello students")

# computes and returns average of two numbers
def avg(no1, no2):
    s = no1+no2
    return s/2


# A function call executes the code within that function.
# Functions must be defined before they can be called.
hello()

result = avg(345, 6788)
print(result)

hello()
# If I write a code 'hello(),' the python will print "Hello students."

print(hello())
# The output is "Hello students," and "none."
# In my opinion, the result of hello(), which returns "Hello students", is printed first, and because it has done it's job, only print() is left. Because there is nothing to return, it returns none.

avg(4,8)
# The python computes the average of 4 and 8, which is 6, but it doesn't print the answer because we didn't let him print.

print( avg(4,8) )
# The result is 6.0.

rez = avg(4,8)
print(rez)
# The output is 6.0.
# Here we defined the function res is the average between two numbers, in this case 4 and 8.
# The difference between this one and the previous one is that here we defined the function rez equals to avg(num1,num2) while the previous one computed the average of 4 and 8 inside of the parentheses.
# In my opinion, it makes things more convenient since once we define something, we can use the function by calling it. Therefore, whenever we want to know the average of 4 and 8, we can know the answer by typing 'rez' instead of typing 'avg(4,8).'
# In addition, it makes codes inside of the parentheses simple. For example, if we have lots of calculations or things to do, we will probably make mistakes as we try to put lots of things inside of the parenthese.

rez2 = avg(50,75)
print(rez2)
# It calculates the average of 50 and 75.

def long_hello():
    print("Hello students")
    print("Oh hi")
    print("How are you?")
    print("I'm good thanks.")
long_hello()
# This prints 4 sentences.

def prod(num1,num2):
    a = num1*num2
    return a

p = prod(10,50)
print(p)

# This function multiplies two numbers.

def weirdsum(n1,n2,n3,n4):
    b = (n1+n2)*(n3+n4)
    return b

w = weirdsum(1,2,3,4)
print(w)

# This function returns the sum of the first two multiplied by the sum of the last two.

def secondsToday():
    st = 24*60*60
    print("IN A DAY THERE ARE :" ,st,  "seconds.")
secondsToday()

# This function tells the number of seconds in a day.