class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Initialising Guitar variables """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Printing of all of guitar's values"""
        return f"{self.name} ({self.year}): ${self.cost}"

    def get_age(self):
        """Calculation of guitar's age"""
        CURRENT_YEAR = 2023
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Checking if guitar is over 50 years old"""
        OLD_AGE = 50
        age = self.get_age()
        if age >= OLD_AGE:
            return True
        else:
            return False

    def __lt__(self,other):
        """Lesser then function """
        return self.year < other.year



