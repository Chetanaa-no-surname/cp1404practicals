"""
CP1404/CP5632 Practical
"""
import datetime
from project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    name = "projects"  # will be fixed as this unless a load option is chosen and then data will change
    datas = load_project(name)
    print(MENU)
    option = input(">>> ").upper()
    while option != "Q":
        if option == "L":
            name = input("Enter file name: ")
            datas = load_project(name)
        elif option == "S":
            name = input("Enter file name: ")
            save_project(name, datas)
        elif option == "D":
            display_project(datas)
        elif option == "F":
            sort_project(datas)
        elif option == "A":
            datas = add_data(datas)
        elif option == "U":
            update_data()
        else:
            print("Invalid option ")
        option = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")


def load_project(name):
    in_file = open(f"{name}.txt", "r")
    datas = []
    object_datas = []
    for line in in_file:
        line_data = line.strip('\t').strip('\n')
        line_data = line_data.split("	")  # Did this as two lines to make it clearer
        datas.append(line_data)
    datas = datas[1:]
    changed_to_datetime(datas)
    in_file.close()

    for data in datas:
        object_datas.append(Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4])))
    return object_datas


def changed_to_datetime(datas):
    for data in datas:
        date = datetime.datetime.strptime(data[1], "%d/%m/%Y").date()
        data[1] = date
    return datas


def save_project(name, datas):
    in_file = open(f"{name}.txt", "w")
    in_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage")
    for data in datas:
        in_file.write(
            "\n{0}	{1}	{2}	{3}	{4}".format(data.name, data.date.strftime("%d/%m/%Y"), data.priority,
                                                       data.cost, data.completion))
    in_file.close()


def display_project(datas):
    incomplete = []
    complete = []
    for data in datas:
        if data.completion == 100:
            complete.append(data)
        else:
            incomplete.append(data)

    print("Incomplete projects:")
    incomplete = sorted(incomplete)
    for data in incomplete:
        print("{0}, start: {1}, priority {2}, estimate: ${3}, completion: {4}%".format(data.name,
                                                                                       data.date.strftime("%d/%m/%Y"),
                                                                                       data.priority, data.cost,
                                                                                       data.completion))

    print("Completed projects: ")
    complete = sorted(complete)
    for data in complete:
        print("{0}, start: {1}, priority {2}, estimate: ${3}, completion: {4}%".format(data.name,
                                                                                       data.date.strftime("%d/%m/%Y"),
                                                                                       data.priority, data.cost,
                                                                                       data.completion))


def sort_project(datas):
    date = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    for data in datas:
        if data.date >= date:
            print("{0}, start: {1}, priority {2}, estimate: ${3}, completion: {4}%".format(data.name,
                                                                                           data.date.strftime(
                                                                                               "%d/%m/%Y"),
                                                                                           data.priority, data.cost,
                                                                                           data.completion))


def add_data(datas):
    print("Let's add a new project")
    name = input("Name:")
    date = input("Start date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    datas.append(Project(name,date,int(priority),float(cost),int(completion)))
    return datas

def update_data():
    pass


main()
