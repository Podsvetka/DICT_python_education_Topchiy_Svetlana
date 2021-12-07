print("""HANGMAN
The game will be available soon.""")

word = "python"
writeWord = input("Guess the word: > ")
if writeWord == word :
    print("You survived!")
else :
    print("You lost!")