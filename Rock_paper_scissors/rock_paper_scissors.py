
while True:
    x = {"paper": "scissors", "rock": "paper", "scissors": "rock"}
    i = str(input("Enter your choice:"))
    y = x.get(i)
    if i in x:
        print(f"Sorry, but the computer chose {y}")
    else:
        print("Choose the item!")
        continue
