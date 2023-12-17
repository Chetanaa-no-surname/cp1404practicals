"""
CP1404/CP5632 Practical
"""
import datetime

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    print(MENU)
    option = input(">>> ").upper()
    while option != "Q":
        if option == "L":
            # name = input("Enter file name: ")
            datas = load_project()
        elif option == "S":
            save_project()
        elif option == "D":
            display_project()
        elif option == "F":
            sort_project()
        elif option == "A":
            add_data()
        elif option == "U":
            update_data()
        else:
            print("Invalid option ")
        option = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")


def load_project(name="projects"):
    in_file = open(f"{name}.txt", "r")
    datas = []
    for line in in_file:
        line_data = line.strip('\t').strip('\n')
        line_data = line_data.split("	")  # Did this as two lines to make it clearer
        datas.append(line_data)
    datas = datas[1:]
    changed_to_datetime(datas)
    return datas


def changed_to_datetime(datas):
    for data in datas:
        date = datetime.datetime.strptime(data[1], "%d/%m/%Y").date()
        data[1] = date
    return datas


def save_project():
    pass


def display_project():
    pass


def sort_project():
    pass


def add_data():
    pass


def update_data():
    pass


main()
