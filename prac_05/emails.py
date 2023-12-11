"""
CP1404/CP5632 Practical
Emails
"""

def main():
    email = input("Email: ")
    emails = {}
    while email != "":
        name = get_name(email).title()
        name = " ".join(name.split('.'))
        check_name = input(f"Is your name {name}? (Y/n) ").lower()
        if check_name != "y" and check_name != "":
            name = input("Name: ").title()
        emails[name] = email
        email = input("Email: ")
    print("\n")
    for i in emails.items():
        print(f"{i[0]} ({i[1]})")


def get_name(email):
    name = email.split("@")
    return name[0]

main()