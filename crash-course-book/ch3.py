# --------- Practice -----------
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = f"My first bicycle was a {bicycles[0].title()}"
# print(message)
# print(bicycles[0].title())
# print(bicycles[1])
# print(bicycles[2])
# -----------------------------------
# motorcycles = ['honda', 'yamaha', 'suzuki']
# replacing a element in a list
# motorcycles[0] = 'ducati'
# adding an object in a list
# motorcycles.append('cd70')
# print(motorcycles)
# --------------------
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('suzuki')
# motorcycles.append('yamaha')
# print(motorcycles)
# ----------------------------
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')
# print(motorcycles)
# -------------------------
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
# -----------------------------
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# popped_motorcyles = motorcycles.pop(1)
# print(motorcycles)
# print(popped_motorcyles)
# ---------------------------
# motorcycles = ['honda', 'yamaha', 'ducati', 'suzuki']
# print(motorcycles)
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")
# --------------------------------
# cars = ["bmw", "audi", "sabaru"]
# sort function to sort the list in alphabetical order permanently
# print(cars)
# cars.sort()
# print(cars)
# -------------------------
# reverse order
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# --------------------------
# Sorting a List Temporarily with the sorted() Function
# ------------------------------
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")
# print(cars)
# ----------------------------------
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# cars.reverse()
# print(cars)
#----------------------------------
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(len(cars))

# ----------------------------------

# ------- Try it Yourself ------
# 3-1
print('---3-1---')
names = ['trex', 'jade', 'amber', 'leon']
print(names[0], names[2])
print(names[3], names[1])


print('---------\n')

# 3-2
print('---3-2---')
names = ['trex', 'jade', 'amber', 'leon']
message = f"Hello how are you? {names[0]}"
print(message)
message = f"Hello how are you? {names[1]}"
print(message)
message = f"Hello how are you? {names[2]}"
print(message)


print('---------\n')

# 3_3
print('---3-3---')
lists = ['honda', 'bike', 'car', 'bus']
message = f'I would love to own a {lists[0]} car'
print(message)
message = f'I dont like to ride a  {lists[3]}'
print(message)
message = f'I have a {lists[1]} at home'
print(message)

print('---------\n')

# 3_4
print('---3-4---')
guest_list = ['amber', 'johnny', 'amanda']
message = f"Hey {guest_list[0].title()} i would like to invite you to my party"
print(message)
message = f"Hey {guest_list[1].title()} i would like you to join my party"
print(message)
message = f"Hey {guest_list[2].title()} i would like to invite you at my place for a party"
print(message)

# 3_5
print('---3-5---')
guest_list = ['amber', 'johnny', 'amanda']

print(f"Sadly {guest_list[2].title()} will not be able to join us tonight")
print("I am inviting another guest to join us at party")
guest_list[2] = "zavala"
print(guest_list)
message1 = f"Hey {guest_list[0].title()} sorry for inconvenience but i had to change some things up"
print(message1)
message1 = f"Hey {guest_list[1].title()} i would like to re invite you to my party"
print(message1)
message1 = f"Hey {guest_list[2].title()} i would like to invite you to my party"
print(message1)

# 3_6
print('---3-6---')
guest_list = ['amber', 'johnny', 'amanda']
print(f"Sadly {guest_list[2].title()} will not be able to join us tonight")
print("I am inviting another guest to join us at party")
guest_list[2] = "zavala"
print(guest_list)
message1 = f"Hey {guest_list[0].title()} sorry for inconvenience but i had to change some things up"
print(message1)
message1 = f"Hey {guest_list[1].title()} i would like to re invite you to my party"
print(message1)
message1 = f"Hey {guest_list[2].title()} i would like to invite you to my party"
print(message1)
print("since i have found a bigger table with more space i would like to invite more people at the party")
guest_list.insert(0, "osiris")
guest_list.insert(2, "cayde")
guest_list.append("caitle")
print(guest_list)
message2 = f"Hey {guest_list[0].title()} i would like to invite you to my party"
print(message2)
message2 = f"Hey {guest_list[2].title()} i would like to invite you to my party"
print(message2)
message2 = f"Hey {guest_list[5].title()} i would like to invite you to my party"
print(message2)

