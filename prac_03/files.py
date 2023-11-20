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
FILENAME = "numbers.txt"
in_file = open(FILENAME, "r")

total = 0
two_lines = in_file.readlines()[0:2]

for line in two_lines:
    total += int(line.strip("\n"))

print(f"Result is {total}")

out_file.close()

# Part 4.
FILENAME = "numbers.txt"
in_file = open(FILENAME, "r")

total = 0

for line in in_file:
    total += int(line.strip("\n"))
print(f"Total is {total}")

out_file.close()




