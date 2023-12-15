from prac_07.guitar import Guitar

in_file = open("guitars.csv", "r")

guitars = []

for line in in_file:
    guitar = (line.strip("\n")).split(",")
    guitars.append(Guitar(guitar[0], guitar[1], guitar[2]))

guitars = sorted(guitars)

for guitar in guitars:
    print(f"{guitar.name} was bought in {guitar.year} and costs {guitar.cost}")

