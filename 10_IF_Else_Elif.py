print("Hello guys my name is Sarthak deora")  # Normal printing.
var1 = 12   # A variable.
var2 = 56  # Also a variable.
var3 = int(input())     # Also a variable he user have to type its value.


if var3 > var1:  # This is how if statement is created, and that collan is important make sure to put it.
    # Don't forget to add 4 spaces or a tab in the starting before the code.
    print("Yuor number is Greater than 12!!")
else:
    # Don't forget to add 4 spaces or a tab in the starting before the code.
    print("Your number is lesser than 12")

    # Now if I type exactly 12 in the input it will show lesser but we want it to say equal so to do that we have a synatx "Elif"


if var3 > var2:  # normal if statement
    print("Your number is bigger than 56, Congrats!!!")
elif var3 == var2:  # If we want to addmore conditions than 1 we use this statement
    print("Your number is equal to 56,Congrats!!!")
else:  # normal else statement
    print("Your number is lesser than 56,Congrats!!!")

    # We can check and make if sstaements by the content of a list too!!!! lets see it
    list = [34, 435, 3445, 345, 34, 5]  # I made a normal list
    if 34 in list:  # this is how u do it
        print("34 is in the list")
    else:
        print("34 is not in the list")
