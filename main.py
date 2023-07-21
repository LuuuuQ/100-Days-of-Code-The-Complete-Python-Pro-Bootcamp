from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    order_name = input(f"Dostępne produkty to: {menu.get_items()}")

    if order_name == "report":
        coffee_maker.report()
        money_machine.report()

    elif order_name == "off":
        print("Wyłączanie\nTU DU Du du")
        is_on = False

    else:
        drink = menu.find_drink(order_name)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





