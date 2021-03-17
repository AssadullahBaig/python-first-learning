# import csv
# file = open("phonebook.csv", "a")
# name = str(input("Name: "))
# number = str(input("Number: "))
# writer = csv.writer(file)
# writer.writerow([name, number])
# file.close()

#using the WITH keyword now because it automatically opens and closes a file for us..
import csv

with open("phonebook.csv", "a") as file:
    name = str(input("Name: "))
    number = str(input("Number: "))
    writer = csv.writer(file)
    writer.writerow([name, number])

