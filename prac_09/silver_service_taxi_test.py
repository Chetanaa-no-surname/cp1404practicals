"""
CP1404/CP5632 Practical
Silver Service Taxi class
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

new_taxi = SilverServiceTaxi("New1",100,2)
print(new_taxi.__str__())
new_taxi.drive(18)
print(new_taxi.__str__())
print(f"${(new_taxi.get_fare()):.2f}")
