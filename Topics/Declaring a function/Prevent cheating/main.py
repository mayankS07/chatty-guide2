import math


# your code here

def print_message(x):
    x = "Don't cheat!"
    return print(x)


math.factorial = print_message

# don't delete this line, please
c = 23
math.factorial(c)
