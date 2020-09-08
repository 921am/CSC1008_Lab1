#Question 1
def reverse():
    chara = input("Input characters: ")
    if (chara != 'end'):
        reverse()
    print(chara)
reverse()

#Question 3
def sum(n):
    i = 1
    s = 0.0

    for i in range(i, n+1):
        if (i == 1):
            s = i
        elif (i%2 == 0):
            s = s + (1 / i)
        else:
            s = s - (1 / i)
    return s
num = int(input("Enter n value: "))
print("The answer for Q2: ")
print(sum(num))

#Question 4
def gcd(n,m):
    if (m != 0):
        return gcd(m, n%m)
    else:
        return n
n =int(input("Please enter n value: "))
m =int(input("Please enter m value: "))
print("The answer for Q3 is: ")
print(gcd(n,m))

