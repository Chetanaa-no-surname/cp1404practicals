from prac_07.guitar import Guitar


def main():
    guitars = get_file_data("guitars")
    print_data(guitars)
    guitars = sorted(guitars)
    print("\nResorted guitars list:\n")
    print_data(guitars)


def get_file_data(name):
    in_file = open(f"{name}.csv", "r")
    guitars = []
    for line in in_file:
        guitar = (line.strip("\n")).split(",")
        guitars.append(Guitar(guitar[0], guitar[1], guitar[2]))
    return guitars


def print_data(guitars):
    for guitar in guitars:
        print(f"{guitar.name} was bought in {guitar.year} and costs {guitar.cost}")


main()