print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")



print( "Write how many ml of water the coffee machine has:")
availableWater = int(input(">"))
print("Write how many ml of milk the coffee machine has:")
availableMilk = int(input(">"))
print("Write how many grams of coffee beans the coffee machine has:")
availableBeans = int(input(">"))

maxCoffee = min(availableWater//200, availableMilk//50, availableBeans//15)

print("Write how many cups of coffee you will need:")
cups = int(input(">"))

water =  200*cups
milk = 50*cups
beans =  15*cups

if water <= availableWater and milk <= availableMilk and beans <= availableBeans:

    if maxCoffee == 1:
        print("Yes, I can make that amount of coffee")
    elif maxCoffee > cups:
        print("Yes, I can make that amount of coffee (and even {} more than that)".format(maxCoffee-cups))
else:
    print("No, I can make only {} cups of coffee".format(maxCoffee))
