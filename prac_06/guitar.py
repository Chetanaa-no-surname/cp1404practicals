"""
CP1404/CP5632 Practical
Guitar

Estimated Time: 45 mins
Actual Time:  38 mins
"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """ """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost}"

    def get_age(self):
        CURRENT_YEAR = 2023
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False


