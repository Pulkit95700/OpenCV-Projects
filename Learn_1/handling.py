# file handling in python
import os
import shutil

path = "C:\\Users"

if(os.path.exists(path)):
    print("That location exists!")
    if(os.path.isfile(path)):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a dir")
else:
    print("That does not exists")

source = " "
destination = " "

# excption handling in python is every simple

# try:
#     a = int(input())
#     b = int(input())
#
#     div = a / b
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print("done computing")
# finally:
#     print("I will always be called")

# moving a file or directory inside

source = "test.txt"
destination = "folder\\x.txt"

# try:
#     if(os.path.exists(destination)):
#         print("there is already a folder there")
#     else:
#         os.replace(source, destination)
#         print(source + " was moved")
# except FileNotFoundError as e:
#     print(e)

path = 'folder\\p.txt'
try:
    os.remove(path)
except FileNotFoundError as e:
    print("That file was not found")
except PermissionError as e:
    print("you do not have permission to remove that file")


# to remove a directory we use following 3 methods
# os.remove(path) 
# os.rmdir(path)
# shutil.rmtree(path)