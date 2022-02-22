import random


countMark = 5
rightMark = 0


for n in range(countMark):



    a = random.randrange(2,9)
    oper = random.choice(["+","-","*"])
    b = random.randrange(2,9)
    answer = 0

    if oper == "+":
        answer = a+b
    elif oper == "-":
        answer = a-b
    elif oper == "*":
        answer = a*b

    print(f"{a} {oper} {b}")
    answerUser = 0
    while(True):
        try:
            answerUser = int(input(">"))
            break
        except:
            print("Incorrect format")


    if int(answerUser) == answer:
        print("Right!")
        rightMark += 1
    else:
        print("Wrong!")

print(f"Your mark is {rightMark}/{countMark}")

