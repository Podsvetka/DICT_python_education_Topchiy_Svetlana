import random

print("""HANGMAN
The game will be available soon.""")

listWords=["python", "java", "javascript", "php"]

selectWord = random.choice(listWords)
writeWord = input("Guess the word: > ")

if writeWord == selectWord:
    print("You survived!")
else :
    print("You lost!")
