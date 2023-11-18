"""
CP1404/CP5632 - Practical 2
"""
import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    score = validate_score()
    result = determine_grade(score)
    print(result)


def get_random_score():
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    result = determine_grade(random_score)
    print(f"Your score is {random_score}. Your result is {result}")


def validate_score():
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter valid score: "))
    return score


def determine_grade(score):
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()
get_random_score()