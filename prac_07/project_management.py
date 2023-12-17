"""
CP1404/CP5632 Practical
"""

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
def main()
    print(MENU)
    option = input(">>> ").upper()
    while option != "Q":
        if option == "L":
            load_project()
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

def load_project():
    pass

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