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


while True:
    action = input("yes?")
    if action == "yes":
        interface()
        dominoes()
    else:
        break