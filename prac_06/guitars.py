"""
CP1404/CP5632 Practical
Guitar Testing
"""
from prac_06.guitar import Guitar


def main():
    guitar_names = []
    print("My guitars!")
    name = input("Name: ")

    guitar_names.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_names.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        guitar_names.append(Guitar(name, year, cost))
        name = input("Name: ")

    print("\n"+"... snip ..."+"\n")

    print("These are my guitars: ")
    count = 1
    for guitar in guitar_names:
        vintage_string = " (vintage)" if guitar.is_vintage() == True else ""
        print(f"Guitar {count}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
        count += 1

main()