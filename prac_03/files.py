# Part 1.
OUT_FILE = "name.txt"
out_file = open(OUT_FILE, "w")

name = input("Enter name: ").title()
out_file.write(name + "\n")

out_file.close()

# Part 2.
OUT_FILE = "name.txt"
out_file = open(OUT_FILE, "r")

name = out_file.readline()
print(f"Your name is {name}")

out_file.close()

# Part 3.
FILENAME = "numbers"
out_file = open(FILENAME, "r")

total = 0
line_number = 0
for line in out_file:
    if line_number < 2:
        total += int(line)
    line_number += 1
print(f"Result is {total}")
