# NOw this variable will have the file opened but will not print anything.
file1 = open("Example for part 17.txt")
# But this variable will have the content of the file.
content_of_file1 = file1.read()
# and now if printed the second variable we will get the content.
print(content_of_file1)

file1.close()  # very important pleaseeeee always close the file after opening.

# If i will print just the first 3 letters of the file and then again do it then i will get the 4th 5th and 6th letter as 1st 3 have already been printed.
file2 = open("Example-2 for part 17.txt")

for i in file2:
    print(i)      # now this has printed each line line by line.

    # noe to print onlya a single line at a time we us ethis function named redline
file2.close()
f = open("Example-2 for part 17.txt")
print(f.readline())  # this printed the first line of the text.
print(f.readline())  # this printed the second line of the text.
print(f.readline())  # This line printed the third line of the text.
# This function will give you a list in which every line is there seperated.
print(f.readlines())
