"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



# Replace this with your code

#repeat forever:
while True:
#    read input
    user_input = input("Please enter an equation :) >")
#    tokenize input
    tokenize = user_input.split(" ")
#        if the first token is "q":
        if "q" in tokenize:
            print("That was fun, see ya later!")
            break
#            quit
#            (decide which math function to call based on first token)
            
#           if the first token is 'pow':
#                  call the power function with the other two tokens#

