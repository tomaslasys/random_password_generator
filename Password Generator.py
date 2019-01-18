
# coding: utf-8

# In[1]:


# Importing random package for later use
import pprint
import random
from random import *

# Creating strings that will be used for password generation
numbers = "0123456789"
lowletters = "qwertyuiopasdfghjklzxcvbnm"
capletters = lowletters.upper()
symbols = "!@#$%^&*+=-,./?_"
allchars = [numbers, lowletters, capletters, symbols]


# In[2]:


# Defining function for password length
def passLength():

    pass_length = 8
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


# In[3]:


# defining function for creating pasword from previously defined strings

def createPass(pass_length):
      
    password1 = ""
    i = 0

    while i < int(pass_length):
        x = choice(allchars)
        password1 += choice(x)
        i += 1
    return password1


# In[4]:


# Checking password strength.
# Pasword should include at least one number, one symbol, one upper case and one lower case letter.
# if criteria are not met function calls createPass function for a new password.

def testPass(pass_length):
    password2 = createPass(pass_length)
        
    j = 0
    
    for i in allchars:
        string1 = password2
        string2 = allchars[j]
        s1 = set(string1)
        s2 = set(string2)
        common_char = s1 & s2
        if len(common_char) == 0:
            password2 = createPass(pass_length)
            j = -1
        j += 1
    return password2


# In[5]:


# Demo users

users = {'jim': ',3,-X#1%4m1Rt!P0xx^_',
 'joe': 'hRL$-&18!!G7',
 'john': '^oAjJR^1g^D&F4',
 'mark': 'OU,n-3II',
 'tomas': '1234'}


# In[6]:


# Creating class user

class user:
    
    def __init__(self, username, pass_length):
        self.username = username
        self.pass_length = pass_length
        self.password = testPass(pass_length)
        print ("Your login name is:", username)
        print ("Your password is: ", self.password)
        users.update({self.username : self.password})


# In[7]:


# defining logIn function that asks for user details, checks if a user already exists, and, if not, creates a new user.

def logIn():
    user_name = input("Enter your username:")
    if users.get(user_name) == None:
        if user_name == "":
            print("Your imput is empty.")
            return
        print('User "' + user_name + '" does not exist')
        pass_length = passLength()
        print(pass_length)
        new_user = user(user_name, pass_length)
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


# In[8]:


# Operating part of code.

while True:
    logIn()
    user_name = input('Enter username username or press ENTER to exit.')
    if user_name == "":
        break

