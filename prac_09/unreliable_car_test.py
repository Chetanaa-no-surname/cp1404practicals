"""
CP1404/CP5632 Practical
Car class
"""

from prac_09.unreliable_car import UnreliableCar

new_car = UnreliableCar("Car 1", 100, 10)
new_car.drive(20)  # Will now get driven based on reliabiltiy
print(new_car.__str__())
