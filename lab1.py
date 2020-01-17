#Question 1
array = [1, 3, 2, 10, 9, 5, 7, 4, 8]
print("The answers to Question 1 are: ")
for i in range (0, len(array)):
    print(array[i], end = ' ')
    print(i)
#Question 1
reverseArray = list(reversed(array))
print("The answer to Question 2: ")
print("Original array: " + str(array))
print("Reversed array: " + str(reverseArray))

#Question 3
def find2Smallest(a):
    if a[0]<a[1]:
        smallest=a[0]
        secondSmallest=a[1]
    else:
        smallest=a[1]
        secondSmallest = a[0]

    for i in range (2, len(a)-1):
        if a[i]<smallest:
            secondSmallest=smallest
            smallest=a[i]
        elif a[i]<secondSmallest:
            secondSmallest=a[i]

    return smallest, secondSmallest
print("The answer to Question 3: ")
print(find2Smallest(array))

#Question 4 -- RELOOK
"""""
integer = int(input("Enter an integer: "))
def insertToArray (a, value):
    tempArray = a
    tempArray.sort()
    if value>tempArray[0] or value<tempArray[len(a-1)]:
        for i in range(0, len(a) - 1):
            if (a[i] == value):
                break
            elif (a[i] - value == 1 or a[i] - value == -1):
                a.insert(i + 1, value)
                break
    elif value<tempArray[0] or value>tempArray[len(a-1)]:
        a.append(value)
    return a
print("The answer to Question 4: ")
print(insertToArray(array, integer))
"""

#Question 5
def findMaxNum (a):
    currentMax = a[0]
    for i in range (0, len(a)):
        if a[i]>currentMax:
            currentMax = a[i]
    return currentMax
print ("The max of the array is: " + str(findMaxNum(array)))

#Question 6
module = {
    "CSC1008": 70,
    "CSC1009": 80,
    "CSC2902": 85,
    "CSC1007": 45
}
studName = input("Name: ")
studNum = input("Student Number: ")
studMod, tempScore = input("Enter module code and score: ").split()
studScore = int(tempScore)
class Student:
    def __init__(self, name, number, completeMods):
        self.name = name
        self.number = number
        self.completeMods = completeMods
    def addScore(self, subjectCode, score):
        self.completeMods.update({subjectCode: score})
        print("The new list of completed modules are: " + str(self.completeMods))
    def printScores(self):
        print("Name of Student: " + self.name)
        print("Updated odules and scores are as follows: ")
        print(self.completeMods)
    def getBestScore (self):
        scores = list(self.completeMods.values())
        best = scores[0]
        for i in range (0, len(scores)):
            if scores[i] > best:
                best = scores[i]
        mod_list = list(self.completeMods.keys())
        bestMod = mod_list[scores.index(best)]
        print("Best module: " + bestMod, end='')
        print(" : " + str(best))
    def getFailedMods (self):
        scores = list(self.completeMods.values())
        failModule = {}
        for i in range (0, len(scores)):
            if scores[i] < 50:
                failScore = scores[i]
                mod_list = list(self.completeMods.keys())
                mod = mod_list[scores.index(failScore)]
                failModule.update({mod: failScore})
        print("Failed module(s) and score(s): " + str(failModule))
stud1 = Student(studName, studNum, module)  #create new student
stud1.addScore(studMod, studScore)  #add new module code and score
stud1.printScores() #print scores
stud1.getBestScore() #get best score and module code
stud1.getFailedMods() #get failed modules and score