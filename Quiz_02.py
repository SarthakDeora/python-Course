# So the question is to add some items in a list and print only NUMBERS not strings and the condition for the number is that it should be greater than 6.

list1 = [235445, "LOL", 754, 634, 6, 436, 34, 3, 2, 2, 2, 4, 5, 5, "lol"]

for numbers in list1:
    if str(numbers).isnumeric() and numbers > 6:
        print(numbers)
