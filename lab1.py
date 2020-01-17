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

#Question 5