# 3_7
print('---3-7---')
guest_list = ['amber', 'johnny', 'amanda']
guest_list[2] = "zavala"
print(guest_list)
message1 = f"Hey {guest_list[0].title()} sorry for inconvenience but i had to change some things up"
print(message1)
message1 = f"Hey {guest_list[1].title()} i would like to re invite you to my party"
print(message1)
message1 = f"Hey {guest_list[2].title()} i would like to invite you to my party"
print(message1)
print("since i have found a bigger table with more space i would like to invite more people at the party")
guest_list.insert(0, "osiris")
guest_list.insert(2, "cayde")
guest_list.append("caitle")
print(guest_list)
message2 = f"Hey {guest_list[0].title()} i would like to invite you to my party"
print(message2)
message2 = f"Hey {guest_list[2].title()} i would like to invite you to my party"
print(message2)
message2 = f"Hey {guest_list[5].title()} i would like to invite you to my party"
print(message2)
print("\nI just found out that my new dinner table won't arrive in time for the dinner, and i only have space for two people for dinner")
popped_guest = guest_list.pop()
print(popped_guest)
message2 = f"Im sorry {popped_guest} but i cannot invite you to the party now"
print(message2)
popped_guest = guest_list.pop()
print(popped_guest)
message2 = f"Im sorry {popped_guest} but i cannot invite you to the party now"
print(message2)
popped_guest = guest_list.pop()
print(popped_guest)
message2 = f"Im sorry {popped_guest} but i cannot invite you to the party now"
print(message2)
popped_guest = guest_list.pop()
print(popped_guest)
message2 = f"Im sorry {popped_guest} but i cannot invite you to the party now"
print(message2)

# for i in range(4):
#     popped_guest1 = guest_list.pop()
#     print(popped_guest1)
print(guest_list)
message2 = f"Hey {guest_list[0].title()} i just wanted to let you know that you're still invited to the party"
print(message2)
message2 = f"Hey {guest_list[1].title()} i just wanted to let you know that you're still invited to the party"
print(message2)
del guest_list[1]
print(guest_list)
del guest_list[0]
print(guest_list)

# 3_8
print('---3-8---')
locations = ["sydney", "colombia", "new york", "spain", "rome"]
print("Here is the list in its original state")
print(locations)
print("\nHere is the sorted list:")
print(sorted(locations))
print("\nHere is the list in its original state again:")
print(locations)
print("\nHere is the list in reverse")
locations.reverse()
print(locations)
print("reversing again to normal state")
locations.reverse()
print(locations)
print("sorting alphabetically")
locations.sort()
print(locations)
print("sorting reverse alphabetically")
locations.sort(reverse=True)
print(locations)

# 3_9
print('---3-9---')
guest_list = ["zavala", "cayde", "osiris", "johnny"]
print(len(guest_list))

# 3_10
print('---3-10---')
big_list = ["cero gordo", "mount rushmore", "french", "zvala", "spain", "romanian"]
print("\nAdding an element at the end of the list")
big_list.append("osiris")
print(big_list)
print("\nAdding new element at a certain location of list")
big_list.insert(0, "africa")
print(big_list)
print("\nDeleting a element")
del big_list[0]
print(big_list)
print("\nPopping an element off the list")
print(big_list)
popped_big_list = big_list.pop(2)
print(popped_big_list)
print("\nRemoving with reason from the list")
print(big_list)
too_expensive = 'spain'
big_list.remove(too_expensive)
print(big_list)
print(f"\nVisiting {too_expensive.title()} is too expensive for me.")
print("\nSorting the list alphabetically permanently")
print(big_list)
big_list.sort()
print(big_list)
print("\nSorting the list alphabetically temporarily")
print(big_list)
print(sorted(big_list))
print("\nReverse order for the list")
print(big_list)
big_list.reverse()
print(big_list)

# 3_11
print('---3-11---')
motorcycles = []
print(motorcycles[-1])

# ------------------------------
