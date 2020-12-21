# # Exercise 2-------->  To make a falty calculator which will give all the correct answers Except the following-->  45*3=555, 56+9=77, 56/6=4

print("Hello I am your Calculator!!")
number1 = int(input("Type your 1st number: "))
operator = input("Type your operator: ")
number2 = int(input("Type your 2nd number: "))

if number1 == 45 and number2 == 3 and operator == "*":
    print(555)
elif number1 == 56 and number2 == 9 and operator == "+":
    print(77)
elif number1 == 56 and number2 == 6 and operator == "/":
    print(4)
else:
    if operator == "*" or operator == "multiply":
        print(number1*number2)
    elif operator == "+" or operator == "plus":
        print(number2+number1)
    elif operator == "/" or operator == "divide":
        print(number1+number2)
    elif operator == "-" or operator == "minus":
        print(number1-number2)
        # And done
