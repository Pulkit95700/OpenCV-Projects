import math

pi = -3.14
print(round(pi))
print(math.ceil(pi))

print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(abs(pi)))

x, y, z = 1, 2, 3

print(max(x, y, z))
print(min(x, y, z))

# string slicing s[start: stop: step] (range to be one greater than it should be)

name = "Pulkit is a good boy"
first_name = name[0: 6]
print(first_name)
first_name = name[0: 6: 2]
print(first_name)

print("**********************"
      "")
funky = "This is reverse"
print(funky[-5:-1])
print(funky[::-1])

website = "https://www.google.com"
# slice first create objects
slice = slice(12, -4)

print(website[slice])

# name = ""
# while len(name) == 0:
#     name = input("Enter your name: ")
#
# print("Hello", name)

for i in range(1, 11):
    print(i)
# pass does nothing just a placeholder in a block

# list is used to store multiple items in a single variable

food = ["pizza", "ham_burgers", "hotdog"]
print(food)

food.append("sausages")
print(food)
food.pop()
print(food)
food.insert(0, "pulkit")
food.sort()
print(food)
food.clear()
print(food)

# // 2d list

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "icecream"]

f = [drinks, dinner, dessert]

print(f[0][0])

# tuples are collection that are unchangable

student = ("Bro", 21, "male")
print(student.count("bro"))

# set is a collection which is unordered, unindexed, No duplicate values

utensils = {"fork", "spoon", "knife"}
print(utensils)
dishes = {"spoon", "bowl"}
utensils.update(dishes)
utensils.add("napkin")
utensils.remove(("fork"))

print(utensils)

dinner_table = utensils.union(dishes)
print(dinner_table)
print(utensils.intersection(dishes))


# A changeable, unordered collection of unique key:value pairs Fast because they use hashing, allow us to access value quickly

capitals = {
    'USA': 'Washington DC',
    'India': 'New Delhi',
    'China': 'Bejing',
    'Russia': 'Moscow'
}
# this could give you error if your key is not found in the dictionary
# print(capitals['Germany'])

# a better method is to use the find function
print(capitals.get('Germany'))


print(capitals.items())
print(capitals.values())
print(capitals.keys())

for key, values in capitals.items():
    print(key, values)

capitals['USA'] = 'pulkit'
print(capitals)

# to remove you can use
capitals.pop('USA')
print(capitals)