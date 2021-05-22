# --------- Practice -------------------
# import json
# numbers = [2, 3, 5 ,7 , 10]
# filename = 'numbers.json'
# with open (filename, 'w') as f:
#     json.dump(numbers, f)

# import json

# username = input("what is your name? ")
# filename = 'username.json'
# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print("we'll remember you when you come back")


# import json

# filename = 'username.json'
# with open(filename) as f:
#     username = json.load(f)
#     print(f"welcome back , {username}!")


# import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

# filename = 'username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("what is your name? ")
#     with open (filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We'll remember you when you come back, {username}! ")
# else:
#     print(f"Welcome back, {username}! ")

# import json

# def greet_user():
#     filename= 'username.json'
#     try: 
#         with open (filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f:
#             json.dump(username, f)
#             print(f"We'll remember you when you come back, {username}")
#     else:
#         print(f"Welcome back, {username}!")
# greet_user()

# import json

# def get_Stored_username():
#     filename = 'username.json'
#     try:
#         with open (filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username

# def greet_user():
#     username = get_Stored_username()
#     if username:
#         print(f"welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         filename = 'username.json'
#         with open (filename, 'w') as f:
#             json.dump(username, f)
#             print(f"We'll remember you when you come back {username}!")
# greet_user()


# import json

# def get_Stored_username():
#     filename = 'username.json'
#     try:
#         with open (filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username

# def get_new_username():
#     username = input("What is your name? ")
#     filename = 'username.json'
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#     return username

# def greet_user():
#     username = get_Stored_username()
#     if username:
#         print(f"welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         filename = 'username.json'
#         with open (filename, 'w') as f:
#             json.dump(username, f)
#             print(f"We'll remember you when you come back {username}!")
# greet_user()

# --------------------------------------\


# ------- Try it Yourself ------

# 10-1
print('\n---10-1---')
filename = 'learning_python.txt'

print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())


# 10-2
print('\n---10-2---')
filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))


# 10-3
print('\n---10-3---')
name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)

# 10-4
print('\n---10-4---')
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name + "\n")
        print("Hi " + name + ", you've been added to the guest book.")


# 10-5
print('\n---10-5---')
filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")


# 10-6
print('\n---10-6---')
try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)

except ValueError:
    print("Sorry, I really needed a number.")

else:
    sum = x + y
    print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")


# 10-7
print('\n---10-7---')
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")

# 10-8
print('\n---10-8---')
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")


# 10-9
print('\n---10-9---')
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        print("\nReading file: " + filename)
        print(contents)

# 10-10
print('\n---10-10---')
def count_common_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)

        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filename = 'book.txt'
count_common_words(filename, 'the')

# 10-11
print('\n---10-11---')
import json

number = input("What's your favorite number? ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("Thanks! I'll remember that.")

import json

with open('favorite_number.json') as f:
    number = json.load(f)

print(f"I know your favorite number! It's {number}.")

# 10-12
print('\n---10-12---')
import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print(f"I know your favorite number! It's {number}.")

# 10-13
print('\n---10-13---')
import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
