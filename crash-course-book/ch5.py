# --------- Practice -------------------
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# -----------------------------------------
# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")
# -------------------------------------------
# age_0 = 22
# age_1 = 18
# if age_0 >= 21 or age_1 >= 21:
#     print("no this is not equal")
# -------------------------------------------
# requested_toppings = ["mushrooms", "onions", "pineapple"]
# if "malorant" in requested_toppings:
#     print("y")
# elif "pineapple" in requested_toppings:
#     print("no")
# --------------------------------------------
# banned_users = ["andrew", "carolina", "david"]
# user = "marie"
# if user not in banned_users:
#     print(f"{user.title()}, You can post a response if you wish.")
# --------------------------------------------
# age = 19
# if age >= 18:
#     print("You are old enough to vote!")
# --------------------------------------------
# age = 12
#  if age < 4:
#      print("Your admission cost is 0$.")
#  elif age < 18:
#     print("Your admission cost is 25$.")
#  else:
#      print("Your admission cost is 50$.")
# --------------------------------------------

# requested_toppings = ['mushrooms', 'extra cheese']
#
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
#
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
#
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
#
# print("\nFinished making your pizza!")
# --------------------------------------------

# --------------------------------------


# ------- Try it Yourself ------

# 5-1
print('---5-1---')
print("1")
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\n------------------------------------")
# -----------------------------------------
print("2")
fruit = 'mango'
print("Is fruit == 'mango'? I predict True.")
print(fruit == 'mango')
print("\nIs fruit == 'apple'? I predict False.")
print(fruit == 'apple')
print("\n------------------------------------")
# -----------------------------------------
print(3)
animal = 'cat'
print("is animal == 'cat'? I predict True")
print(animal == "cat")
print("\nIs animal == 'rat'? I predict False")
print(animal == 'rat')
print("\n------------------------------------")
# -----------------------------------------
print(4)
people = 'andy'
print("is people == 'andy'? I predict True")
print(people == "andy")
print("\nIs people == 'john'? I predict False")
print(people == 'john')
print("\n------------------------------------")
# -----------------------------------------
print(5)
food = 'curry'
print("is food == 'curry'? I predict True")
print(food == "curry")
print("\nIs food == 'chicken'? I predict False")
print(food == 'chicken')
print("\n------------------------------------")
# -----------------------------------------
print(6)
food = 'salad'
print("is food == 'curry'? I predict False")
print(food == "curry")
print("\nIs food == 'salad'? I predict True")
print(food == 'salad')
print("\n------------------------------------")
# -----------------------------------------
print(7)
thing = 'cycle'
print("is thing == 'car'? I predict False")
print(thing == "car")
print("\nIs thing == 'cycle'? I predict True")
print(thing == 'cycle')
print("\n------------------------------------")
# -----------------------------------------
print(8)
thing = 'keyboard'
print("is thing == 'mouse'? I predict False")
print(thing == "mouse")
print("\nIs thing == 'keyboard'? I predict True")
print(thing == 'keyboard')
print("\n------------------------------------")
# -----------------------------------------
print(9)
song = 'eminem'
print("is song == 'eminem'? I predict False")
print(song == "drake")
print("\nIs song == 'eminem'? I predict True")
print(song == 'eminem')
print("\n------------------------------------")
# -----------------------------------------
print(10)
content = 'funny'
print("is content == 'funny'? I predict False")
print(content == "not funny")
print("\nIs content == 'funny'? I predict True")
print(content == 'funny')
print("\n------------------------------------")
# -----------------------------------------
# 5_2
print('---5-2---')
print(1)
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Not the same topping!")
else:
    print("Thanks!")
print("\n------------------------------------")
print(2)
requested_topping = 'mushrooms'
if requested_topping == 'mushrooms':
    print("Thanks!")
else:
    print("Not the toppings i ordered!")
print("\n------------------------------------")
print(3)
cars = ['audi', 'BMW', 'subaru', 'toyota']
for car in cars:
    if car == 'BMW':
        print(car.lower())
print("\n------------------------------------")
print(4)
age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
    print("no this is not equal")
print("\n------------------------------------")
print(5)
number_0 = 7
number_1 = 5
if number_0 == 3 or number_1 != 6:
    print("This will show a result")
print("\n------------------------------------")
print(6)
number_0 = 17
number_1 = 26
if number_0 >= 18 or number_1 <= 28:
    print("This won't show a result")
print("\n------------------------------------")
print(7)
number_0 = 3
number_1 = 7
if number_0 == 18 or number_1 <= 5:
    print("This won't show a result")
print("this won't show a result")
print("\n------------------------------------")
print(8)
number_0 = 9
number_1 = 3
if number_0 == 9 and number_1 <= 5:
    print("This will show a result")
print("\n------------------------------------")
print(9)
number_0 = 3
number_1 = 7
if number_0 == 18 and number_1 <= 5:
    print("This won't show a result")
print("This won't show a result")
print("\n------------------------------------")
print(10)
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, You can post a response if you wish.")
print("\n------------------------------------")
print(11)
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, You can post a response if you wish.")
print("\n------------------------------------")
print(12)
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user in banned_users:
    print(f"{user.title()}, You cannot post here")
else:
    print("user not found!")

# 5_3
print('---5-3---')
print("Passing version:")
alien_color = "green"
if alien_color == "green":
    print("\nYou just earned 5 points")
# -----------------------------------------
print("Failing version:")
alien_color = "red"
if alien_color == "green":
    print("You just earned 5 points")
print("This won't show a result cus the condition failed.")

# 5_4
print('---5-4---')
print("if block runs:")
alien_color = "green"
if alien_color == "green":
    print("\nYou just earned 5 points")
else:
    print("You just earned 10 points")
# ----------------------------------------
print("\nelse block runs:")
alien_color = "yellow"
if alien_color == "green":
    print("You just earned 5 points")
else:
    print("\nYou just earned 10 points")

# 5_5
print('---5-5---')
alien_color = "Green"
if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

# 5_6
print('\n---5-6---')
age = 17
if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult")
else:
    print("You're an elder")

# 5_7
print('---5-7---')

favorite_fruits = ['blueberries', 'salmonberries', 'peaches']
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")

# 5_8
print('---5-8---')

usernames = ['eric', 'willie', 'admin', 'erin', 'ever']
for username in usernames:
    if username == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again!")

# 5_9
print('---5-9---')
usernames = []
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see status report?")
        else:
            print(f"Hello {username.title()}, Thank you for logging in again!")
else:
    print("We need to find some users")
# 5_10
print('---5-10---')

current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user.title()}, that name is taken.")
    else:
        print(f"Great, {new_user.title()} is still available.")

# 5_11
print('---5-11---')
numbers = (range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")
