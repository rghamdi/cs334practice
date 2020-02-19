firstNum = int(input("Enter first number: "))
secNum = int(input("Enter second number: "))

def isGreater(firstNumber, secondNumber):
    if firstNumber > secondNumber:
        print("First number is greater than the second")
    else:
        print("Second number is greater than the first")


def isLesser(firstNumber, secondNumber):
    if firstNumber < secondNumber:
        print("First number is less than the second")
    else:
        print("Second number is less than the first")

def isequal(firstNumber, secondNumber):
    if firstNumber == secondNumber:
        print("First and second number are equal")


isGreater(firstNum, secNum)
isLesser(firstNum, secNum)
isequal(firstNum, secNum)
