# import re 
# def ValidateInput(regex):
#     userInput = input("enter \n")
#     regex = r'' + regex
#     while not(bool((re.match(regex, userInput)))):
#         userInput = input("plaease enter a valid input")
#     print (userInput)
#     return userInput

# ValidateInput("^[a-zA-Z0-9]+@(gmail|outlook)\.com$")

from functions import*

loadUser()
register()

