COFFEE_MACHINE = True
MACHINE_MONEY = 0
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${MACHINE_MONEY}\n")

def money_process(add_money_to_machine):
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies

    if total < MENU[coffee_type]['cost']:
        print(f"Sorry that's not enough money. Money refunded. [${total}]")
    elif total == MENU[coffee_type]['cost']:
        add_money_to_machine += MENU[coffee_type]['cost']
        print(f"Here is your {coffee_type}. Enjoy!")
    else:
        refund= round((total - MENU[coffee_type]['cost']), 2)
        add_money_to_machine += MENU[coffee_type]['cost']
        print(f"Here is ${refund} dollars in change.")
        print(f"Here is your {coffee_type}. Enjoy!")

def available_resources():
    if resources['water'] > MENU[coffee_type]['ingredients']['water']:
        pass
    else:
        print("Don't enough water!")
        return "Error"
    if resources['coffee'] > MENU[coffee_type]['ingredients']['coffee']:
        pass
    else:
        print("Don't have enough coffee!")
        return "Error"
    if coffee_type == "cappuccino" or coffee_type == "latte":
        if resources['milk'] > MENU[coffee_type]['ingredients']['milk']:
            pass
        else:
            print("Don't have enough milk!")
            return "Error"

def resources_process():
    resources['water'] -= MENU[coffee_type]['ingredients']['water']
    resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
    if coffee_type == "espresso":
        pass
    else:
        resources['milk'] -= MENU[coffee_type]['ingredients']['milk']

while COFFEE_MACHINE:
    coffee_type = str(input(" What would you like? (espresso/latte/cappuccino): ")).lower()

    if coffee_type == "report":
        check_resources()
    elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino" :
        result = available_resources()
        if result == "Error":
            COFFEE_MACHINE = False
            break
        money_process(MACHINE_MONEY)
        resources_process()
    elif coffee_type == "off":
        print("Machine is turning off...")
        check_resources()
        COFFEE_MACHINE = False
    else:
        print("Wrong Coffee Drink Name!")
