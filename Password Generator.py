
# coding: utf-8

# In[ ]:


import random
from random import *


numbers = "0123456789"
lowletters = "qwertyuiopasdfghjklzxcvbnm"
capletters = lowletters.upper()
symbols = "!@#$%^&*+=-,./?_"
allchars = [numbers, lowletters, capletters, symbols]


# In[ ]:


pass_length = 8

def passLength():

    pass_length = 0
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


# In[ ]:


def createPass():
      
    password1 = ""
    i = 0

    while i < int(pass_length):
        # print(password)
        x = choice(allchars)
        password1 += choice(x)
        # print(password)
        i += 1
    return password1


# In[ ]:


def testPass():
    password2 = createPass()
        
    j = 0
    
    for i in allchars:
        string1 = password2
        string2 = allchars[j]
        s1 = set(string1)
        s2 = set(string2)
        common_char = s1 & s2
        # print(len(common_char))
        if len(common_char) == 0:
            password2 = createPass()
            print(password2)
            # complexity(password)
            j = -1
        j += 1
    return password2


# In[ ]:


users = {"tom":"1234"}


# In[ ]:


class user:
    
    def __init__(self, username):
        self.username = username
        # self.password = generator()
        password = testPass()
        self.password = password
        print ("Your login name is:", username)
        print ("Your password is: ", password)
        users.update({self.username : self.password})


# In[ ]:


def logIn():
    user_name = input("Enter your user name:")
    if users.get(user_name) == None:
        if user_name == "":
            print("Your imput is empty.")
            return
        print('User "' + user_name + '" does not exist')
        pass_length = passLength()
        new_user = user(user_name)
    else:
        print("user already exists")
        i = 0
        while i < 3:
            password = input("Enter your password:")
            if password == users.get(user_name):
                print("You succesfully logged in")
                break

            i += 1
            if i == 3:
                print('User "' + user_name +'" has been blocked')
                break
            print("Your password is incorrect!")
            print("Please try again.")


# In[ ]:


while True:
    logIn()
    user_name = input('Enter username username or press ENTER to exit.')
    if username == "":
        break


# In[ ]:


import pprint
pprint.pprint(users)
input('press ENTER to exit.')

