"""
CP1404/CP5632 Practical
Guitar Testing
"""

from prac_06.guitar import Guitar


def main():
    """Testing guitar OOP"""
    guitar_1 = Guitar("Guitar 1", 1923, 20.5)
    guitar_2 = Guitar("Guitar 2", 2000, 500.23)

    print(f"{guitar_1.name} get_age() - Expected 100, Got {guitar_1.get_age()}")
    print(f"{guitar_2.name} get_age() - Expected 23, Got {guitar_2.get_age()}")

    print(f"{guitar_1.name} is_vintage() - Expected True, Got {guitar_1.is_vintage()}")
    print(f"{guitar_2.name} is_vintage() - Expected False Got {guitar_2.is_vintage()}")


main()
