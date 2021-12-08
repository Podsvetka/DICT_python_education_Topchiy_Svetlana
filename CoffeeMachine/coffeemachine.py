print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
""")

availableWater = 400
availableMilk = 540
availableBeans = 15
availableMoney = 550
availableCup = 9


def printStatus():
    print("""The coffee machine has:
    {} of water
    {} of milk
    {} of coffee beans
    {} of disposable cups
    {} of money""".format(availableWater, availableMilk, availableBeans, availableCup, availableMoney))

printStatus()

while True:

    print("Write action (buy, fill, take, remaining, exit):")
    action = input(">")

    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
        typeCoffee = input(">")

        if typeCoffee == "back":
            continue
        else:
            typeCoffee = int(typeCoffee)

        maxCoffee = min(availableWater // 200, availableMilk // 50, availableBeans // 15)

        water = milk = beans = price = 0

        if typeCoffee == 1:
            water = 250
            milk = 0
            beans = 16
            price = 4
        elif typeCoffee == 2:
            water = 350
            milk = 75
            beans = 20
            price = 7
        elif typeCoffee == 3:
            water = 200
            milk = 100
            beans = 12
            price = 6

        if water <= availableWater and milk <= availableMilk and beans <= availableBeans:

            if maxCoffee == 1:
                print("Yes, I can make that amount of coffee")
            elif maxCoffee > 1:
                print("Yes, I can make that amount of coffee (and even {} more than that)".format(maxCoffee - 1))

            availableMoney += price
            printStatus()

        else:
            print("No, I can make only {} cups of coffee".format(maxCoffee))

    elif action =="fill":
        print("Write how many ml of water you want to add:")
        addWater = int(input(">"))
        print("Write how many ml of milk you want to add:")
        addMilk = int(input(">"))
        print("Write how many grams of coffee beans you want to add:")
        addBeans = int(input(">"))
        print("Write how many disposable coffee cups you want to add:")
        addCups = int(input(">"))

        availableWater += addWater
        availableMilk += addMilk
        availableBeans += addBeans
        availableCup += addCups
        printStatus()
    elif action == "take":
        print("I gave you {}".format(availableMoney))
        availableMoney = 0
        printStatus()
    elif action == "remaining":
        printStatus()
    elif action == "exit":
        break