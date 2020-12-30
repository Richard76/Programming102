'''
Programming 102
Day 1 Review
'''

'''
Anatomy of an Error Message

File <FILENAME>.py, line number, in <MODULE_NAME>
    troublesome code (approximate)
                   ^
ErrorType: specific error message
'''

# cascading error message using random module
import random
"""
random.choice(123)

"""

# SyntaxError - something is mistyped
# 4 + # SyntaxError: invalid syntax
# print('hello) # SyntaxError: EOL (end of line) while scanning string literal
# print('hello'
# x = 2 # SyntaxError: invalid syntax


# IndentationError - horizontal placement is off
x = 4
"""
if x == 4:
    print('hello')
     print('hi') # IndentationError: unexpected indent (too far right)
   print('howdy') # IndentationError: unindent does not match any outer indentation level (too far left)
"""

for x in range(10): 
    # blank code blocks will cause the following error
    pass # use this if you want to define a blank code block

x = 1 # IndentationError: expected an indented block

# ----------------------------------------------------------- #


# NameError - a variable or function name was used that doesn't exist
# a = b + c # NameError: name 'b' is not defined
# imaginary_function() # NameError: name 'imaginary_function' is not defined

# ----------------------------------------------------------- #

# TypeError - wrong datatype was used for an operation
# print('5' + 5) # TypeError: can only concatenate str (not "int") to str
colors = ['red', 'green']
# colors() # TypeError: 'list' object is not callable
# 100[0] # TypeError: 'int' object is not subscriptable

# ----------------------------------------------------------- #

# IndexError - index doesn't exist in a sequence
# colors[3] # IndexError: list index out of range
letters = 'abc'
# letters[10] # IndexError: string index out of range

# ----------------------------------------------------------- #

# AttributeError - variable or function or method doesn't belong to an object
# random.fish() # AttributeError: module 'random' has no attribute 'fish'
# 'hello'.append('a') # AttributeError: 'str' object has no attribute 'append'
# ['a', 'b', 'c'].capitalize() # AttributeError: 'list' object has no attribute 'capitalize'

# ------------------------------------------------------------ #

# ModuleNotFoundError - trying to import a module that doesn't exist
# import imaginary_module # ModuleNotFoundError: No module named 'imaginary_module'

# ------------------------------------------------------------ #

# ImportError - Importing from a parent directory without proper module setup
# from .. import imaginary_module  # ImportError: attempted relative import with no known parent package

# ------------------------------------------------------------ #

# ZeroDivisionError - dividing by 0
# 1 / 0 # ZeroDivisionError: division by zero

# ------------------------------------------------------------ #

# ValueError - Improper value passed to a function
# float('#$%^&') # ValueError: could not convert string to float: '#$%^&'
# int('$%^&') # ValueError: invalid literal for int() with base 10: '$%^&'

# -------------------------------------------------------------- #

# Handling Errors
# keyword: try / except / else / finally

'''
try:
    # try to run this code
    number = input('Please enter a number: ')
    number = float(number)

except ValueError:
    # if the code in the try block raises a ValueError
    # run this block instead of breaking the code
    print(f'Could not convert "{number}" to float')

else:
    # run this block if no error was raised in the try block
    print(f'Converted "{number}" to float')

finally:
    # this will run whether there was an error or not
    print('Yay, Python!')
'''

'''
numerator = 100

while True:
    try:
        denominator = input('Please enter a number by which to divide: ')

        # convert the number to a float
        denominator = float(denominator)

        # divide the numbers
        quotient = numerator / denominator

    except ValueError:
        print('Invalid entry please try again.')

    except ZeroDivisionError:
        print('Cannot divide by zero!!!')

    else:
        print(f'{numerator} / {denominator} = {quotient}')
        break

'''

'''
# raise your own error
# keyword raise

try:
    color = 'green' # imagine this was from an input()
    if color == 'green':
        # raise a ValueError with a custom message
        raise ValueError(f'Green is not a valid color!') 

# catch the ValueError and store the message in a variable called 'error'
except ValueError as error:
    print(error)
'''

# ------------------------------------------------------------------------- #

# REPL

'''
R ead
E valuate
P rint
L oop
'''


'''
while True:
    again = input('Do you want to play again? yes/no: ')

    if again == 'no':
        break
'''

'''
colors = []

while True:
    # ask the user for a color
    color = input('Please enter a color or "done" to quit: ')

    # check if the user has entered 'done'
    if color == 'done':
        print(f'These were the colors you entered: {colors}')
        break

    # ensure the use hasn't entered a duplicate
    # if the user's color is already in the list
    while color in colors:
        print('Sorry, no duplicates allowed.')
        color = input('Please enter a color: ')

    # add the user's color to the list
    colors.append(color)
'''

# ------------------------------------------------------ #

# Functions

# Functions are named blocks of code that run only when called
# Data is passed to function to be manipulated and the manipulated
# data is returned to where the function was called

def absolute_value(number):
    # if the number is negative, flip it positive
    if number < 0:
        number *= -1

    return number

# print(absolute_value(-99)) # -99 is an argument that will fill the number parameter
# print(absolute_value(5))
'''
nums = [-5, -87, -99]

for num in nums:
    print(absolute_value(num))
    
'''

def power_n(number=3, n=2):
    '''
    DOCSTRING - Allow documentation to be added to a function

    Return the number raised to the power of n
    '''
    return number ** n

# print(power_n(100)) # this will use the default value for n if it exists, otherwise it will break
# print(power_n()) # use both default values
# print(power_n(4)) # use 4 as number
# print(power_n(n=4)) # use 4 as n
# print(power_n(n=4, number=10))

# ----------------------------------------------------- #
'''
# *args (arguments)/ **kwargs (keyword arguments)
def show_args_kwargs(*args, **kwargs):
    print(args)

    for arg in args:
        print(arg)

    print(kwargs)

show_args_kwargs(3.14, True, 'cat', word1 = 'fish', word2='dog', word3 = 'banana')
'''

# add up any arbitrary number of numbers
def add_em_up(*nums):
    '''Return the sum of any arbitrary number of numbers'''
    total = 0

    # loop through the numbers and add them to total
    for num in nums:
        total += num

    return total

# print(add_em_up(56,46,36,72,29,46,56,46,36,72,29,46))

# ------------------------------------------------------ #

# SCOPE - the 'bubble' in which a variable exists

# anything defined all the way left is in the 'global' scope
'''
y = 5 # since y and add are in the same scope, y is available inside add()

def add(a, b):

    print(y)
    # total only exists inside this function
    total = a + b

    return a + b

add(1,2)

def main():
    # main function contains the body of the program
    pass
'''