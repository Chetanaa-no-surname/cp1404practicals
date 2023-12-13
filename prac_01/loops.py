"""
CP1404/CP5632 - Practical
Loops Program
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
print("a.")
for i in range(0, 101, 10):
    print(i, end=" ")

# b.
print("\nb.")
for i in range(20, -1, -1):
    print(i, end=" ")

#c.
print("\nc.")
stars_number = int(input("Number of stars: "))
for i in range(stars_number):
    print("*",end="")

#d.
print("\nd.")
increasing_stars = int(input("Number of increasing stars: "))
for i in range(1,increasing_stars+1):
    print("*"*i)