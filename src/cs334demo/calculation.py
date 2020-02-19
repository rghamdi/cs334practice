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

def isDouble(firstNumber,secondNumber):
    if firstNumber * 2 == secondNumber:
        print("Second number is double of first")
    else:
        print("Second number is not double of first")

isGreater(firstNum, secNum)
isLesser(firstNum, secNum)
isequal(firstNum, secNum)
isDouble(firstNum, secNum)
