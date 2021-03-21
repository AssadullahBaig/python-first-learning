# --------- Practice -------------------
#  input user works
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
# --------------------------------------
# write clear prompts
# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")
# --------------------------------------
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")
# --------------------------------------
# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 48:
#  print("\nYou're tall enough to ride!")
# else:
#  print("\nYou'll be able to ride when you're a little older.")
# --------------------------------------
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#  print(f"\nThe number {number} is even.")
# else:
#  print(f"\nThe number {number} is odd.")
# --------------------------------------
# while loop in action
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
# --------------------------------------

# --------------------------------------

# ------- Try it Yourself ------

# 7-1
# print('\n---7-1---')
car = input("What kind of car would you like?:")
print(f"Let me see if i can find you a {car.title()}.")

# 7-2
print('\n---7-2---')
party_size = input("How many people are in your dinner party tonight? ")
party_size = int(party_size)
if party_size > 8:
    print("Im sorry, you'll have to wait for a table")
else:
    print("Your table is ready!")

# 7-3
print('\n---7-3---')
number = input("Give me a number, please: ")
number = int(number)
if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")

# 7-4
print('\n---7-4---')
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' When you are finished: "
while True:
    topping = input(prompt)
    if topping != "quit":
        print(" I'll add " + topping + " to your pizza.")
    else:
        break


# 7-5
print('\n---7-5---')
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
# 7-6
print('\n---7-6---')
prompt = "\nMovie ticket prices are based on age, please enter your age for your price: "
prompt += "\nType 'quit' to exit the program."

active = True

while active:
    age = input(prompt)

    if age == "quit":
        active = False
    else:
        age = int(age)
        if age < 3:
            print("YOU ARE FREE!")
        elif age < 13:
            print("YOU ARE $10.00")
        else:
            print("YOU ARE $15.00")

# 7-7
print('\n---7-7---')
# while True
#     print("WHY AM I!")
# 7-8
print('\n---7-8---')
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

# 7-9
print('\n---7-9---')
sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
# 7-10
print('\n---7-10---')
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

responses = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place

    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")
