# Name: Jun Kang
# HW 4

import math

# Q1 [1pt]. Write a selection statement (if statement) that sets the value
# of a variable named answer to 1 if the input parameter is equal to 100.
# Set answer to 2 otherwise. Return the variable answer.
def q1(input):
    # your code here
    answer = 0
    if(input==100):
        answer = 1
    else:
        answer = 2
    return answer

# Q2 [1pt]. Write a selection statement that sets the value of a variable
# gradepoint to 4 if the parameter score is greater than or equal to 90,
# 3 if the score is between 80 and 89 (inclusive),
# 2 if score is between 70 and 79 (inclusive)
# 1 if score is between 60 and 69 (inclusive)
# and 0 otherwise.
def q2(score):
    gradepoint = 0
    if(score>=90):
        gradepoint = 4
    elif(80<=score<=89):
        gradepoint = 3
    elif(70<=score<=79):
        gradepoint = 2
    elif(60<=score<=69):
        gradepoint = 1
    else:
        gradepoint = 0
    return gradepoint

# Q3 [1pt]. A year is a leap year if it is divisible by 4,
# unless it is a century year (2100, 2200, etc.), then it is not a leap year.
# The only exception to this rule are century years that can exactly divide by 400,
# then it is a leap year.
# Write a function called leapYear which takes a year as a parameter and
# returns True if the year is a leap year and False otherwise

def leapYear(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Q4 [1pt]. A fruit company sells oranges for 32 cents a pound,
# plus $7.50 per order for shipping. If an order is 100 pounds or more,
# shipping cost is reduced by $1.50.
# Write a function called costOfOranges that will take the number of
# pounds of oranges as a parameter and return the cost of the order.

def costOfOranges(pound):
    orange = 0.32
    regular_shipping = 7.5
    if(pound>=100):
        shipping = regular_shipping - 1.5
    else:
        shipping = regular_shipping
    cost = orange*pound+shipping
    return cost

# Q5 [1pt]. Fix the following function so that it returns the largest
# of the three input parameters

def maxOfThree(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Q6 [1pt]. Write a function called getCircumference that takes one
# parameter for the radius, computes the circumference of a circle
# using the math module's pi constant, and returns it.
# Note: you'll need to import math at the top of this file

def getCircumference(radius):
    circumference = 2*radius*math.pi
    return circumference

# Q7 [1pt]. Write a function called getArea that takes one parameter
# for the radius, computes the area of a circle using the math
# module's pi constant, and returns it.
# Note: you'll need to import math at the top of this file

def getArea(radius):
    area = radius*radius*math.pi
    return area

# Q8 [1pt]. Write a function called getVolume that takes one parameter
# for the radius, computes the volume of a sphere with that radius,
# and returns it.
# Note: you'll need to import math at the top of this file

def getVolume(radius):
    volume = (4/3)*math.pi*(radius**3)
    return volume

# Q9 [1pt]. Write a function called calculatePay that takes two
# parameters - the first parameter is the pay rate, and the second
# parameter is the number of hours worked that week. The function should
# return the total pay for the week. Any hours over 40 are paid
# at time and a half

def calculatePay(pay_rate,number_of_hours):
    if(number_of_hours<=40):
        total_pay = pay_rate*number_of_hours
    else:
        normal_pay = pay_rate*40
        over_pay = (pay_rate*1.5)*(number_of_hours-40)
        total_pay = normal_pay+over_pay
    return total_pay

# Q10 [1pt]. Write a function called calculatePay2 that takes
# three parameters - the first is the pay rate, the second is the
# hours worked that week, and the third is the bonus.
# The function should return the total pay for the week, including
# time and a half for overtime (> 40 hours), plus the bonus.
# Hint: Try using the previous function you wrote for Q9!

def calculatePay2(pay_rate,number_of_hours,bonus):
    if(number_of_hours<=40):
        total_pay = pay_rate*number_of_hours+bonus
    else:
        normal_pay = pay_rate*40
        over_pay = (pay_rate*1.5)*(number_of_hours-40)
        total_pay = normal_pay+over_pay+bonus
    return total_pay

if __name__ == "__main__":
    ## TODO: Uncomment each function call out as you work through the questions.
    ## When you're finished, all of them should be uncommented.
    ## DO NOT MAKE ANY OTHER CHANGES HERE EXCEPT TO UNCOMMENT
    print("Q1 - testA:", q1(100))
    print("Q1 - testB:", q1(52))
    print("----------------------")
    print("Q2 - testA:", q2(100))
    print("Q2 - testB:", q2(90))
    print("Q2 - testC:", q2(89))
    print("Q2 - testD:", q2(75))
    print("Q2 - testE:", q2(69))
    print("Q2 - testF:", q2(55))
    print("----------------------")
    print("Q3 - testA:", leapYear(2020))
    print("Q3 - testB:", leapYear(1900))
    print("Q3 - testC:", leapYear(2000))
    print("----------------------")
    print("Q4 - testA:", costOfOranges(90))
    print("Q4 - testB:", costOfOranges(100))
    print("----------------------")
    print("Q5 - testA:", maxOfThree(10, 20, 30))
    print("Q5 - testB:", maxOfThree(2, 3, 1))
    print("Q5 - testC:", maxOfThree(1, 3, 2))
    print("Q5 - testD:", maxOfThree(5, 4, 2))
    print("Q5 - testE:", maxOfThree(5, 2, 4))
    print("----------------------")
    print("Q6 - testA:", getCircumference(1))
    print("Q6 - testB:", getCircumference(3))
    print("----------------------")
    print("Q7 - testA:", getArea(1))
    print("Q7 - testB:", getArea(3))
    print("----------------------")
    print("Q8 - testA:", getVolume(1))
    print("Q8 - testB:", getVolume(3))
    print("----------------------")
    print("Q9 - testA:", calculatePay(8.25, 10))
    print("Q9 - testB:", calculatePay(8.5, 40))
    print("Q9 - testC:", calculatePay(8.5, 45))
    print("----------------------")
    print("Q10 - testA:", calculatePay2(8.25, 10, 0))
    print("Q10 - testB:", calculatePay2(8.5, 40, 200))
    print("Q10 - testC:", calculatePay2(8.5, 45, 150))
