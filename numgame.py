import random


def game(userInput: str, mode: int = 1):
    if mode == 1:
        number = random.randint(1, 10)
    elif mode == 2:
        number = random.randint(1, 50)
    elif mode == 3:
        number = random.randint(1, 100)
    else:
        print("ERROR: Mode 1 - 3 | You gave: {}".format(mode))
        return "Mode incorrect"
    if userInput == number:
        print("You won!")
        return "User won"
    else:
        print("\nYou lose!\n"
              "The number was > {}".format(number))
        return "User lose"


if __name__ == "__main__":
    usr = input("Enter a number > ")
    game(userInput=usr)
