# RESTAURANT

# Introduction
# Explain what the program will do
######

available_pizzas = ['spicy', 'mexican', 'calzone', 'tikka', 'veg']
available_toppings = ['mushroom', 'onions', 'green pepper', 'extra cheese']
pizza_prices = {'spicy': 600, 'mexican': 700, 'calzone': 600, 'tikka': 700, 'veg': 650}
topping_prices = {'mushroom': 10, 'onions': 15, 'green pepper': 10, 'extra cheese': 40}
sub_total = []
final_order = {}

# ordering a pizza here..
print("Hi, welcome to our Saleem Shady Pizza Ordering")
order_pizza = True
while order_pizza:
    print("Please choose a pizza of your choice: ")
    print()
    for pizzas in available_pizzas:
        print(pizzas)
        print()
    while True:
        pizza = input("Which pizza would you like to order?\n")
        if pizza in available_pizzas:
            print(f"You have ordered a {pizza} pizza.")
            sub_total.append(pizza_prices[pizza])
            break
        if pizza not in available_pizzas:
            print(f"I am sorry, we currently do not have {pizza} pizza.")

    # im asking for extra toppings here...
    order_topping = True
    print("\nThis is the list of available extra toppings: ")
    for toppings in available_toppings:
        print(toppings)
        print()
    while order_topping:
        extra_topping = input("Would you like an extra topping? (yes / no)?")
        if extra_topping == "yes":
            topping = input("Which one would you like to add?")
            if topping in available_toppings:
                final_order.setdefault(pizza, [])
                final_order[pizza].append(topping)
                print(f"I have added {topping}.")
                sub_total.append(topping_prices[topping])
            else:
                print(f"I am sorry, we don't have {topping} available.")

        elif extra_topping == "no":
            break
    extra_pizza = input("Would you like to order another pizza? (yes / no)?")
    if extra_pizza == "no":
        for key, value in final_order.items():
            print(f"\nYou have ordered a {key} pizza with {value}")
        check_order = True
        while check_order:
            print()
            order_correct = input("Is this correct? yes / no ")
            if order_correct == "yes":
                check_order = False
                order_pizza = False
            if order_correct == "no":
                print(final_order)
                add_remove = input("would you like to add or remove? ")
                if add_remove == "remove":
                    remove = input("Which pizza would you like to remove? ")
                    del final_order[remove]
                    print(final_order)
                if add_remove == "add":
                    check_order = False

# finalizing the order
print(f"\nYour total order price is: ${sum(sub_total)}")






