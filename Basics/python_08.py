# try except similar version of try catch error of js

# number= int((input("enter a number")))
# print(number)

# if the user input anything other than number the program will just stop and throw error in terminal
# in order to avoid this we use this funcitonality of try except

try:
    number= int((input("enter a number")))
    print(number)   
except:
    print("enter only number")

# we can write multiple except for multiple error we can catch specific type fo error and we can store it in varibale

try:
    # ans=10/0
    number= int((input("enter a number")))
    print(number)   
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)