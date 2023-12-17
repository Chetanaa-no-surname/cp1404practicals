from prac_07.guitar import Guitar


def main():
    guitars = get_file_data("guitars")
    print_data(guitars)
    guitars = sorted(guitars)
    print("\nResorted guitars list:\n")
    print_data(guitars)

    new_guitars = []

    name = input("\nEnter guitar name: ")
    while name != "":
        year = input("Enter year guitar was bought: ")  # Inputted as str so that  __lt__ can be carried out
        cost = float(input("Enter cost of guitar: "))
        guitars.append(Guitar(name, year, cost))
        new_guitars.append([name, year, cost])
        name = input("Enter guitar name: ")

    guitars = sorted(guitars)
    print_data(guitars)
    write_to_file(new_guitars,"guitars")


def get_file_data(name):
    in_file = open(f"{name}.csv", "r")
    guitars = []
    for line in in_file:
        guitar = (line.strip("\n")).split(",")
        guitars.append(Guitar(guitar[0], guitar[1], guitar[2]))
    in_file.close()
    return guitars


def print_data(guitars):
    for guitar in guitars:
        print(f"{guitar.name} was bought in {guitar.year} and costs {guitar.cost}")


def write_to_file(datas,name):
    in_file = open(f"{name}.csv", "a")
    for data in datas:
        in_file.write(f"{data[0]},{data[1]},{data[2]}")
    in_file.close()



main()
