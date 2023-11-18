"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            converted_fahrenheit = convert_to_fahrenheit(celsius)
            print(f"Result: {converted_fahrenheit:.2f} F")
        elif choice == "F":
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            fahrenheit_input = float(input("Fahrenheit: "))
            converted_celsius = convert_to_celsius(fahrenheit_input)
            print(f"Result: {converted_celsius:.2f}C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_to_celsius(fahrenheit):
    celsius_calculated = 5 / 9 * (fahrenheit - 32)
    return celsius_calculated

main()