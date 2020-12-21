dict1 = {"immutable": "Cannot Change",
         "mutable": "Can Change",
         "earphone": "An object to hear sounds",
         "programing": "To talk to the computer and give it some commands",
         "sarthak": "Meaningfull",
         "dhruv": "It is a Star"}

print("Hello! I am your Dictionary Type the word:")
input1 = input()
print("The meaning of", input1 + " is", dict1[input1])
