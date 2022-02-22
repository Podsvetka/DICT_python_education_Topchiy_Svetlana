import random
from collections import Counter

def dominoes():
    domino_pieces = [[x, y] for x in range(0, 7) for y in range(0, 7) if x >= y]
    while True:
        random.shuffle(domino_pieces)
        stock = domino_pieces[:14]
        player = domino_pieces[21:28]
        computer = domino_pieces[14:21]
        tier_list = []
    while True:
        for i in player:
            if i == i[::-1]:
                tier_list.append(i)
        for i in computer:
            if i == i[::-1]:
                tier_list.append(i)
        if len(tier_list) >= 1:
            break
        else:
            pass
    if len(tier_list) > 1:
        m = max(tier_list)
    else:
        m = tier_list
    if m in player:
        player.remove(m)
        choice = "Status: Computer is about to make a move. Press Enter to continue..."
    else:
        computer.remove(m)
        choice = "Status: It's your turn to make a move. Enter your command. "


    tier_list = [m]

def interface(m):
    print("=" * 70)
    print(f"""Stock pieces {len(stock)}
    Computer pieces {len(computer)}
    If you don't have a suitable dominance press 0 and you get 1 domino.
     """)
    if len(m) <= 6:
        print(m)
    elif len(m) > 6:
        print(f"""{m[:3]}...{m[-3:]}""")
    print("""
    Your pieces:
           """)
    for x, item in enumerate(player):
        print(f"{x + 1}: {item}")

def check():
    while True:
        player_answer = input("Status: It's your turn to make a move. Enter your command. ")
        try:
            int(player_answer)
            if int(player_answer) not in range(-len(player), len(player) + 1):
                print("you don't have that much")
                continue
            else:
                return player_answer
        except ValueError:
            print("Invalid input. Please try again.")
            continue

def player_input():
    turn = False
    player_answer = int(check())
    while not turn:
        if player_answer < 0:
            if player[abs(player_answer) - 1][-1] == tier_list[0][0]:
                tier_list.insert(0, player[-player_answer - 1])
                player.remove(player[-player_answer - 1])
                turn = True
            elif player[abs(player_answer) - 1][0] == tier_list[0][0]:
                tier_list.insert(0, player[-player_answer - 1][::-1])
                player.remove(player[-player_answer - 1])
                turn = True

        elif player_answer > 0:
            if player[player_answer - 1][0] == tier_list[-1][1]:
                tier_list.append(player[player_answer - 1])
                player.remove(player[player_answer - 1])
                turn = True
            elif player[player_answer - 1][1] == tier_list[-1][1]:
                tier_list.append(player[player_answer - 1][::-1])
                player.remove(player[player_answer - 1])
                turn = True
            else:
                print("wrong one")
                player_answer = int(check())


        elif player_answer == 0:
            player.append(stock[0])
            del stock[0]
            turn = True
        else:
            print("Incorrect input. Enter number ")
            continue

def logic():
    a = []
    for j in list(computer):
        for x in j:
            a += [x]
    b = []
    for j in list(tier_list):
        for x in j:
            b += [x]
    result = dict(Counter(a + b))
    new_dict = []
    for x, j in computer:
        num = result.get(x) + result.get(j)
        new_dict.append([[x, j], num])
    sorted(new_dict, key=lambda y: y[1], reverse=True)
    computer.clear()
    for x in new_dict:
        computer.append(x[0])
    print(computer)
    return computer



def computer_input():
    turn = False
    while not turn:
        computer_answer = random.choice(range(-len(computer), len(computer) + 1))
        if computer_answer < 0:
            if computer[abs(computer_answer) - 1][-1] == tier_list[0][0]:
                tier_list.insert(0, computer[abs(computer_answer) - 1])
                computer.remove(computer[abs(computer_answer) - 1])
                turn = True
            elif computer[abs(computer_answer) - 1][0] == tier_list[0][0]:
                tier_list.insert(0, computer[abs(computer_answer) - 1][::-1])
                computer.remove(computer[abs(computer_answer) - 1])
                turn = True
        elif computer_answer > 0:
            if computer[computer_answer - 1][0] == tier_list[-1][1]:
                tier_list.append(computer[computer_answer - 1])
                computer.remove(computer[computer_answer - 1])
                turn = True
            elif computer[computer_answer - 1][1] == tier_list[-1][1]:
                tier_list.append(computer[computer_answer - 1][::-1])
                computer.remove(computer[computer_answer - 1])
                turn = True
        else:
            computer.append(stock[0])
            del stock[0]
            turn = True



while True:
    if len(computer) > 0 and len(player) > 0:
        if choice == "Status: Computer is about to make a move. Press Enter to continue...":
            print(input("Status: Computer is about to make a move. Press Enter to continue..."))
            computer_input()
            choice = "Status: It's your turn to make a move. Enter your command"
        else:
            player_input()
            choice = "Status: Computer is about to make a move. Press Enter to continue..."


interface(tier_list)
if len(player) == 0:
    print("The game is over. You won!")
    print("You have 0 pieces")
    exit
elif len(computer) == 0:
    print("The game is over. The computer won!")
    exit
elif tier_list[0][0] == tier_list[-1][-1]:
        score = 0
        for i in range(len(tier_list)):
            for s in tier_list[i]:
                if s == tier_list[0][0]:
                    score += 1
        if score == 8:
            print("The game is over. It's a draw!")
            exit
elif len(stock) == 0:
        if choice == "Status: Computer is about to make a move. Press Enter to continue...":
                print("The game is over. You won!")
                exit
        elif choice == "Status: It's your turn to make a move. Enter your command":
                print("The game is over. The computer won!")
                exit