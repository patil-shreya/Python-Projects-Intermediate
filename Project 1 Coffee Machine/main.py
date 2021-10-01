from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
make_coffee = CoffeeMaker()
count_money = MoneyMachine()

coffee_make = True

while coffee_make:
    coffee_menu = menu.get_items()
    user_choice = input(f"What would you like? ({coffee_menu}): ")
    if user_choice == "off":
        coffee_make = False
    elif user_choice == "report":
        make_coffee.report()
        count_money.report()
    else:
        coffee = menu.find_drink(user_choice)
        if make_coffee.is_resource_sufficient(coffee):
            if count_money.make_payment(coffee.cost):
                make_coffee.make_coffee(coffee)






