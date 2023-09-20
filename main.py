import random
import time


def roll_dice():

    dice_drawing = {
        1: (
            "+-------+",
            "|       |",
            "|   ●   |",
            "|       |",
            "+-------+",
        ),
        2: (
            "+-------+",
            "|       |",
            "| ●   ● |",
            "|       |",
            "+-------+",
        ),
        3: (
            "+-------+",
            "| ●     |",
            "|   ●   |",
            "|     ● |",
            "+-------+",
        ),
        4: (
            "+-------+",
            "| ●   ● |",
            "|       |",
            "| ●   ● |",
            "+-------+",
        ),
        5: (
            "+-------+",
            "| ●   ● |",
            "|   ●   |",
            "| ●   ● |",
            "+-------+",
        ),
        6: (
            "+-------+",
            "| ●   ● |",
            "| ●   ● |",
            "| ●   ● |",
            "+-------+",
        ),
    }

    roll = input("Roll the dice? (Yes/No): ")

    while roll.lower() == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("\nRolling the dice...")

        # print("Dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        print("")

        # for line in dice_drawing[dice1]:
        #     print(line)
        #     print()
        # for line in dice_drawing[dice2]:
        #     print(line)
        #     print()

        roll = input("Roll again? (Yes/No): ")


roll_dice()
