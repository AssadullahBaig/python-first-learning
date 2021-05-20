print('\n---10-4---')
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
with open(filename, 'w') as f:
    while True:
        name = input("\nWhat's your name? ")
        if name == 'quit':
            break
        else:   
            f.write(name + "\n")
            print("Hi " + name + ", you've been added to the guest book.")