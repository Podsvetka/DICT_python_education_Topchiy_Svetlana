import random

print("""HANGMAN
The game will be available soon.""")

listWords=["python", "java", "javascript", "php"]

selectWord = random.choice(listWords)

help = ''
for i in range(len(selectWord)):
    if i < 3:
        help += selectWord[i]
    else:
        help +="-"

writeWord = input("Guess the word: "+help+"> ")

if writeWord == selectWord:
    print("You survived!")
else :
    print("You lost!")
