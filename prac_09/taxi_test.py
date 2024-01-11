"""
CP1404/CP5632 Practical
Car class
"""

from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100)  # Removed 1.23 since variable was added
my_taxi.drive(40)
print("Taxi details: " + str(my_taxi.name) + ", Current Fare: $" + str(my_taxi.get_fare()))
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi.__str__())

print(f"${(my_taxi.get_fare()):.2f}")