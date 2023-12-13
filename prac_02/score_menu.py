"""
CP1404/CP5632 - Practical 2
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASSABLE_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90


def main():
    """Menu,Input and Output"""
    score_input = float(input("Enter score: "))
    score = validate_score(score_input)

    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score_input = float(input("Enter score: "))
            score = validate_score(score_input)
        elif choice == "P":
            result = determine_grade(score)
            print(f"You have a score of {score}. The result is {result}.")
        elif choice == "S":
            print_stars(int(score))
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">>>").upper()
    print("Goodbye.")


def print_stars(score):
    """Prints stars"""
    for i in range(score):
        print("*", end=" ")
    print("\n")


def validate_score(score):
    """Determines score is valid"""
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter valid score: "))
    return score

def determine_grade(score):
    """Categorizes which grade the score is in"""
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

main()