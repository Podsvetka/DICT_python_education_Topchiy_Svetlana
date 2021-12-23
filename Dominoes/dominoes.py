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
    print(f"Stock pieces {[stock]}")
    print(f"Player pieces {[player]}")
    print(f"Computer pieces {[computer]}")
    print(f"Domino snake {m}")
    if computer > player:
        print("Status: Computer")
    elif player > computer:
        print("Status: Player")


while True:
    choice = input("yes?")
    if choice == "yes":
        dominoes()
    else:
        break