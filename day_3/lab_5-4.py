# Richard Farr
# PDX Code Guild 
# Day 3 - Lab 5
# 12/30/2020

# Final Project - 'Log in"

'''
Create a REPL which allows a user to 'log in'.

Please complete the sections in order. Create a working version of 5.1 before attempting 5.2, etc. 
This will make your life easier. You may also want to consider creating separate .py files for each version, 
so you can refer back to previous working versions.
'''

'''
5.1
Create a dictionary called profile

The profile should contain two key : value pairs with keys of username and password and values of your choosing. 
They will represent a username and password for a single user.

username - gandalfTheGrey
password - noneShallPass!
Do not create your profile with the user's username as the key and their password as the value as below:

'gandalfTheGrey':'noneShallPass'
'''

profile_1 = {
    'username': 'Richard',
    'password': 'Farr'
}

profile_2 = {
    'username': 'Mike',
    'password': 'Jones'
}

profiles = [profile_1, profile_2]


'''
Define a function called login() which will have parameters for:

username_attempt
password_attempt

The login() function will return True if the values passed to the function for username_attempt and 
password_attempt match the values at the keys of username and password found in the profile.

If the credentials don't match those in the profile, the login() function will return False

Create variables for a username_attempt and password_attempt which will emulate a user's login attempt.

Pass the username_attempt and password_attempt to login() and tell the user whether their login attempt was successful.
'''

# print(profile.keys())

'''
def login(username_attempt, password_attempt):
    if username_attempt in profile.keys() and password_attempt == profile[username_attempt]:
        print("Good, your login was successful")
        return True
    else:
        print("Sorry, at least one of those was incorrect")
        return False

username = input("What's your username? ")
password = input("What's your password? ")

login(username, password)
'''


'''
Output:

profile:
    username: gandalfTheGrey
    password: noneShallPass!


# successful login
username: gandalfTheGrey
password: noneShallPass!

Welcome, gandalfTheGrey!

# unsuccessful login
username: gandalfTheGrey
password: myPrecious?

Error! Your username or password was incorrect!
'''


'''
5.2
Create a REPL that asks the user for their username and password and attempts to log them in.

If their login is successful, print a welcome message and end the program.

If their login is unsuccessful, ask if they'd like to try again.
'''



def login(username_attempt, password_attempt):
    count = 0
    for profile in profiles:
        if (username_attempt == profile['username'] and password_attempt == profile['password']):
            count = count + 1

    if count >= 1:
        return True  
    else:
        return False
            


login_attempts = 0

# REPL
while login_attempts < 3:
    username = input("What's your username? ")
    password = input("What's your password? ")
    if login(username, password):
        print("Good, your login was successful")
        break
    else: 
        print("Sorry, at least one of those was incorrect")
        login_attempts = login_attempts + 1 
        try_again = input("Would you like to try to login again? (Y/N) ")
        if try_again == "N":
            print("OK, bye")
            break   
else:
    print("Sorry, 3 failed login attempts is enough for one day. Try again tomorrow. bye.")


'''


'''
'''
5.3
Allow the user three attempts to login. If they exceed three attempts without a successful login, tell the user and end the program

Output:

username: gandalfTheGrey
password: myPrecious?

Error! Your username or password was incorrect!

Enter 'y' to try again, 'n' to quit: y

You have 2 login attempt(s) remaining...

username: gandalfTheGrey
password: foolOfATook!

Error! Your username or password was incorrect!

Enter 'y' to try again, 'n' to quit: y

You have 1 login attempt(s) remaining...

username: gandalfTheGrey
password: bilboBaggins!

Error! Your username or password was incorrect!

Your login has been unsuccessful three times! Try again later. Goodbye!





5.4
Add support for multiple users.

A few things will need to change:

Instead of one profile, you will need a list of profiles. Each profile be a dictionary containing key : value pairs 
with the keys of username and password.

The login() function will require a third parameter, profile.

When the user enters their username and password attempts, loop through the list of profiles, pass each profile 
one at time into the login() function along with the username_attempt and password_attempt.

If the username_attempt and password_attempt match the values at the keys of username and password current profile, 
the login() function will return that True and that user will be logged in. Otherwise, it will return False.





5.5 - Advanced
Define a function called create_user() which:

prompts the user for a username and password.
checks to see if the username already exists in the profiles list using the user_exists() function
If the username is unique and doesn't appear in the profiles list, .append() it to the profiles list.
Define a function called user_exists() which will:

loop through each profile in the profiles list
check to see if the username the user entered already exists within one of the profile dictionaries.
If a user with that username already exists, return True, otherwise return False

Integrate the create_user() function into your REPL to allow the user to create a new username.

Profiles list:

username: gandalfTheGrey
password: noneShallPass!

username: bilboBaggins
password: theShire123

username: iAmSmeagol
password: myPrecious!
Output:

Welcome!

Please select from the following options:

    1. Create user
    2. Login

Enter the number of your choice: 1

Create User
-----------
    Enter your new username: gandalfTheGrey

    That username already exists!

    Enter your new username:
    mrSamwise

    Enter your password:
    frodoIsMyFriend

Thanks for signing up, mrSamwise!

Please select from the following options:

1. Create user
2. Login

Enter the number of your choice: 2

Login:
------

    username: smaugTheDragon
    password: gimmeYerGold!

    Error! Your username or password was incorrect!

Enter 'y' to try again, 'n' to quit: y

You have 2 login attempt(s) remaining...

    username: iAmSmeagol
    password: myPrecious!

Welcome, iAmSmeagol!
'''