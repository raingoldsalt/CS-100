numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

grades = ['a', 'b', 'c', 'd', 'e']
print(grades)

def prettyPrint_v1(myList):
    for i in myList:
        print(i)
    
prettyPrint_v1(grades)

def prettyPrint_v2(myList):
    for i in range(len(myList)):
        print("index:  " , i , "  - value:  " , myList[i])

prettyPrint_v2(grades)

def listTimesTen(myList):
    otherList = []
    for i in myList:
        otherList.append(i*10)
    return otherList
    
print(listTimesTen(numbers))

def stringToList(myString):
    otherList = []
    for i in range(len(myString)):
        otherList.append(myString[i])
    return otherList

print(stringToList("example string"))
    