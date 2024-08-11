# zip + (variables) = aggregate elements from two or more iterables (list, tuples, sets etc.), creates a zip object with paired elements stored in
# tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ["p@ssword", "abc123", "guest"]

users = list(zip(usernames, passwords))

print(users)


import time

print(time.ctime(2))

print(time.time())

print(time.ctime(time.time()))

trime_object = time.localtime()
print(trime_object)