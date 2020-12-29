# Richard Farr
# PDX Code Guild 
# Day 2 - Lab 2
# 12/29/2020

# Lab 3: Unit Converter
# This lab will involve writing a program that allows the user to convert a number between units.

# Each version should be accomplished using a dictionary and each can be completed without the use of if/elif statements.


# 1. Create a dictionary that I can reference to do the conversions

conversion = {

    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'inch': 0.0254
    }



# 2. Ask the user for inputs

user_input_distance = int(input("what is the distance to convert to meters? <enter a number> "))
#print(user_input_distance)

user_input_units = input("what are the units to convert from? <enter ft, mi, m, km, yard, inch> ")
#print(user_input_units)




# 3. Do the calculations and display the output

if user_input_units in conversion.keys(): # ["ft", "mi", "m", "km", "yard", "inch"]:
    output = round(user_input_distance * conversion[user_input_units], 4)
else:
    output = "an unknown measure of distance and can not be converted to"


print(f"{user_input_distance} {user_input_units} is {output} meters.")
