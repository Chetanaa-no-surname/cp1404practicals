"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the input is not an integer, for either numerator or denominator
2. When will a ZeroDivisionError occur?
When the integer 0 is entered as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
We can to a check and ask for a valid denominator to avoid this error since
mathematically we can't change this error.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")