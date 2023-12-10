"""
CP1404/CP5632 Practical
Programming language

Estimated Time: 30 mins
Actual Time: 18 mins
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialising the Programming language"""
        self.name = name.title()
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Checking if langauge is dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """Printing all values of the language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
