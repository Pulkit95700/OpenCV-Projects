try:
    with open('text.txt') as file:
        print(file.read())
except FileNotFoundError as e:
        print("That file is not found in python")
except Exception as e:
    print(e)
finally:
    file.close()

text = "Yooooooo\nThis is some text\nHave a good one!\n"

#with open('test.txt', 'w') as file:
#     file.write(text)

f = "this wil append the text to the file"
with open('test.txt', 'a') as file:
    file.write(f)