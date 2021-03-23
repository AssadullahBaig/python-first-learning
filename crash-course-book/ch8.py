# --------- Practice -------------------
# def greet_user():
#     # display a simple greeting.
#     print("Hello!")
# greet_user()

# --------------------------------------
# def greet_user(username):
#     print(f"Hello, {username.title()}!")
# greet_user("james")
# --------------------------------------
# def describe_pet(pet_name, animal_type="dog"):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name="willie")
# --------------------------------------
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# --------------------------------------
# def build_person(first_name, last_name):
#  """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)


# --------------------------------------

# ------- Try it Yourself ------

# 8-1
print('\n---8-1---')


def display_message():
    msg = "Im learning to store code in functions"
    print(msg)


display_message()


# 8-2
print('\n---8-2---')


def favorite_book(title):
    print(title + " is one of my favorite books.")


favorite_book('The Abstract Wild')

# 8-3
print('\n---8-3---')


def make_shirt(size, message):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')


make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')


# 8-4
print('\n---8-4---')


def make_shirt(size="large", message="I love python"):
    print("\nIm going to make a " + size + " t-shirt.")
    print("It will say " + message + "")


make_shirt()
make_shirt(size="medium")
make_shirt("small", "programmers are loopy")


# 8-5
print('\n---8-5---')


def describe_city(city, country="pakistan"):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)


describe_city("lahore")
describe_city("karachi", "pakistan")
describe_city("mochi gate")


# 8-6
print('\n---8-6---')


def city_country(city, country):
    return city.title() + ", " + country.title()


print(city_country("santiago", "chile"))
print(city_country("karachi", "pakistan"))
print(city_country("frankfurt", "germany"))


# 8-7
print('\n---8-7---')
print("Album and artist:")


def make_album(artist, title):
    album_dict = {
        "artist": artist.title(),
        "title": title.title(),
    }
    return album_dict


print()
album = make_album("eminem", "river")
print(album)
album = make_album("eminem", "gnat")
print(album)
album = make_album("tupac", "changed man")
print(album)
print("\nWith tracks:")


def make_album(artist, title, tracks=None):
    album_dict = {
        "artist": artist.title(),
        "title": title.title(),
    }
    if tracks is not None:
        album_dict["tracks"] = tracks
    return album_dict


print()
album = make_album("eminem", "river", 0)
print(album)
album = make_album("eminem", "gnat")
print(album)
album = make_album("tupac", "changed man")
print(album)
album = make_album("eminem", "music to be murdered by", tracks=16)
print(album)

# 8-8
print('\n---8-8---')


def make_album(artist, title, tracks=0):
    album_dict = {
        "artist": artist.title(),
        "title": title.title(),
    }
    if tracks:
        album_dict["tracks"] = tracks
    return album_dict


title_prompt = "\nWhat album are you looking for? "
artist_prompt = "who's the artist? "

print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    artist = input(artist_prompt)
    if artist == 'quit':
        break
    album = make_album(artist, title)
    print(album)
print("\nThanks for responding")


# 8-9
print('\n---8-9---')


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


magicians = ["harry potter", " ron wesly", "john matters"]
show_magicians(magicians)


# 8-10
print('\n---8-10---')


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the great"
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)


magicians = ["harry potter", "ron wesly", "john matters"]
show_magicians(magicians)
print()
make_great(magicians)
show_magicians(magicians)


# 8-11
print('\n---8-11---')


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the great"
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)
    return magicians


magicians = ["harry potter", "ron wesly", "john matters"]
show_magicians(magicians)
print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)
print("\nOriginal magicians:")
show_magicians(magicians)


# 8-12
print('\n---8-12---')


def make_sandwich(*items):
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(" ....adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")


make_sandwich("roast beef", "cheddar cheese", "lettuce", "chicken")
make_sandwich("turkey", "cheese", "mustard", "salad")
make_sandwich("smoked grill chicken", "sauce")


# 8 - 13
print('\n---8-13---')


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('assadullah', 'baig',
                             location='lahore',
                             field='computers')
print(user_profile)


# 8-14
print('\n---8-14---')


def make_Car(manufacturer, model, **options):
    car_dict = {
        "manfacturer": manufacturer.title(),
        "model": model.title(),
    }
    for key, value in options.items():
        car_dict[key] = value
    return car_dict


my_outback = make_Car("sabaru", "outback", color="blue", tow_package=True, a='b')
print(my_outback)
my_accord = make_Car("honda", "accord", year=2012, color="white", headlights="popup")
print(my_accord)


# 8-15
print('\n---8-15---')
import print_model as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

