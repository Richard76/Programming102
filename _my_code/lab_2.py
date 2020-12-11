# Richard Farr
# December 11th, 2020
# PDX Code Guild
# Programming 102
# Lab 2

'''
Problem to Solve
================
> what is the operation you would like to perform? +
> what is the first number? 5
> what is the second number? 7
> 5 + 7 = 12
> what is the operation you would like to perform? done
> goodbye
'''

def question1():
    return float(input("what is the first number? "))

def question2():
    return float(input("what is the second number? "))

def add(num1, num2):
    total = num1 + num2
    return total

def subtract(num1, num2):
    total = num1 - num2
    return total


while True:
    print(" ") # start off with an empty line
    operation = input("what is the operation you would like to perform? (choose + or - or done to quit) ")

    if operation != "done":
        number1 = question1()
        number2 = question2()
        if operation == "+":
            result = add(number1, number2)
            print(f"{number1} {operation} {number2} = {result} ")
        elif operation == "-":
            result = subtract(number1, number2)
            print(f"{number1} {operation} {number2} = {result} ")
        else:
            print("thats not a supported operation at this time")
            
    else:
        print("goodbye")
        break


