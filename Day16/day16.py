from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def make_coffee():
    end_program = False
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while not end_program:
        choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        if choice == "off":
            end_program = True
            continue
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
            continue
        else:
            drink = menu.find_drink(choice)
            if not drink:
                continue
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


make_coffee()
