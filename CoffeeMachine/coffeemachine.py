print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
""")

STATE_COMMAND = 0
STATE_BUY = 1
STATE_FILL_1 = 2
STATE_FILL_2 = 3
STATE_FILL_3 = 4
STATE_FILL_4 = 5
STATE_FILL_5 = 6


class CoffeeMachine:
    availableWater = 400
    availableMilk = 540
    availableBeans = 15
    availableMoney = 550
    availableCup = 9
    exit = False
    state = STATE_COMMAND
    action = ""
    typeCoffee = ""

    def __init__(self):
        self.reset()

    def printStatus(self):
        print("""The coffee machine has:
        {} of water
        {} of milk
        {} of coffee beans
        {} of disposable cups
        {} of money""".format(self.availableWater,
                              self.availableMilk,
                              self.availableBeans,
                              self.availableCup,
                              self.availableMoney))

    def reset(self):
        self.state = STATE_COMMAND
        print("\nWrite action (buy, fill, take, remaining, exit):")

    def input(self, text):
        if self.state == STATE_COMMAND:
            self.action = text

            if self.action == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
                self.state = STATE_BUY

            elif self.action == "fill":
                print("Write how many ml of water you want to add:")
                self.state = STATE_FILL_1

            elif self.action == "take":
                print("I gave you {}".format(self.availableMoney))
                self.availableMoney = 0
                self.reset()

            elif self.action == "remaining":
                self.printStatus()
                self.reset()

            elif self.action == "exit":
                self.exit = True
                self.state = STATE_COMMAND

        elif self.state == STATE_BUY:
            self.typeCoffee = text

            if self.typeCoffee == "back":
                self.reset()
                return
            else:
                typeCoffee = int(self.typeCoffee)

            maxCoffee = min(self.availableWater // 200, self.availableMilk // 50, self.availableBeans // 15)

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

            if water <= self.availableWater and milk <= self.availableMilk and beans <= self.availableBeans:

                if maxCoffee == 1:
                    print("Yes, I can make that amount of coffee")
                elif maxCoffee > 1:
                    print("Yes, I can make that amount of coffee (and even {} more than that)".format(
                        maxCoffee - 1))

                self.availableMoney += price

            else:
                print("No, I can make only {} cups of coffee".format(maxCoffee))

            self.reset()

        elif self.state == STATE_FILL_1:
            addWater = int(text)
            self.availableWater += addWater

            print("Write how many ml of milk you want to add:")
            self.state = STATE_FILL_2

        elif self.state == STATE_FILL_2:
            addMilk = int(text)
            self.availableMilk += addMilk

            print("Write how many grams of coffee beans you want to add:")
            self.state = STATE_FILL_3

        elif self.state == STATE_FILL_3:
            addBeans = int(text)
            self.availableBeans += addBeans

            print("Write how many disposable coffee cups you want to add:")
            self.state = STATE_FILL_4

        elif self.state == STATE_FILL_4:
            addCups = int(text)
            self.availableCup += addCups

            self.reset()


coffeeMachine = CoffeeMachine()

while True:
    text = input(">")
    coffeeMachine.input(text)

    if coffeeMachine.exit:
        break
