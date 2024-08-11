# str.format() = optional method that gives users more control while displaying the output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item)) # It works as a positional index, you can also give 2 and 3 and so on indexes.

# you can also use the format method as keyword pairs with this you can use the same variable twice anywhere in the string
print("The {a} jumped over the {b}".format(a=item, b=item))

# we can also store the string in a variable and then use the format method in that variable
text = "The {} jumped over the {}"
print(text.format("cow", "moon"))

# we can also many things using format field
pi = 3.14579
print("The number is {:.2f}".format(pi))

n = 1000


print("The number is {:b}".format(n)) # This converts the number in binary format
print("The number is {:o}".format(n)) # This converts the number in octal format
print("The number is {:X}".format(n)) # This converts the number in hexadecimal format
print("The number is {:E}".format(n)) # This converts the number in exponential format

