from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_mach = MoneyMachine()
c_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}\n")
    if choice == "report":
        money_mach.report()
        c_maker.report()
    elif choice == "off":
        print("📴")
        is_on = False
    else:
        drink = menu.find_drink(order_name=choice)
        if c_maker.is_resource_sufficient(drink=drink) and money_mach.make_payment(cost=drink.cost):
            c_maker.make_coffee(order=drink)
