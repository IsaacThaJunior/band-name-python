from coffee_data import MENU, resources

turn_on = True
profit = 0


def is_there_resource(ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""

    for stuffs in ingredients:
        if ingredients[stuffs] > resources[stuffs]:
            print(f"Sorry there is not enough {stuffs}.")
            return False

    return True


def coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction(money, drinks_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money >= drinks_cost:
        change = round(money - drinks_cost, 2)
        print(f'Here is {change} in change')
        global profit
        profit += drinks_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")


while turn_on:
    user_input = input('What would you like? (espresso/latte/cappuccino): ')
    if user_input == 'off':
        turn_on = False
    elif user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        if is_there_resource(drink['ingredients']):
            money = coins()
            if transaction(money, drink['cost']):
                make_coffee(user_input, drink['ingredients'])
