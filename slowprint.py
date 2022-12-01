import sys
from time import sleep


def slowprint(value: str, breakLineEnd: bool = True, breakLineStart: bool = False):
    if breakLineStart:
        sys.stdout.write("\n")
        sys.stdout.flush()
    for l in value:
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(.01)
    if breakLineEnd:
        sys.stdout.write("\n")
        sys.stdout.flush()


if __name__ == "__main__":
    slowprint("Hey :) how are you?")
