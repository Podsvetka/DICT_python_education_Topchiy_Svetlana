import random

print("""HANGMAN
The game will be available soon.""")

listWords=["python", "java", "javascript", "php"]

while True :
    print('Type "play" to play the game, "exit" to quit:')
    enter = input("> ")

    if enter == "play":

        guesses = 8

        selectWord = random.choice(listWords)
        listLetter = set(selectWord)
        listUseLetter = set()

        help = list("-")*len(selectWord)
        while True:
            print("".join(help))
            writeLetter = input("Input a letter: > ")

            if len(writeLetter) > 1 or len(writeLetter) == 0:
                print("You should input a single letter ")
                continue
            elif writeLetter.isupper() :
                print('Please enter a lowercase English letter')
                continue

            if writeLetter in listLetter :
                listLetter.remove(writeLetter)

                for i in range(len(selectWord)) :
                    if selectWord[i] == writeLetter :
                        help[i] = writeLetter
            else :

                if writeLetter in listUseLetter:
                    print("You've already guessed this letter.")
                else:
                    print("That letter doesn't appear in the word")
                    guesses -= 1

            if writeLetter in selectWord :
                listUseLetter.add(writeLetter)

            if len(listLetter) == 0 :
                print("You survived!")
                break
            elif guesses==0:
                print("You lost!")
                break

        print("Thanks for playing!\nWe'll see how well you did in the next stage")

    elif enter == "exit":
        break