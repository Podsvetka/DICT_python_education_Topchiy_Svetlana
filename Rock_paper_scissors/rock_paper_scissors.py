import random
while True:
    x = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
    player = str(input("Enter your choice:"))
    computer = random.choice([*x.keys()])
    if player == computer:
        print("Draw")
        continue
    if player == x.get(computer):
        print(f"Sorry, but the computer chose {computer}")
        continue
    if x.get(player) == computer:
        print(f"Well done. The computer chose {computer} and failed")
        continue
    if player == "exit":
        print("Bye")
        break
    else:
        print("Invalid input")
        continue
