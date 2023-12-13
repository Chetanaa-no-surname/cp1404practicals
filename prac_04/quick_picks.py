"""
CP1404/CP5632 Practical
"Quick Pick" Lottery Ticket Generator
"""
import random
MINIMUM = 1
MAXIMUM = 45
PER_LINE = 6


def main():
    """Input number of picks wanted and output picks"""
    rounds = int(input("How many quick picks? "))
    for i in range(rounds):
        line = get_line()
        for x in line:
            print(f"{x:>2}", end=" ")
        print("")


def get_line():
    """Getting the random 6 numbers per line"""
    line = []
    for x in range(PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in line:
            number = random.randint(MINIMUM, MAXIMUM)
        line.append(number)
    return line


main()
