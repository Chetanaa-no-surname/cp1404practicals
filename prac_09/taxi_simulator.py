"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    option = input(">>> ").lower()
    current_taxi = None
    bill = 0.00
    while option != "q":
        if option == "c":
            print("Taxis available;")
            current_taxi = display_taxi(taxis)
        elif option == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                print(f"Your {current_taxi.name} trip will cost you ${current_taxi.get_fare():.2f}")
                bill += current_taxi.get_fare()

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        option = input(">>> ").lower()
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now: ")
    display_taxi(taxis)


def display_taxi(taxis):
    for taxi in taxis:
        print(f"{taxis.index(taxi)} - {taxi.__str__()}")
    option = int(input("Choose taxi: "))

    if option > (len(taxis)-1) or option < 0:
        print("Invalid taxi choice")
        return None
    else:
        return taxis[option]


main()
