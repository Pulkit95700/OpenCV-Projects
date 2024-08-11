# list comprehension is a way to create a list with new syntax and less lines of code

squares = []
for i in range(4):
    squares.append(i*i)
print(squares)

# it can be made like this
squares_2 = [i*i for i in range(4)]

print(squares_2)

students = [100,90, 80, 70, 60, 50, 40, 30, 20, 10]

passed_students = [marks for marks in students if marks > 60]

passed_students_2 = [marks if marks > 60 else "FAILED" for marks in students]
print(passed_students_2)


# dictionary comprehensions

# dictionary = {key: expression for (key, value) in iterable}

cities_in_f = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

cities_in_c = {key + "1": round((value - 32) * 5/ 9) for (key, value) in cities_in_f.items()}

only_new_york = {key if key == "New York" else "h": value for (key, value) in cities_in_f.items()}
print(only_new_york)