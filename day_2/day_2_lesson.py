'''
Programming 102
Day 2 - Dictionaries
'''

'''
Dictionaries

- are one of the most powerful datatypes in Python
- can be used to store large amounts of data
- make working with data quick and easy
- are collections of key:value pairs

keys and values are separated with colons, key:value PAIRS
are separated with commas. Dictionaries are surrounded by curly brackets {}
'''

# blank dictionary
blank_dictionary = {}
# print(blank_dictionary, type(blank_dictionary)) # {} <class 'dict'>

example_dict = {'a':11, 'b':22, 'c':33}

example_dict = {
    # key: value,
    'a': 11,
    'b': 22,
    'c': 33
}

# keys should always be strings
# values can be ANY datatype, including other dictionaries

# dictionary values are accessed by placing their key in square brackets
# print(example_dict['a']) # 11
# print(example_dict['b']) # 22
# print(example_dict['c']) # 33

# cannot access values at keys that don't exist
# example_dict['d'] # KeyError: 'd'

vehicle = {
    'make': 'Dodge',
    'model': 'Dakota',
    'year': 2004,
    'features': ['2WD', 'Auto Windows', 'Auto Locks']
}

# print(vehicle['make']) # Dodge

# CAN add values at keys that don't exist yet
vehicle['color'] = 'beige'
# print(vehicle)

# change the value at a key
vehicle['year'] = 2020
# print(vehicle)

# since vehicle['features'] is a list, items can be appended to it
vehicle['features'].append('A/C')
# print(vehicle)

# delete a key:value pair with the keyword: del
# del vehicle['model']
# print(vehicle)

# -------------------------------------------------------- #

# Dictionary methods

# vehicle['for_sale'] # KeyError: 'for_sale'

'''
# look to see if this key exists
desired_key = 'for_sale'

# check if desired key is one of the keys
if desired_key in vehicle.keys():
    # if the key exists, get its value
    value = vehicle[desired_key]
else:
    value = f'Key doesn\'t exist: {desired_key}'

print(value)
'''

# .get() will do the same as lines 74-84
# .get(key, default) - return the value at the key, if it exists. Otherwise, return the default

desired_key = 'fish'
value = vehicle.get(desired_key, f'Key doesn\'t exist: {desired_key}')
# print(value)

# -------------------------------------------------------------------- #

# add multiple key:value pairs
# .update(dict) add the dictionary to the original dictionary
vehicle.update({
    'for_sale': True,
    'mileage': 120000
})

# print(vehicle)

# .pop(key) - remove the key:value pair at the key and return the value
removed_value = vehicle.pop('mileage')
# print(removed_value, vehicle)

# ---------------------------------------------------------------------- #

# Looping with dictionaries

# .keys(), .values(), .items()

# loop through dict keys
# print(vehicle.keys()) # dict_keys(['make', 'model', 'year', 'features', 'color', 'for_sale'])
for key in vehicle.keys():
    value = vehicle[key] # grab the value at the current key
    output = f'{key}: {value}'
    # print(output)


# loop through dict values
# print(vehicle.values()) # dict_values(['Dodge', 'Dakota', 2020, ['2WD', 'Auto Windows', 'Auto Locks', 'A/C'], 'beige', True])
for value in vehicle.values():
    output = f'value: {value}'
    # print(output)

# print(vehicle.items())
for item in vehicle.items():
    # use indices to pull out the key/value for each item
    key = item[0]
    value = item[1]

    output = f'{key}: {value}'
    # print(output)

# 'unpack' each item into TWO variables each loop
for key, value in vehicle.items():
    output = f'{key}: {value}'
    # print(output)

# 'unpacking' a list
nums = [33, 55, 77]

# assign each subsequent item to a different variable
a, b, c = nums

# print(a,b,c) # 33 55 77

# assign a,b,c to the same list
a = b = c = nums
# print(a, b, c)

# -------------------------------------------------- #

fruit_prices = {
    'tomato': .55,
    'pumpkin': 1.0,
    'bell pepper': .75
}

def is_valid_number(number):
    '''Return True if the number can be converted, False if not'''
    try:
        number = int(number)
        return True
    except ValueError:
        return False

while True:
    # ask the user which fruit they would like to buy
    fruit_name = input('Please enter the name of the fruit you\nwould like to buy or "done" to quit: ')

    # exit if 'done'
    if fruit_name == 'done':
        print('Goodbye')
        break

    # ensure the user has entered a valid fruit
    while fruit_name not in fruit_prices.keys():
        print(f'Invalid selection: {fruit_name}')
        fruit_name = input('Please enter the name of the fruit you would like: ')

    # use the user's input as the key to get the price
    price_per = fruit_prices[fruit_name]

    # ask how many the user wants
    quantity = input('Enter quantity: ')

    # use the is_valid_number() function to ensure the user enters a valid number
    while not is_valid_number(quantity):
        print('invalid number')
        quantity = input('Enter quantity: ')

    # convert quantity to integer
    quantity = int(quantity)

    # calculate the total
    total = quantity * price_per

    print(f'{quantity} {fruit_name}s @ {price_per} each - ${total}')