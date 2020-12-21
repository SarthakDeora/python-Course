var1 = 65          # This is a integer
inpvar = input()   # This is how we take input, This means that whatever the user will type is going to store in the variable "inpvar"

# ? NOTE: The input will be stored as an string even if you type a number
# * And to prove that i will show you this:

print(type(inpvar))

# ? Now if we want to do some maths with the input we can't do it as you can see

# * It will just print it 10 times as usual but we wanted to multiply the number by 10 that the user typed
print(10*inpvar)

# ? Too Solve that problem we use this:

print(10 * int(inpvar))  # it workeds
