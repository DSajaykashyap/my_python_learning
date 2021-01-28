from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        if is_enough_ingredients:
            cost_of_coffee = drink.cost
            print(f'Please pay Rs {cost_of_coffee}')
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_payment_successful:
            coffee_maker.make_coffee(drink)
    else:
        print('Please type correctly')
