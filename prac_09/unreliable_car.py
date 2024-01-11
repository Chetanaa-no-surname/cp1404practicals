"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise a reliability, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliable = reliability

    def drive(self, distance):
        """Driving like parent but includes unreliability"""
        if self.reliable > random.randint(0, 100):
            super().drive(distance)
        else:
            distance = 0
        return distance

    def __str__(self):
        """Return a string like a Car but with reliability."""
        return f"{super().__str__()}, Reliability: {self.reliable}%"


