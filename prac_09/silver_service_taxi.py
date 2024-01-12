"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fancy = fanciness
        self.price_per_km = Taxi.price_per_km * self.fancy

    def __str__(self):
        """Return a string like a Taxi but with fanciness too."""
        price = (self.price_per_km * self.current_fare_distance) + self.flagfall
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall