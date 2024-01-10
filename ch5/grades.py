# TODO: Finish/fix
def getAverages(myList):
    Sum = 0
    for i in range(len(myList)):
        Sum = myList[i]+Sum
    Average = Sum/(len(myList))
    return Average

# TODO: Finish/fix
def getLowestGrade(myList):
    lowest = float('inf')
    for i in range(len(myList)):
        if(myList[i] < lowest):
            lowest = myList[i]
    return lowest

# TODO: Finish/fix
def getHighestGrade(myList):
    highest = float('-inf')
    for i in range(len(myList)):
        if(myList[i] > highest):
            highest = myList[i]
    return highest

# TODO: Finish/fix
def getGrade(score):
    if(score>=90):
        return "A"
    elif(80<=score<=90):
        return "B"
    elif(70<=score<=80):
        return "C"
    elif(60<=score<=70):
        return "D"
    else:
        return "F"
    
# TODO: Finish/Fix
def getGradeDistributionDict(myList):
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for s in myList:
        grade = getGrade(s)
        grades[grade] = grades[grade]+ 1
    return grades


numScores = input("How many scores? ")
numScores = int(numScores)

allScores = []
for i in range(numScores):
    nextScore = input("Enter Score: ") # TODO: fill in code to get next score from the user
    # TODO: add the nextScore to the list allScores
    nextScore = int(nextScore)
    allScores.append(nextScore)


print("Grades:".rjust(20), allScores)
print("Grade Average:".rjust(20), getAverages(allScores))
print("Lowest Grade:".rjust(20), getLowestGrade(allScores))
print("Highest Grade:".rjust(20), getHighestGrade(allScores))
gradeDistribution = getGradeDistributionDict(allScores)

print("Grade Distribution:".rjust(20), gradeDistribution)