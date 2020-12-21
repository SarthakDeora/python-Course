num1 = "23"  # This is a variable conataining a STRING which is "23"
num2 = "7"   # This is a variable conataining a STRING which is "7"
# So a normal person will expect the output to be 30 but its not because num1 and num2 are nothing but strings that's why python is taking it like sentence.
print(num1 + num2)

# To prove that num1 and num2 are strings we can do:

print(type(num1))
print(type(num2))

# But there is a way to convert a tring, integer or a float to any other type of variable
# This is how you do it:

# now this command has converted num1 and num2 to integers which were trings intially but they are integers for this line only it will be string as default as we have put double inverted commas.
print(int(num1) + int(num2))
