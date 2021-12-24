import random


def dominoes():
    domino_pieces = [[x, y] for x in range(0, 7) for y in range(0, 7) if x >= y]
    while True:
        random.shuffle(domino_pieces)
        stock = domino_pieces[:14]
        player = domino_pieces[21:28]
        computer = domino_pieces[14:21]
        tier_list = []
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
    elif m in computer:
        computer.remove(m)
    print(f"""Stock pieces {len(stock)}
    Computer pieces {len(computer)}
    {m}
    Your pieces:
        """)
    for i, item in enumerate(player):
        print(f"{i + 1}: {item}")
    print("")
    if computer > player:
        print("Status: Computer is about to make a move. Press Enter to continue...")
    elif computer < player:
        input("Status: It's your turn to make a move. Enter your command. ")


def interface():
    print("=" * 70)
    print(f"""Stock pieces {len(stock)}
    Computer pieces {len(computer)}
    {m} 
     """)
    print("""Your pieces:
           """)
    for x, item in enumerate(player):
        print(f"{x + 1}: {item}")


def player_input(player_answer):
    turn = False
    while not turn:
        if player_answer < 0:
            tier_list.insert(0, player[-player_answer - 1])
            player.remove(player[-player_answer - 1])
            turn = True
        elif player_answer > 0:
            tier_list.append(player[player_answer - 1])
            player.remove(player[player_answer - 1])
            turn = True
        elif player_answer == 0:
            player.append(stock[0])
            del stock[0]
            turn = True

        else:
            print("Incorrect input. Enter number ")
            continue


def computer_input():
    turn = False
    while not turn:
        computer_answer = random.choice(range(-len(computer), len(computer)+1))
        if computer_answer < 0:
            tier_list.insert(0, computer[-computer_answer - 1])
            computer.remove(computer[-computer_answer - 1])
            turn = True
        elif computer_answer > 0:
            tier_list.append((computer[computer_answer - 1]))
            computer.remove(computer[computer_answer - 1])
            turn = True
        elif computer_answer == 0:
            computer.append(stock[0])
            del stock[0]
            turn = True


interface(tier_list)

win = False
while not win:
    if len(computer) > 0 and len(player) > 0:
        if choice == "Status: Computer is about to make a move. Press Enter to continue...":
            print(input("Status: Computer is about to make a move. Press Enter to continue..."))
            computer_input()
            choice = "It's your turn to make a move. Enter your command"
        else:
            move = input("Status: It's your turn to make a move. Enter your command. ")
            try:
                int(move)
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            else:
                if int(move) not in range(-len(player), len(player) + 1):
                    print("you don't have that much")
                    continue
                if int(move) in range(-len(computer), len(computer)+1):
                    player_input(int(move))
                    choice = "Status: Computer is about to make a move. Press Enter to continue..."
                else:
                    print("Invalid input. Please try again.")
                    continue
    interface(tier_list)
    if len(player) == 0:
        print("""The game is over. You won!
        You have 0 pieces""")
        break
    elif len(computer) == 0:
        print("The game is over. The computer won!")
        break
    elif tier_list[0][0] == tier_list[-1][-1]:
        score = 0
        for i in range(len(tier_list)):
            for s in tier_list[i]:
                if s == tier_list[0][0]:
                    score += 1
        if score == 8:
            print("The game is over. It's a draw!")
            break