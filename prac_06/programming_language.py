"""
CP1404/CP5632 Practical
Programming language

Estimated Time: 30 mins
Actual Time:
"""


class ProgrammingLanguage:

    def __int__(self, name="", typing="", reflection="", year=0):
        self.name = name.title()
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False
