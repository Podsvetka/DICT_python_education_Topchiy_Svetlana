import random
from random import choice

print("""Hello!
Welcome to the game "Rock, Paper, Scissors"
Good Luck!""")
name = input("Enter your name: ")
print(f"Hello {name}!")
elements = input(">")
voc = elements.split(",")

wordsChoice = {"rock": ["fire", "scissors", "snake", "human", "tree", "wolf", "sponge"],
           "paper": ["rock", "air", "water", "dragon", "devil", "lighting", "gun"],
           "scissors": ["snake", "human", "tree", "wolf", "sponge", "paper", "air"],
           "gun": ["rock", "fire", "scissors", "snake", "human", "tree", "wolf"],
           "lighting": ["gun", "rock", "fire", "scissors", "snake", "human", "tree"],
           "devil": ["lighting", "gun", "rock", "fire", "scissors", "snake", "human"],
           "dragon": ["devil", "lighting", "gun", "rock", "fire", "scissors", "snake"],
           "water": ["dragon", "devil", "lighting", "gun", "rock", "fire", "scissors"],
           "air": ["water", "dragon", "devil", "lighting", "gun", "rock", "fire"],
           "sponge": ["paper", "air", "water", "dragon", "devil", "lighting", "gun"],
           "wolf": ["sponge", "paper", "air", "water", "dragon", "devil", "lighting"],
           "tree": ["wolf", "sponge", "paper", "air", "water", "dragon", "devil"],
           "human": ["tree", "wolf", "sponge", "paper", "air", "water", "dragon"],
           "snake": ["human", "tree", "wolf", "sponge", "paper", "air", "water"],
           "fire": ["scissors", "snake", "human", "tree", "wolf", "sponge", "paper"]}

def stat():
    r = open('rating.txt', 'r')
    point = 0
    for x in r:
        y, z = x.split()
        if name == y:
            point = int(z)
            break
        else:
            break
while True:
    player = str(input("Enter your choice:"))
    elements = ["rock", "paper", "scissors"]
    computer = random.choice(list(wordsChoice))
    if player == "rating":
        print(f"your point: {point}")
    if player == computer:
        print("Draw")
        continue
    if player == x.get(computer):
        print(f"Sorry, but the computer chose {computer}")
        continue
    if x.get(player) == computer:
        print(f"Well done. The computer chose {computer} and failed")
        continue
    if player == "!exit":
        print("Bye")
        break
    else:
        print("Invalid input")
        continue

def extend():
    r = open('rating.txt')
    point = 0
    for x in r:
        y, z = x.split()
        if name == y:
            point = int(z)
            break
        else:
            break
    while True:
        player = input("Enter your choice: ")
        computer = random.choice(voc)
        if player == "rating":
            print(f"Your point: {point}")
        elif player == "!exit":
            print("Bye!")
            break
        elif player not in voc:
            print("This element not in choose!")
        elif player == computer:
            print(f"Draw")
        elif computer in wordsChoice.get(player):
            print(f"Well done. The computer chose {computer} and failed")
            point += 10
        elif player in wordsChoice.get(b):
            print(f"Sorry, but the computer chose {computer}")
            point += 10
        else:
            print("Invalid input")


stat = {"rock": ["scissors"], "paper": ["rock"], "scissors": ["paper"]}
if elem == "":
    print("Okay, let's start!")
    stat()
else:
    print("Okay, let's start!")
    extend()