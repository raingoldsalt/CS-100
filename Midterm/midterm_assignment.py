# Jun Kang
# CS 100 
# Fall 23
# Midterm Assignment

# Q1 [1pt]: Manipulate the parameter myList by performing
# the following actions to myList, in this order:
#   - Append 'word'
#   - Append 3
#   - Insert the value of 'cat' at position 3
#   - Remove the first 9
#   - Remove the item at index 2 by using pop
#   - Return myList when finished
def manipulate(myList):
    myList.append('word')
    myList.append('3')
    myList.insert(3, 'cat')
    myList.remove(9)
    myList.pop(2)
    return myList


# Q2 [1pt]: Create a function called listOfWords which takes a parameter
# called myPhrase and splits it into a list of words. Return the list of words.

def listOfWords(myPhrase):
    low = myPhrase.split()
    return low

# Q3 [2pt]: Finish the following function 'fibonacciList' that populates the first
# numTerms indexes of myList such that each index of the list corresponds to the 
# correct Fibonacci number, then returns the list.
# Ex1: nums = 3, list = [1, 1, 2]
# Ex2: nums = 8, list = [1, 1, 2, 3, 5, 8, 13, 21]
def fibonacciList(numTerms):
    myList = []
    if numTerms >= 1:
        myList.append(1)
        if numTerms >= 2:
            myList.append(1)
    for i in range(2, numTerms):
        nextnumber = int(myList[i-1])+int(myList[i-2])
        myList.append(nextnumber)
    return myList


# Although Python provides many list methods, it's good practice
# and instructive to think about how they are implemented. Implement
# a python function that works like the following
#   - Q4 [1pt]: find
#   - Q5 [1pt]: min


# Q4 (find equivalent)
# Return the first index where the given item is found in myList, or if
# it cannot be found, return -1. (don't use find)
def q4_find(myList, item):
    if item in myList:
        x = myList.index(item)
        return x
    else:
        return -1


# Q5 (min equivalent)
# Return the minimum element in the list. (don't use min)
def q5_min(myList):
    minimum = float('inf')
    for i in range(len(myList)):
        if(myList[i]<minimum):
            minimum = myList[i]
    return minimum


# Q6 [2pts] Finish the function 'ascendingSort'. Given a list of distinct integers, 
# sort them in ascending order, and return the sorted list.
# HINT: While there are multiple approaches to this, one possible
# approach is outlined below:
# -Create a second list
# -Find the smallest value in the 1st list
# -Add the smallest value to the 2nd list
# -Remove the value from the 1st list
# -Repeat till the 1st list is empty
# -Return the 2nd list.
#
# IMPORTANT: You cannot use the sort function for this question.
# Doing so will result in no credit given.
def ascendingSort(myList):
    secondList = []
    for j in range(len(myList)):
        minimum = float('inf')
        for i in range(len(myList)):
            if(myList[i]<minimum):
                minimum = myList[i]
        secondList.append(minimum)
        myList.remove(minimum)
    return secondList


# Q7 [2pts]: Create a function 'twoSum' that takes two parameters:
#   1. a list of distinct integers myList 
#   2. an integer targetInt
# that returns True if there are two different integers in myList that 
# add up to targetInt, and False if not.

def twoSum(myList, targetInt):
    newList = []
    for num in myList:
        sub = targetInt - num
        if(sub in newList):
            return True
        newList.append(num)
    return False

            

if __name__ == "__main__":
    ## TODO: Uncomment each function call out as you work through the questions.
    ## When you're finished, all of them should be uncommented.
    ## DO NOT make any other changes here other than to uncomment.
    listA = [7, 'a', 'cat', 7, 9, False, 9]
    listB = ['e', 'c', 'b', 'bird', 9, 'd', 42]
    print("Q1 - testA:", manipulate(listA))
    print("Q1 - testB:", manipulate(listB))
    print("----------------------")
    print("Q2 - testA:", listOfWords("fun with python programming") )
    print("Q2 - testB:", listOfWords("if you like this class you might like CS110 too") )
    print("----------------------")
    print("Q3 - testA:", fibonacciList(5) )
    print("Q3 - testB:", fibonacciList(10) )
    print("----------------------")
    list4A = [1, 5, 10, 23, 42, 9, 8, 15, 2, 3, 104]
    list4B = ['bat', 'rat', 'emu', 'cow', 'dog', 'cat', 'rat', 'fish']
    print("Q4 - testA:", q4_find(list4A, 42) )
    print("Q4 - testB:", q4_find(list4B, 'bird') )
    print("----------------------")
    list5A = [1, -5, 10, 23, 42, 9, 8, 15, 3]
    print("Q5 - testA:", q5_min(list4A) )
    print("Q5 - testB:", q5_min(list5A) )
    print("----------------------")
    print("Q6 - testA:", ascendingSort(list4A) )
    print("Q6 - testB:", ascendingSort(list5A) )    
    print("----------------------")
    list7A = [1, 2, 3, 4, 5, 6]
    print("Q7 - testA:", twoSum(list7A, 10) )
    print("Q7 - testB:", twoSum(list7A, 12) )    



