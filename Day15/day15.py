from day15_art import MENU, resources

end_program = False
money_machine = 0



def sum_coins():
    coins = 0
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    coins = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return coins


def check_coins(coins, flavor):
    if coins >= MENU[flavor]["cost"]:
        change = coins - MENU[flavor]["cost"]
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {flavor}☕ Enjoy!")
        return 1
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def check_resources(flavor):
    for ingredient in MENU[flavor]["ingredients"]:
        if resources[ingredient] < MENU[flavor]["ingredients"][ingredient] :
            print(f"Sorry there is not enough {ingredient}.")
            return 0
    return 1

def discont_resources(coins, flavor):
    global money_machine
    money_machine += coins
    for ingredient in resources:
        if ingredient in MENU[flavor]["ingredients"]:
            qnt = MENU[flavor]["ingredients"][ingredient]
            resources[ingredient] -= qnt


def make_coffee():
    global money_machine
    while not end_program:
        flavor = input("What would you like? (espresso/latte/cappuccino): ")
        if flavor.lower() == "report":
            print(f"Water: {resources['water']}ml\nMilk:  {resources['milk']}ml"
                  f"\nCofeee: {resources['coffee']}g\nMoney: ${money_machine:.2f}")
            continue

        if check_resources(flavor):
            coins = sum_coins()
            if check_coins(coins, flavor):
                discont_resources(coins, flavor)


make_coffee()
