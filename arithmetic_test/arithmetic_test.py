import random


countMark = 5
rightMark = 0

print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")

level = 0
while True:
    l = input(">")
    if l in ["1", "2"]:
        level = int(l)
        break
    else :
        print("Incorrect format")


for n in range(countMark):

    answer = 0
    if level == 1:
        a = random.randrange(2,9)
        oper = random.choice(["+","-","*"])
        b = random.randrange(2,9)

        if oper == "+":
            answer = a+b
        elif oper == "-":
            answer = a-b
        elif oper == "*":
            answer = a*b

        print(f"{a} {oper} {b}")
    elif level == 2:
        a = random.randrange(11, 29)
        print(a)
        answer = a**2

    answerUser = 0
    while(True):
        try:
            answerUser = int(input(">"))
            break
        except:
            print("Wrong format! Try again")

    if answerUser == answer:
        print("Right!")
        rightMark += 1
    else:
        print("Wrong!")

print(f"Your mark is {rightMark}/{countMark}. Would you like to save the result? Enter yes or no.")
answer = input(">")
if answer == "yes":
    print("What is your name?")
    name = input(">")
    f = open("results.txt", "a+")

    description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
    f.write(f"{name}: {rightMark}/{countMark} in level {level} ({description}).\n")
    f.close()
    print('The results are saved in "results.txt".')




