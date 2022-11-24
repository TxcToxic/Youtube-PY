import random
import string


def genPwd(lenght: int):
    chars = string.digits + string.punctuation + string.ascii_letters
    if lenght > 100:
        return "Too long!"
    elif lenght < 2:
        return "Too short!"
    pwd = "".join(random.choice(chars) for _ in range(lenght))
    return str(pwd)


def genPwd2():
    firstWords = ["tiny", "huge", "little", "tall"]
    secondWords = ["turtle", "horse", "man", "woman"]
    number = random.randrange(0, 1000)
    firstWord = random.choice(firstWords)
    secondWord = random.choice(secondWords)
    password = firstWord + secondWord + str(number)
    return password


if __name__ == "__main__":
    print(genPwd(50) + " | " + genPwd2())
    print("^^^^^^ this is safer!")
