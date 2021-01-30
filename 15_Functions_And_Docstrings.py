# Listen this is gonna be realy realy difficult

# So be focused ok?

# oo lets begin

# There are 2 types of Functions

# User defined functions:-
num1 = int(input("Type a number"))
num2 = int(input("Type the second number"))


def function1(a, b):
    print("Hi guys my name is Sarthak Deora")
    average = (a+b)/2
    sum1 = a+b


print(function1(2, 6))
# Now if we will print functions It will print "None" in the terminal at the end of the functions so to prevent that we can simply do this


def function2(a, b ):
    print("Hi guys my name is Sarthak Deora")
    average = (a+b)/2
    sum1 = a+b
    return average


# Now what this will do is "v" will contain the return value of function1
v = function2(num1, num2)
print(v)

# NOw we will learn about docstrings


def docstrings():
    """This function prints the average of variable [x] and  variable [y]"""


# This is how you print docstrings to know that what does the function does, this helps in Knowing what the function does when there are lot of functions.
print(docstrings.__doc__)
