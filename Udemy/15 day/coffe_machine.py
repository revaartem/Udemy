# espresso, latte, cappuccino


MENU = {
    "1": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
        "name": "espresso",
    },
    "2": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
        "name": "latte",
    },
    "3": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
        "name": "cappuccino"
    },
    'report': 0,
    'off': 0,

}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

power_switch = True


def drink_choice():
    switch = True
    while switch:
        choice_drink = input(f'''Please, select your drink and enter number of it.
1 - Espresso (1.5$)
2 - Latte (2.5$)
3 - Cappuccino (3$)
Enter number here: ''')
        if choice_drink not in MENU:
            print('Wrong number, try again.')
        else:
            switch -= 1
            return choice_drink


def resources_check(drink_res: str):
    if MENU[drink_res]["ingredients"]['water'] > resources["water"]:
        print('Sorry there is not enough water.')
        return False
    elif MENU[drink_res]["ingredients"]["coffee"] > resources["coffee"]:
        print('Sorry there is not enough coffee.')
        return False
    elif (drink_res == '2' or drink_res == '3') and MENU[drink_res]["ingredients"]["milk"] > resources["milk"]:
        print('Sorry there is not enough milk.')
        return False
    else:
        resources["water"] -= MENU[drink_res]["ingredients"]['water']
        resources["coffee"] -= MENU[drink_res]["ingredients"]["coffee"]
        if drink_res == '2' or drink_res == '3':
            resources["milk"] -= MENU[drink_res]["ingredients"]["milk"]
        return True


def enter_coins():
    switch = True
    while switch:
        print('Please, insert coins.')
        try:
            quarters = int(input('How many quarters: '))
            dimes = int(input('How many dimes: '))
            nickles = int(input('How many nickles: '))
            pennies = int(input('How many pennies: '))
        except ValueError:
            print('Invalid enter, try again.')
            continue
        suma = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
        switch -= 1
        return suma


def payment_check(price: float, money: float):
    if money == price:
        return True
    elif money > price:
        print(f'Here is {round(money - price, 2)}$ change.')
        return True
    elif money < price:
        print('Sorry, that`s not enough money. Money refund.')
        return False


def refill(resources_to_fill):
    water = int(input('How much water do you want to fill (in ml.): '))
    coffee = int(input('How much coffee do you want to fill (in g.): '))
    milk = int(input('How much milk do you want to fill (in ml.): '))
    resources_to_fill['water'] += water
    resources_to_fill['coffee'] += coffee
    resources_to_fill['milk'] += milk
    return resources_to_fill


def report_check():
    print(f'''
Water - {resources["water"]}
Coffee - {resources["coffee"]}
Milk - {resources["milk"]}
Money - {resources["money"]}$
''')


while power_switch:

    drink = drink_choice()
    if drink == 'off':
        power_switch -= 1
        continue

    elif drink == 'report':
        report_check()
        continue

    if not resources_check(drink):
        refill_decision = input('Do you want to refill machine? Type Yes or No: ')
        if refill_decision.lower() == 'yes':
            refill(resources)
            continue
        else:
            continue

    summa = enter_coins()
    if not payment_check(MENU[drink]['cost'], summa):
        continue
    resources["money"] += MENU[drink]['cost']
    print(f'Here is your drink -☕{MENU[drink]["name"]}☕. Enjoy!')
