print("message")
print('It is really good')

# variables are containers to store values. Behaves as the value after they are assigned

first_name = "Pulkit"
last_name = "Gupta"

# use to print the data type of a variable
print(type(first_name))

print(first_name + " " + last_name)

# age variable is int data type
# age = 21
# print(age)
# age += 1
# print(age)
# print(type(age))

# you cannot add a int data type to a string data type
# print("Your age is " + age)
# Traceback (most recent call last):
#   File "D:\python\Learn_1\main.py", line 22, in <module>
#     print("Your age is " + age)
#           ~~~~~~~~~~~~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str

# We have to typecast the variable first to a string data type
# print("Your age is " + str(age))

height = 250.5
print(height)
print(type(height))

# you can also typecast your floating point number
print("Your height is " + str(height))

# (this is another way to use print statement for the same task)
print("Your height is", height)

# Boolean variable
human = True
print(human)
print(type(human))

print("Are you a human: " + str(human))

# multiple assignment in python allows to assign value to multiple variables at the same time in one line of code
#
# name = "Bro"
# age = 21
# attractive = True

# it is same as
# name, age, attractive = "Bro", 21, True

# Spongebob = Pattrick = Sandy = Squilward = 30

# print(Spongebob)


name1 = "Pulkit"

print(len(name1))
# finds the first character in python
print(name1.find("P"))
print(name1.lower())
print(name1.upper())
print(name1.isdigit())
print(name1.isalpha())
print(name1.isalnum())
print(name1.replace("P", "a"))
print(name1.count("P"))
# prints the name 3 times
print(name1*3)

# typecasting is same as very easy in python just cover anything with the open parenthesis
name1 = "pul"
# print(int(name1))
# Traceback (most recent call last):
#   File "D:\python\Learn_1\main.py", line 81, in <module>
#     print(int(name1))
#           ^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'pul'

# we can expect some user input in python
x = input("What is your name?: ")
age = int(input("What is your age bro?: "))

print(x, age)