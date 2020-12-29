# Richard Farr
# December 28th, 2020
# PDX Code - 102 - Day 1 - Lab 2

'''> what is the operation you would like to perform? +
> what is the first number? 5
> what is the second number? 7
> 5 + 7 = 12
> what is the operation you would like to perform? done
> goodbye
'''

# Define the functions to be used
def add(num1, num2):
    total = num1 + num2
    return total

def subtract(num1, num2):
    total = num1 - num2
    return total

def multiply(num1, num2):
    total = num1 * num2
    return total

def divide(num1, num2):
    total = num1 / num2
    return total


# Define the questions to be asked
def question_operation():
    operation = input("what is the operation you would like to perform? (choose + or - or * or / or done to quit) ") 
    return operation

def question1():
    return float(input("what is the first number? "))

def question2():
    return float(input("what is the second number? "))


# Define output
# output = f"{number1} {operation} {number2} = {result} "

while True:
    operation = question_operation()

    if operation != "done":
        number1 = question1()
        number2 = question2()
        if operation not in ["+", "-", "*", "/"]:
            print("thats not a supported operation at this time")
            continue
        elif operation == "+":
            result = add(number1, number2)
            print(f"{number1} {operation} {number2} = {result} ")
        elif operation == "-":
            result = subtract(number1, number2)
            print(f"{number1} {operation} {number2} = {result} ")
        elif operation == "*":
            result = multiply(number1, number2)
            print(f"{number1} {operation} {number2} = {result} ")
        elif operation == "/":
            result = divide(number1, number2)
            print(f"{number1} {operation} {number2} = {result} ")
        else:
            print("this should never be printed - some mistake happened")
            
    else:
        print("goodbye")
        break


