# RESTAURANT

# Introduction
# Explain what the program will do:
# Here i am working on a program which gives us a menu to choose pizza from and then asks us if we need extra toppings
# for the pizza and after taking the user input, it tells us if the restaurant has the pizza and the toppings
# available or not, if they have the required pizza and toppings. the programs proceeds and gives us the
# total amount of the order. If the pizza or topping we ask for isn't in the available list, the program tells us
# that the restaurant doesn't have the pizza or the topping we ordered, and then program asks us for our order again
######


###### FINISHED ########

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

# New Tasks
# 1. Add support for different toppings for different pizzas
# 2. Order another pizza prompt should show error when input is neither yes nor no

#######################

# Constraints ###
# No global variables. The functions should return the output they generate
# No functions inside functions. All functions should be add the root level (0 tab-space)
# No large functions. Max around 20 lines, preferably <15. One function should do generally one task
# Avoid loops inside loops (nested loops) inside a single function
# Function names should start with a verb e.g. order_pizza instead of pizza_order
# Variable names should be like nouns e.g. toppings, complete_order
# Compact output to minimize screen space
#---------------------------------------

def order_burger():
    available_burgers = {"zinger": 200, "fish": 350, "beef": 250, "patty": 150, "grilled": 260}
    
    order = ("\nPlease specify the burger u want or type quit to finish: ")
    print("\nAvailable burgers are: ")
    for burger, prices in available_burgers.items():
        print(burger + ": " + str(prices) + ", ", end="")
    while True:
        burger = input(order)
        if burger in available_burgers:
            print(f"You ordered a {burger} burger. ")
            return {"burger": burger, "price": available_burgers[burger]}          
        else:
            print("Im sorry we don't have that burger.")      

def selecting_pizza(available_pizzas):
    order = ("\nPlease specify the pizza: ")
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

def selecting_toppings(pizza, topping_prices, supported_toppings):
    toppings_list = []
    extra_toppings =("\nPlease specify topping or type quit to finish ordering: ")
    print("\nAvailable toppings are: ")
    for topping in supported_toppings[pizza]:
        price = topping_prices[topping]
        print(topping + ": " + str(price) + ", ", end="")

    while True:
        topping = input(extra_toppings)
        if topping == "quit":
            break
        elif topping in supported_toppings[pizza]:
            toppings_list.append(topping)
            print(f"I'll add {topping} to your pizza")
        else:
            print("Im sorry we don't have that topping.")
    return toppings_list

def order_pizzas():
    available_pizzas = {'spicy': 600, 'mexican': 700, 'calzone': 600, 'tikka': 700, 'veg': 650}
    topping_prices = {'mushroom': 10, 'onions': 15, 'green pepper': 10, 'extra cheese': 40}
    supported_toppings = {
        "spicy": ("green pepper", "onions"),
        "mexican": ("extra cheese", "onions"),
        "calzone": ("extra cheese", "green pepper"),
        "tikka": ("onions", "mushroom", "extra cheese"),
        "veg": ("onions", "mushroom"),
    }
    
    pizza = selecting_pizza(available_pizzas)
    toppings = selecting_toppings(pizza, topping_prices, supported_toppings)
    topping_price = 0
    for i in toppings:
        topping_price += topping_prices[i]
    return {'pizza': pizza, 'price': available_pizzas[pizza]+topping_price, 'toppings': toppings}
    
def finalize_order(total_pizzas, total_burgers):
    total_cost = 0
    print('Your ordered burgers:')
    for i in total_burgers:
        print(f"{i['burger']} burger: ${i['price']}" )
        total_cost += i['price']
    print('Your ordered pizzas:')
    for i in total_pizzas:
        print(f"{i['pizza']} pizza with toppings: {', '.join(o for o in i['toppings'])} : ${i['price']}" )
        total_cost += i['price']  
    print("Total Cost: $" + str(total_cost))

def main():
    total_burgers = []
    total_pizzas = [] 
  
    

    print("Hi, welcome to our Saleem Shady food Ordering")
    isContinueOrder = True
    while(isContinueOrder):
        menu = input("Please select the type of food you want (burger, pizza): ")
        if menu == 'pizza':
            pizza = order_pizzas()
            print(f"Preparing one {pizza['pizza']} pizza with toppings: {', '.join(pizza['toppings'])}")
            total_pizzas.append(pizza)
        elif menu == 'burger':
            burger = order_burger()
            print(f"Preparing one {burger['burger']} burger ")
            total_burgers.append(burger)          
            
        another_order = input("Would you like to do an another order? (yes/no): ")
        if another_order == "no":
            isContinueOrder = False
            finalize_order(total_pizzas, total_burgers)
            print('\n Thank you for ordering with us')
        elif another_order == 'yes':
            isContinueOrder = True
       
main()


