"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    num_of_months = int(input("How many months? "))

    incomes = get_incomes(num_of_months)

    print_report(incomes, num_of_months)


def get_incomes(num_of_months):
    incomes = []
    for month in range(1, num_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes


def print_report(incomes, num_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()