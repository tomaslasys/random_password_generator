
# coding: utf-8

import string
import pprint
from random import choice

# Creating strings that will be used for password generation
NUMBERS = string.digits
LOWLETTERS = string.ascii_lowercase
CAPLETTERS = string.ascii_uppercase
SYMBOLS = "!@#$%^&*+=-,./?_"
allchars = [NUMBERS, LOWLETTERS, CAPLETTERS, SYMBOLS]


# Defining function for password length
def password_length():

    print("Choose password length.")
    print("Password length should be 8 to 32 elements")

    while True:
        pass_length = input('Please enter desired password length in numbers:')
        if pass_length.isnumeric():

            if int(pass_length) < 8:
                print("Your chosen password length is too short.\nPlease choose another value.")
            elif int(pass_length) > 32:
                print("Your chosen password length is too long.\nPlease choose another value.")
            else:
                # print("Your password length will be ", password_length)
                return int(pass_length)
        else:
            print("You entered invalid characters!")


# defining function for creating pasword from previously defined strings

def create_password(pass_length):
      
    password1 = ""
    i = 0

    while i < int(pass_length):
        x = choice(allchars)
        password1 += choice(x)
        i += 1
    return password1



# Checking password strength.
# Pasword should include at least one number, one symbol, one upper case and one lower case letter.
# if criteria are not met function calls createPass function for a new password.

def test_password(pass_length):
    password2 = create_password(pass_length)
        
    j = 0
    
    for i in allchars:
        string1 = password2
        string2 = allchars[j]
        s1 = set(string1)
        s2 = set(string2)
        common_char = s1 & s2
        if len(common_char) == 0:
            password2 = create_password(pass_length)
            j = -1
        j += 1
    return password2


# Demo users

users = {'jim': ',3,-X#1%4m1Rt!P0xx^_',
 'joe': 'hRL$-&18!!G7',
 'john': '^oAjJR^1g^D&F4',
 'mark': 'OU,n-3II',
 'tomas': '1234'}


# Creating class user

class User:
    
    def __init__(self, username, pass_length):
        self.username = username
        self.pass_length = pass_length
        self.password = test_password(pass_length)
        print ("Your login name is:", username)
        print ("Your password is: ", self.password)
        users.update({self.username : self.password})


# defining logIn function that asks for user details, checks if a user already exists, and, if not, creates a new user.

def log_in():
    user_name = input("Enter your username:")
    if users.get(user_name) == None:
        if user_name == "":
            print("Your imput is empty.")
            return
        print('User "' + user_name + '" does not exist')
        pass_length = password_length()
        print(pass_length)
        new_user = User(user_name, pass_length)
    else:
        print("user already exists")
        i = 0
        while i < 3:
            password = input("Enter your password:")
            if password == users.get(user_name):
                print("You succesfully logged in")
                pprint.pprint(users)
                break

            i += 1
            if i == 3:
                print('User "' + user_name +'" has been blocked')
                break
            print("Your password is incorrect!")
            print("Please try again.")


# Operating part of code.

while True:
    log_in()
    user_name = input('Press ANY BUTTON and ENTER to continue or press ENTER to exit.')
    if user_name == "":
        break

