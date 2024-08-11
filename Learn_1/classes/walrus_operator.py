# walrus_operator :=

# new feature to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as a part of a larger expression

# we can assign a value and use it at the same time
# hello = "hello"
# print(hello)

# this is same as above code
print(hello := "pulkit")
print(hello)

# walrus operator ko apan kaafi jagah istmaal kar sakte hain, upar print wali line se
# ye to samajh main aagya hoga ki walrus operator wahi variable return karta hai kyunki hello ki value print hui thi

# foods = list()
# while True:
#     food = input("What food do you like?")
#     if(food == "quit"):
#         break
#     foods.append(food)
#
# print(foods)

# this same code can be written as
foods = list()
while (food := input("What food do you like?")) != "quit":
    foods.append(food)
print(foods)