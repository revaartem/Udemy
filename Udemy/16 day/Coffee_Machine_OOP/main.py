from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

while True:
    customer_choice = input(f'What would you like? ({drinks.get_items()}): ')

    if customer_choice.lower() == 'off':
        break

    elif customer_choice.lower() == 'report':
        machine.report()
        money.report()
        continue

    elif not Menu.find_drink(drinks, customer_choice.lower()):
        print('Try again.')
        continue

    drink_card = Menu.find_drink(drinks, customer_choice.lower())

    if not CoffeeMaker.is_resource_sufficient(machine, drink_card):
        continue

    if not money.make_payment(drink_card.cost):
        continue

    machine.make_coffee(drink_card)