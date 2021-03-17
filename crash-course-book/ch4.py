# --------- Practice -----------
# looping through a list
# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(magician)
# ------------------------
# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
# ------------------------
# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# -------------------------
# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you everyone. that was a great magic show!")
# ----------------------------------
# for value in range(1, 5):
#     print(value)
# ----------------------------------
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)
# -----------------------------------
# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)
# -----------------------------------
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))
# -----------------------------------
# squares =[value**2 for value in range(1, 11)]
# print(squares)
# -----------------------------------
# slicing a list:
# players = ["Charles", " martina", "michael", "florence", "eli", "zavala", "osiris"]
# print(players[0:3])
# print(players[3:6])

# ----------------------------------
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())
# -----------------------------------
# my_foods = ["pizza", "falafel", "carrot cake"]
# friends_food = my_foods[:]
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friends_food)
# tuples
dimensions = (250, 50)
print("original dimensions")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimension)

 # --------------------------------------


# ------- Try it Yourself ------

# 4-1
print('---4-1---')
pizzas = ["pepperoni", "chicken", "cheese"]
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")
print("I really love pizza")

# 4_2
print('---4-2---')
animals = ["sher", "cheetah", "chuha"]
for animal in animals:
    print(f"A {animal.title()} would be a great pet")
print("\nNon of these a great pets lol")

# 4_3
print('---4-3---')
# numbers =[]
# for numbers in range(1, 21):
#     print(numbers)

# 4_4
print('---4-4---')
# numbers = []
# for numbers in range(1, 1000001):
#     print(numbers)

# 4_5
print('---4-5---')
numbers = list(range(1, 1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4_6
print('---4-6---')
numbers = []
for numbers in range(1, 21, 2):
    print(numbers)

# 4_7
print('---4-7---')
threes = list(range(3, 31, 3))
for number in threes:
    print(number)

# 4_8
print('---4-8---')
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
for cube in cubes:
    print(cube)

# 4_9
print('---4-9---')
cubes = [number**3 for number in range(1, 11)]
for cube in cubes:
    print(cube)

# 4_10
print('---4-10---')
players = ['charles', 'martina', 'michael', 'florence', 'eli', "zavala", "osiris", "cayde"]
print("The first three names in my list are")

for player in players[:3]:
    print(player.title())
print("\nThese are the names in the middle of my list")
for player in players[2:5]:
    print(player.title())
print("\nThese are the names at the end of my list")
for player in players[5:]:
    print(player.title())

# 4_11
print('---4-11---')
fav_pizzas = ["pepperoni", "chicken", "veggie"]
friend_pizzas = fav_pizzas[:]

fav_pizzas.append("tikka")
friend_pizzas.append("cheese")
print("my favorite pizzas are:")
for pizza in fav_pizzas:
    print("-" + pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("-" + pizza)

# 4_13
print('---4-13---')
menu = ("curry", "sandwich", "nuggets", "salmon", "zinger burger", "cake")
print("you can choose from the following items in the menu:")
for item in menu:
    print("-" + item)
# menu[0] = "fish"
# print(menu)
menu = ("curry", "sandwich", "nuggets", "salmon", "shawarma", "chicken roll")
print("\nOur menu has been updated")
print("You can now choose these items from the menu:")
for item in menu:
    print("-" + item)



