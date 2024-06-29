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
income = {"money": 0}


def espresso(getorder):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    totaltender = round(quarters + dimes + nickles + pennies, 2)
    change = round(totaltender - MENU["espresso"]["cost"], 2)
    if totaltender < 1.5:
        print("Sorry that's not enough moeny, Money refunded.")
    else:
        value1 = resources["water"] >= MENU["espresso"]["ingredients"]["water"]
        value2 = resources["coffee"] >= MENU["espresso"]["ingredients"][
            "coffee"]
        if value1 and value2:
            print(f"Here is ${change} in change.")
            print(f"Here is your {getorder} enjoy!")
            income["money"] = income.get("money") + MENU["espresso"]["cost"]
            remaining_water = resources.get(
                'water') - MENU["espresso"]["ingredients"]["water"]
            remaining_coffee = resources.get(
                'coffee') - MENU["espresso"]["ingredients"]["coffee"]
            resources["water"] = remaining_water
            resources["coffee"] = remaining_coffee
        else:
            if not value1:
                print("Sorry there is not enough water.")
            if value2 == False:
                print("Sorry there is not enough coffee.")

    getorder = input("What would you like? (espresso/latte/cappuccino): ")
    checkInput(getorder)


def latte(getorder):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10 
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    totaltender = round(quarters + dimes + nickles + pennies, 2)
    change = round(totaltender - MENU["latte"]["cost"], 2)
    if totaltender < 2.5:
        print("Sorry that's not enough moeny, Money refunded.")
    else:
        value1 = resources["water"] >= MENU["latte"]["ingredients"]["water"]
        value2 = resources["coffee"] >= MENU["latte"]["ingredients"][
        "coffee"]
        value3 = resources["milk"] >= MENU["latte"]["ingredients"][
    "milk"]
        if value1 and value2 and value3:
            print(f"Here is ${change} in change.")
            print(f"Here is your {getorder} enjoy!")
            income['money'] = income.get('money') + MENU["latte"]["cost"]
            remaining_water = resources.get(
            'water') - MENU["latte"]["ingredients"]["water"]
            remaining_coffee = resources.get(
            'coffee') - MENU["latte"]["ingredients"]["coffee"]
            remaining_milk = resources.get(
            'milk') - MENU["latte"]["ingredients"]["milk"]
            resources["water"] = remaining_water
            resources["coffee"] = remaining_coffee
            resources["milk"] = remaining_milk
        else:
            if not value1:
                print("Sorry there is not enough water.")
            if value2 == False:
                print("Sorry there is not enough coffee.")
            if value3 == False:
                print("Sorry there is not enough milk.")
                

    getorder = input("What would you like? (espresso/latte/cappuccino): ")
    checkInput(getorder)


def cappuccino(getorder):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    totaltender = round(quarters + dimes + nickles + pennies, 2)
    change = round(totaltender - MENU["cappuccino"]["cost"], 2)
    if totaltender < 3.0:
        print("Sorry that's not enough moeny, Money refunded.")
    else:
        value1 = resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]
        value2 = resources["coffee"] >= MENU["cappuccino"]["ingredients"][
            "coffee"]
        value3 = resources["milk"] >= MENU["cappuccino"]["ingredients"][
        "milk"]
        if value1 and value2 and value3:
            print(f"Here is ${change} in change.")
            print(f"Here is your {getorder} enjoy!")
            income['money'] = income.get('money') + MENU["cappuccino"]["cost"]
            remaining_water = resources.get(
            'water') - MENU["cappuccino"]["ingredients"]["water"]
            remaining_coffee = resources.get(
            'coffee') - MENU["cappuccino"]["ingredients"]["coffee"]
            remaining_milk = resources.get(
            'milk') - MENU["cappuccino"]["ingredients"]["milk"]
            resources["water"] = remaining_water
            resources["coffee"] = remaining_coffee
            resources["milk"] = remaining_milk
        else:
            if not value1:
                print("Sorry there is not enough water.")
            if value2 == False:
                print("Sorry there is not enough coffee.")
            if value3 == False:
                print("Sorry there is not enough milk.")
    getorder = input("What would you like? (espresso/latte/cappuccino): ")
    checkInput(getorder)


def checkInput(getorder):
    if getorder == "report":
        report()
    elif getorder == "espresso":
        espresso(getorder)
    elif getorder == "latte":
        latte(getorder)
    elif getorder == "cappuccino":
        cappuccino(getorder)


def report():
    print(
        f"Water: {resources.get('water')}\nMilk: {resources.get('milk')}\nCoffee: {resources.get('coffee')}\nMoney: {income.get('money')}"
    )
    getorder = input("What would you like? (espresso/latte/cappuccino): ")
    checkInput(getorder)


getorder = input("What would you like? (espresso/latte/cappuccino): ")
checkInput(getorder)
