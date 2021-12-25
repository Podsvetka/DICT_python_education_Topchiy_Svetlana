import random

name = str(input("Enter your name:"))
print(f"Hello: {name}")
point = 0
r = open('rating.txt', 'r')
for context in r:
    nick, score = context.split()
    if name == nick:
        point = int(score)

while True:
    x = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
    player = str(input("Enter your choice:"))
    computer = random.choice([*x.keys()])
    if player == "rating":
        print(f"your score: {point}")
    if player == computer:
        print("Draw")
        point += 50
        continue
    if player == x.get(computer):
        print(f"Sorry, but the computer chose {computer}")
        continue
    if x.get(player) == computer:
        print(f"Well done. The computer chose {computer} and failed")
        point += 100
        continue
    if player == "exit":
        print("Bye")
        break
    else:
        print("Invalid input")
        continue
