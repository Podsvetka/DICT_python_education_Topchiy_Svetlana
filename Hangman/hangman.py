import random

print("""HANGMAN
The game will be available soon.""")

listWords=["python", "java", "javascript", "php"]
guesses = 8

selectWord = random.choice(listWords)
listLetter = set(selectWord)
listUseLetter = set()

help = list("-")*len(selectWord)
while True:
    print("".join(help))
    writeLetter = input("Input a letter: > ")

    if len(writeLetter) > 1 or len(writeLetter) == 0:
        print("You have to write one symbol ")
        continue

    if writeLetter in listLetter :
        listLetter.remove(writeLetter)

        for i in range(len(selectWord)) :
            if selectWord[i] == writeLetter :
                help[i] = writeLetter
    else :
        guesses -= 1
        if writeLetter in listUseLetter:
            print("No improvements")
        else:
            print("That letter doesn't appear in the word")

    if writeLetter in selectWord :
        listUseLetter.add(writeLetter)

    if len(listLetter) == 0 :
        print("You survived!")
        break
    elif guesses==0:
        print("You lost!")
        break

print('''Thanks for playing!
We'll see how well you did in the next stage''')