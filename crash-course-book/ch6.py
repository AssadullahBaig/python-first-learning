# --------- Practice -------------------
# alien_0 = {"color": "green", "points": 5}
# print(alien_0["color"])
# print(alien_0["points"])
# print()
# --------------------------------------
# alien_0 = {"color": "green", "points": 5}
# print(alien_0["color"])
# alien_0 = {"color": "green", "points": 5}
# new_points = alien_0["points"]
# print(f"You just earned {new_points} points!")
# --------------------------------------
# alien_0 = {"color": "green", "points": 5}
# print(alien_0)
# alien_0["x_position"] = 0
# alien_0["y_position"] = 25
# print(alien_0)
# --------------------------------------
# alien_0 = {}
# alien_0["color"] = "green"
# alien_0["points"] = 5
# print(alien_0)
# --------------------------------------
# alien_0 = {"color": "green"}
# print(f"The alien is {alien_0['color']}.")
# alien_0["color"] = "yellow"
# print(f"The alien is now {alien_0['color']}.")
# --------------------------------------
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")
# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0["x_position"] = alien_0["x_position"] + x_increment
# print(f"New position: {alien_0['x_position']}")
# --------------------------------------
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)
# --------------------------------------
# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")
# --------------------------------------
# user_0 = {
#  'username': 'efermi',
#  'first': 'enrico',
#  'last': 'fermi',
#  }
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")
# --------------------------------------
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s' 'fav lang is {language.title()} ")

# --------------------------------------


# ------- Try it Yourself ------

# 6-1
print('\n---6-1---')
person = {
    "first_name": "john",
    "last_name": "barns",
    "age": 20,
    "city": "california",
}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

# 6_2
print('\n---6-2---')
favorite_numbers = {
    "john": 34,
    "carter": 78,
    "elias": 2,
    "carlos": 8,
    "amy": 1
}
number = favorite_numbers["john"]
print("john's favorite number is " + str(number) + ".")

number = favorite_numbers["carter"]
print("carter's favorite number is " + str(number) + ".")

number = favorite_numbers["elias"]
print("elias's favorite number is " + str(number) + ".")

number = favorite_numbers["carlos"]
print("carlos's favorite number is " + str(number) + ".")

number = favorite_numbers["amy"]
print("amy's favorite number is " + str(number) + ".")
# ----------------------------------------------------
# 6_3
print('\n---6-3---')
glossary = {
    "string": "A series of characters.",
    "comment": "A note in a program that the python interpreter ignore.",
    "list": "The Group of elements is called a list in python.",
    "loop": "Work through a collection of items, one at a time.'",
    "dictionary": "A collection of key-value pairs",
}
word = "string"
print("\n" + word.title() + ": " + glossary[word])

word = "comment"
print("\n" + word.title() + ": " + glossary[word])

word = "list"
print("\n" + word.title() + ": " + glossary[word])

word = "loop"
print("\n" + word.title() + ": " + glossary[word])

word = "dictionary"
print("\n" + word.title() + ": " + glossary[word])

# ----------------------------------------------------
# 6_4
print('\n---6-4---')
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
}

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
# ----------------------------------------------------
# 6_5
print('\n---6-5---')
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())
# ----------------------------------------------------
# 6_6
print('\n---6-6---')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print("\n")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")
# ----------------------------------------------------
# 6_7
print('\n---6-7---')
people = []

person = {
    'first_name': 'john',
    'last_name': 'barns',
    'age': 20,
    'city': 'california',
}
people.append(person)

person = {
    'first_name': 'ever',
    'last_name': 'grand',
    'age': 5,
    'city': 'lahore',
}
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'mathers',
    'age': 8,
    'city': 'detroit',
}
people.append(person)

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + ", of " + city + ", is " + age + " years old.")
# ----------------------------------------------------
# 6_8
print('\n---6-8---')

pets = []

pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
# ----------------------------------------------------
# 6_9
print('\n---6-9---')
favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'ever': ['mt. verstovia', 'the playground', 'south carolina']
}

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())
# ----------------------------------------------------
# 6_10
print('\n---6-10---')
favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))

# ----------------------------------------------------
# 6_11
print('\n---6-11---')
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
    },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himilaya',
    }
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  The " + mountains + " mountains are nearby.")
# ----------------------------------------------------
# 6_12
print('\n---6-12---')
