# RESTAURANT

# Introduction
# Explain what the program will do:
# Here i am working on a program which gives us a menu to choose pizza from and then asks us if we need extra toppings
# for the pizza and after taking the user input, it tells us if the restaurant has the pizza and the toppings
# available or not, if they have the required pizza and toppings. the programs proceeds and gives us the
# total amount of the order. If the pizza or topping we ask for isn't in the available list, the program tells us
# that the restaurant doesn't have the pizza or the topping we ordered, and then program asks us for our order again
######


# Requirements ##
# 1. Ask for pizza type
#   Example:
#       Available pizzas: spicy, mexican, ....
#       Which pizza would you like to order?:
#
# 2. Ask for toppings until user inputs no. No separate input to just ask for yes and no
#   Example:
#       Available toppings: mushroom, onions, ....
#       Please specify topping or type no/quit to finish ordering pizza:
#
# 3. Print the order
#   Example: Preparing one spicy pizza with toppings: mushroom, onions
#
# 4. Ask user if they want to order another pizza, if yes then repeat from step 1.
#   Example: Would you like to order another pizza? (yes/no)
#
# 5. If no then print full order with each pizza, its topping and price and, finally, the total bill
#   Example:
#       Spicy pizza with toppings: mushroom: $5
#       Mexican pizza with toppings: calzone, tikka: $10
#
#       Total Price: $15
#       Thank you for ordering with us

# New Requirements
# Support different toppings for different pizzas

# Next Tasks
# 1. Fulfill the original requirement above 100%
# 2. Use list of dict instead of the zip function
# 3. Remove redundant code in the start_system function
# 4. Add the new requirement if possible

# Constraints ###
# No global variables. The functions should return the output they generate
# No functions inside functions. All functions should be add the root level (0 tab-space)
# No large functions. Max around 20 lines, preferably <15. One function should do generally one task
# Avoid loops inside loops (nested loops) inside a single function
# Function names should start with a verb e.g. order_pizza instead of pizza_order
# Variable names should be like nouns e.g. toppings, complete_order
# Compact output to minimize screen space


def order_pizza(available_pizzas):
    order = ("\nPlease specify the pizza or type quit to finish: ")
    print("\nAvailable Pizzas are: ")
    for pizza, prices in available_pizzas.items():
        print(pizza + ": " + str(prices) + ", ", end="")
    while True:
        pizza = input(order)
        if pizza in available_pizzas:
            print(f"You ordered a {pizza} pizza ")
            return pizza
        else:
            print("Im sorry we don't have that pizza.")

def order_toppings(available_toppings):
    extra_toppings =("\nPlease specify topping or type quit to finish ordering: ")
    print("\nAvailable toppings are: ")
    for topping, prices in available_toppings.items():
        print(topping + ": " + str(prices) + ", ", end="")
    toppings_list = []
    while True:
        topping = input(extra_toppings)
        if topping == "quit":
            break
        elif topping in available_toppings:
            toppings_list.append(topping)
            print(f"I'll add {topping} to your pizza")
        else:
            print("Im sorry we don't have that topping.")
    return toppings_list

def finalize_order(available_pizzas, available_toppings, total_order):
    total_cost = 0
    print('Your ordered pizzas:')
    
    for i in total_order:
        print(f"{i['pizza']} pizza with toppings: {', '.join(o for o in i['toppings'])} : ${i['price']}" )
        total_cost += i['price']
  
    print("Total Cost: $" + str(total_cost))
    print("Thank you for ordering with us")

def start_system():
    available_pizzas = {'spicy': 600, 'mexican': 700, 'calzone': 600, 'tikka': 700, 'veg': 650}
    available_toppings = {'mushroom': 10, 'onions': 15, 'green pepper': 10, 'extra cheese': 40}
    print("Hi, welcome to our Saleem Shady Pizza Ordering")
    total_order = []

    ordering_another_pizza = True
    while(ordering_another_pizza is True):
        pizza = order_pizza(available_pizzas)
        toppings = order_toppings(available_toppings)
        topping_price = 0
        for i in toppings:
            topping_price += available_toppings[i]
        total_order.append({
            'pizza': pizza,
            'price': available_pizzas[pizza] + topping_price,
            'toppings': toppings
            })
        print(f"Preparing one {pizza} pizza with toppings: {', '.join(toppings)}")
        extra_pizza = input("Would you like to order another pizza? (yes/no): ")
        if extra_pizza == "no":
            ordering_another_pizza = False
        else:
            ordering_another_pizza = True

    finalize_order(available_pizzas, available_toppings, total_order)

start_system()