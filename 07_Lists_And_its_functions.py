# ? This is how u can write a list
items = ["Candy", "corn Flakes", "Batter", "Atta"]

print(items.count("Candy"))  # ? We can also use some functions of string also

items.reverse()

print(items)  # ? And there are many others functions which are useless


items.append("lol")  # ! adds any desired element at the end
print(items)


items.remove("Candy")  # ! Removes any desired element
print(items)


items.pop()  # ! Removes the last element

print(items)


# * There are two types
# ? 1) Mutable    --> Can be changed  example: lists
# ? 2) Immuatable --> Cannot be changed example: tuple

tp = (34, 35, 6, 3465, 34, 634, 34634, 65)  # This is a normal tuple

#! And this is immutable so we cant change it by using insert remove append etc...


# to swap to variables we do:
a = 5
b = 6

# now to swap

a, b = b, a
print(a, b)
