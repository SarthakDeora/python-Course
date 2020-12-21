d2 = {"Sarthak": "full",  # ? This is how we make a dictionary by using curly brackets
      "Dhruv": "Half",
      "Mammi": "Sabh"}

print(d2["Mammi"])  # Here I said python to tell about mammi

#! To add more in the dictionary we do this

d2["Pooty"] = "Goo Khale"

print(d2)

del d2["Pooty"]
print(d2)


print(d2.copy())  # * This will make a new copy of d2 and print that for you
            