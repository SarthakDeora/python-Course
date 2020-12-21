string1 = "My name is Sarthak Deora"


print(string1)  # ? Her i Just printed the the variable string1


# ?So this is how you can print a specific digit but python doesnt start counting from1 it starts counting from 0
print(string1[7])


print(string1[0:7])  # ? So this will help us by printing from a desired plsce to a desired place but remember the number which is before ":" this is including but the number which is after it iis not included like if it is 5 it will tkae it as 4


print(len(string1))  # ? This will print the length of the string


# ?  If i will leave them empty it will take the first digit as zero only and the second digit as its length as default
print(string1[:])


# ? Now the third one will decide that how much letters will you skip like write now its 2 so it will print every second letter from 0 to 24.
print(string1[0:24:2])

# ? Again if we left it empty it will take it as 1s
print(string1[::])


# ? - numbers will make python to count from the end
print(string1[-1:-7])


# ? And negative third number will print the string revered and then count
print(string1[-1:-7:-1])


# ? This will tell us wether the string is alphanumberic or not
print(string1.isalnum())

# * Alphanumeric --> String containing (a-z) and (0-9) no space or any other charecters

# ? This will tell you that wether the given number is alpha or not
print(string1.isalpha())

# * Alpha --> String containing (a-z) only nothing else


# ? This will tell wether the string is ending with the given string or integer or float
print(string1.endswith("Deora"))


# ? This will count how thr given string and tell how many are there
print(string1.count("D"))


# ? This will replace the first one with the second one
print(string1.replace("is", "was"))
4

print(string1.capitalize())  # ? This will capitalize the first letter


print(string1.upper())  # ? obviously will make every letter Capital


print(string1.lower())  # ? obviously will make every letter LowerCase
