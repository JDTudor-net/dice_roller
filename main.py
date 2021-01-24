import random


def diceroll():
    inputt = input("Pick a number to roll dice up to: ")
    dice_roll = random.randint(1, int(inputt))
    print(dice_roll)
    diceroll()


if __name__ == '__main__':
    diceroll()
