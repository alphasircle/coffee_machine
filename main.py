from machine_data import MENU
from machine_data import resources


profit = 0 # money put in machine by user


# take input from user and decide next step
def check_user_choice(check_choice, money):
    if check_choice == "espresso":
        return "espresso"
    elif check_choice == "latte":
        return "latte"
    elif check_choice == "cappuccino":
        return "cappuccino"
    elif check_choice == "prices":
        espresso = MENU['espresso']['cost']
        latte = MENU['latte']['cost']
        cappuccino = MENU['cappuccino']['cost']
        print(f'Espresso: ${espresso}\nLatte: ${latte}\nCappuccino: ${cappuccino}\n')
        return "prices"
    elif check_choice == "status":
        water = resources['water']
        milk = resources['milk']
        coffee = resources['coffee']
        print(f"Water: {water} ml\nMilk: {milk} ml\nCoffee: {coffee} g\nMoney: ${money}\n")
        return "status"
    elif check_choice == "off":
        return "off"
    else:
        print("Unexpected error.\nRestarting machine...\n")
        game_on()

# checks if enough resources
def is_enough(returned_choice):
    if resources['water']< MENU[returned_choice]['ingredients']['water']:
        print('Not enough water.\n')
        game_on()
    elif resources['milk'] < MENU[returned_choice]['ingredients']['milk']:
        print('Not enough milk.\n')
        game_on()
    elif resources['coffee'] < MENU[returned_choice]['ingredients']['coffee']:
        print('Not enough coffee.\n')
        game_on()
    else:
        print("")  # this line means there are enough resources and should continue process of making coffee

# checks if user put enough money, gives change and returns price of drink to add to machine profit
def calculate_price(quarters, dimes, nickles, pennies, user_choice):
	how_many_quarters = quarters * 0.25
	how_many_dimes = dimes * 0.10
	how_many_nickles = nickles * 0.05
	how_many_pennies = pennies * 0.01
	sum = how_many_quarters + how_many_dimes + how_many_nickles + how_many_pennies
	if sum > MENU[user_choice]['cost']:
	    change = round(sum - MENU[user_choice]['cost'], 2)
	    print(f'Your change is: ${change}')
	
	    return MENU[user_choice]['cost']
	elif sum == MENU[user_choice]['cost']:
		return MENU[user_choice]['cost']
	elif sum < MENU[user_choice]['cost']:
		print("Not enough money. Try again.")
		game_on()


# if all step successful, removes resources needed to make drink
def remove_resources(returned_choice):
	resources['water'] = resources['water'] - MENU[returned_choice]['ingredients']['water']
	resources['milk'] = resources['milk'] - MENU[returned_choice]['ingredients']['milk']
	resources['coffee'] = resources['coffee'] - MENU[returned_choice]['ingredients']['coffee']
	

# main function to call all functions and get machine going
def game_on():
	global profit # money stored in machine
	global resources # storing actual resources
	user_choice = input('Choose coffee: espresso/latte/cappuccino\nor\nChoose command: prices/status/off\n').lower()
	returned_choice = check_user_choice(user_choice, profit)
	
	if returned_choice == "off":

		raise SystemExit
	if returned_choice == "status" or returned_choice == "prices":
		game_on()

	is_enough(returned_choice) # check if enough resources 
	
	print('Insert coins.')
	quarters = int(input('How many quarters ($0.25)?\n'))
	dimes = int(input('How many dimes ($0.10)?\n'))
	nickles = int(input('How many nickles ($0.05)?\n'))
	pennies = int(input('How many pennies ($0.01)?\n'))
	profit += calculate_price(quarters, dimes, nickles, pennies, user_choice)
	
	remove_resources(returned_choice) # remove resources after payment
	
	print(f'Here is your {returned_choice}.\n')
	game_on() # starts machine over again if drink was made
	




game_on()# call to start machine
