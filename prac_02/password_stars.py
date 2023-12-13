def main():
    password = get_password()
    censor_password(password)


def censor_password(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    return password

main()