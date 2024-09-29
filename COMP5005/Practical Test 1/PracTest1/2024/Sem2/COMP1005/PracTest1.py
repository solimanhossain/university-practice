"""
PracTest1.py: Read nunber of rows/cols and print an ASCII grid

Student Name : Zinat Tasnim
Student ID   : 0005
"""
numrows = 3
numcols = 3

# code error solve
# for row in range(numrows):
#     if row%2 == 0:
#         print("+|",end="")
# print()

# task 4-5
rows = int(input("Enter number of rows in grid..."))
while rows < 1 or rows > numrows:
    print("Out of range, please re-enter...")
    rows = int(input("Enter number of rows in grid..."))
cols = int(input("Enter number of columns in grid..."))
while cols < 1 or cols > numcols:
    print("Out of range, please re-enter...")
    cols = int(input("Enter number of columns in grid..."))

for row in range(rows):
    print("+---" * cols + "+")
    for col in range(cols):
        print("|   ",end="")
    print("|")
print("+---" * cols + "+")

# task 6-8
xinrow = int(input("Enter a row number..."))
while xinrow < 0 or xinrow > rows-1:
    print("Out of range, please re-enter...")
    xinrow = int(input("Enter a row number..."))
xincol = int(input("Enter a column number..."))
while xincol < 0 or xincol > cols-1:
    print("Out of range, please re-enter...")
    xincol = int(input("Enter a column number..."))

for row in range(rows):
    print("+---" * cols + "+")
    for col in range(cols):
        if row == xinrow and col == xincol:
            print("| X ",end="")
        else:
            print("|   ",end="")
    print("|")
print("+---" * cols + "+")
