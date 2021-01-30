number1 = input("Type your first number: \n")
number2 = input("Type your second number: \n")
# This helps in continuing the code even after an error and the error is stored as an string so that u can print the error.
try:
    print(int(number1)+int(number2))
except Exception as errormessage:
    print(errormessage)
print("Other code")
