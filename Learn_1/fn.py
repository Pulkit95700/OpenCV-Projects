# function is a block of code which is executed only when it is called

def hello(name, age = 10):
    print("Hello world " + name, str(age))

hello("Dude", 22)

def multipy(a, b):
    return a * b

print(multipy("hello", 3))

# keyword arguments in python

def fn(f_name, l_name, age):
    print("Hello", f_name, l_name, ", you are", age, "years old")

fn(age=4, f_name="Pulkit", l_name="Gupta")


# variable scope in python

# scope == The region that a variable is recognized. A variable is only variable from inside the region is created.
# A global variable and a locally scoped variable can be created as you know it.
# It is possible that you can make the same variables name inside the function.
# If that happens python will follow LEGB rule i.e Local Variable first, Enclosed Variable next, Global Variable next and the Built in variables.


# *args parameter in python
# this parameter will pack all the arguments passed into a tuple. useful so that function can accepts a varying amount of arguments
# args is just a name important is asterisk sign
# the only problem is that you can't change the values inside the tuple so you could not modify the tuple inside the function


def add(*args):
    return sum(args)

print(add(4, 5, 6, 10, 12))

# **kwargs parameter in python
# parameter that will pack all arguments into a dictionary useful so that a function can accept varying amount of keywords arguments

def hello(**kwargs):
    print("hello", kwargs["first"], kwargs["last"])

hello(first="Pulkit", last="Gupta")
# By default, every print statement in python runs every print line in a new line
print(1)
print(2)

# If you need to change it you have to use a second argument to print function that tells it to take the action at after whole thing is printed
print(1, end = " ")
print(2)

