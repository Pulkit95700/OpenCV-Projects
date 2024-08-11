# we can make higher order function in python also as in javascript
import functools
import math
# def divisor(x):
#     def dividend(y):
#         return y / x;
#     return dividend
#
# divide = divisor(2)
# print(divide(10))


# lambda function = function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression
# (think of it as shortcut)
# useful if needed for a short period of time

# lambda parameter:expression

# def double(x):
#     return x*2
#
# print(4)

double = lambda x: x*2
print(double(10))

multiply = lambda x,y: x*y
print(multiply(3, 5))

full_name = lambda f_name, l_name: f_name + " " + l_name

print(full_name("Pulkit", "Gupta"))

age_check = lambda age: True if age > 18 else False

print(age_check(19))

# sort function in python

# sort() method that is built in lists
# sort() function = used with iterables

students = ["Squid", "Sandy", "Apple"]
students.sort()

print(students)

# now you can also use sorted method for iterables like tuple

students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr Krabs")

# students.sort(reverse=True) cannot be used because tuples do not have sort method
sorted_students = sorted(students)

# it always returns a list
print(sorted_students)

# level 2

students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36)
            ]

students.sort()

# default sorts the element related to the first column
print(students)

grade = lambda grades: grades[1]
students.sort(key=grade, reverse=True)
#sort the students using grades

print(students)

# key is sort is a parameter that is used to sort the array related to a particular item in the list, it takes in
# a function and use to the get the value from each element. it passes each element as a parameter to the function

# same can be written with sorted function, (can be used if the given data type is a tuple)
sorted_students = sorted(students, key=grade)
print(sorted_students)

# map function applies a function to each item in an iterable

to_euro = lambda data: (data[0], data[1] * 0.82)

store = [
    ("shirt", 20.0),
    ("pants", 25.00),
    ("jacket", 50.00)
]

store_euros = list(map(to_euro, store))

print(store_euros)


# filter function returns all the elements that follows a certain condition

friends = [("Pulkit", 20),
           ("Harshit", 24),
           ("Ayush", 21),
           ("Dhruv", 20),
           ("Yash", 20)
           ]

# want all the firends of age greater than 20 only in my list
filtered_friends = list(filter(lambda e: e[1] > 20, friends));
print(filtered_friends)

# reduce function in python. It is used to compute a single value in whole iterable like a sum, multiply, average etc
# we need to import functools library for this


average_age = functools.reduce(lambda x, y: math.floor((x if isinstance(x, int) else x[1] + y[1]) / 2), friends)

print(average_age)