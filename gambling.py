import random
"""
Gamblers ruin problem finding the gambler gain profit or loss of money
"""


def gamble_play():
    money = 100
    goal = 200
    gamble = 200
    wins = 0

    for i in range(gamble):
        stake = 1
        if 0 < stake < goal:
            if random.randint(0, 1) == 1:
                money += 1
                print("money won", money)
            else:
                money -= 1
                print("money loss", money)
        if money == goal:
            wins = wins + 1

    print(":", wins)
    print("wins", (wins * 100 // gamble))

if __name__ == '__main__':
    gamble_play()
