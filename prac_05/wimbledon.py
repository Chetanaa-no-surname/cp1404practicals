"""
CP1404/CP5632 Practical
wimbledon
Assuming we are not using functions, just focusing on the opening of file.
"""

FILENAME = "wimbledon.csv"
in_file = open(FILENAME, "r", encoding="utf-8-sig")

name_score = {}
countries = []
for line in in_file:
    details = line.split(",")
    name = details[2]
    if name not in name_score:
        name_score[name] = 1
    else:
        name_score[name] += 1

    country = details[1]
    if country not in countries:
        countries.append(country)

del name_score["Champion"]
print("Wimbledon Champions: ")
for line in name_score:
    print(line, name_score[line])
print("\n")

countries.remove("Country")
print("These 12 countries have won Wimbledon: ")
for country in countries:
    print(country, end=", ")
