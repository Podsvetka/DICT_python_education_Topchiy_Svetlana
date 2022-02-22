import random


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
answerUser = input(">")

if int(answerUser) == answer:
    print("Right!")
else:
    print("Wrong!")

