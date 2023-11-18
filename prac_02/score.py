"""
CP1404/CP5632 - Practical 2
"""
import random

"""All Magic Numbers"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    """Input and Output function"""
    score = float(input("Enter score: "))
    score = validate_score(score)
    result = determine_grade(score)
    print(result)
    #Adding random_score
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    random_result = determine_grade(random_score)
    print(f"Your score is {random_score}.The result is {random_result}")


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