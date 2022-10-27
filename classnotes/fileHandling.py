import os

# writing in file
newFile = open("newFile.txt","r")

newFile.seek(10)
print(newFile.read())
print(newFile.tell())

# to print file mode
# print(newFile.mode)
# print(newFile.name)

# for i in range(0,10):
#     newFile.write("\nHello, welcome to Python:")

# reading in file

# newFile = open("newFile.txt","r")

# for i in range(0,10):
#     print(newFile.read())

# rename a file

# os.rename('newFile.txt','changedName.txt')

# delete a file
# os.remove("changedName.txt")