from musician import Musician


class Band(Musician):
    """Band class"""

    def __init__(self, band_name=""):
        super().__init__()
        self.band = []
        self.band_name = band_name

    def add(self, musician):
        self.band.append(musician)

    def __str__(self):
        """Returns Band details"""
        musicians = []
        for person in self.band:
            musicians.append(person)
        return f"{self.band_name} ({musicians})"

    def play(self):
        printed = []
        for person in self.band:
            printed.append(Musician.play(person))
        return ("\n".join(printed))
