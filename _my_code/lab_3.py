# Richard Farr
# December 11th, 2020
# PDX Code Guild
# Programming 102
# Lab 3

'''
Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters. 
Hint: 1 ft is 0.3048 m. 
So we can get the output in meters by multiplying the input distance by 0.3048. 
Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m


Version 2
Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
'''
def main():

    conversion = {
        'ft': 0.3048,
        'mi': 1609.34,
        'm': 1,
        'km': 1000,
        'yard': 0.9144,
        'inch': 0.0254
    }


    user_input_distance = int(input("what is the distance to convert? "))
    # print(user_input_distance)

    user_input_units = input("what are the units? (choose ft, mi, m, km, yard, inch) ")
    # print(user_input_units)

    if user_input_units in conversion.keys(): # ["ft", "mi", "m", "km"]:
        output = round(user_input_distance * conversion[user_input_units], 4)
    else:
        output = "an unknown measure of distance and can not be converted to"


    print(f"{user_input_distance} {user_input_units} is {output} meters.")


main()






'''
    if user_input_units == "ft":
        output = round(user_input_distance * conversion['ft'], 4)
    elif user_input_units == "mi":
        output = round(user_input_distance * conversion['mi'], 4)
    elif user_input_units == "m":
        output = round(user_input_distance * conversion['m'], 4)
    elif user_input_units == "km":
        output = round(user_input_distance * conversion['km'], 4)
    else:
        output = "an unknown measure of distance and can not be converted to"
'''