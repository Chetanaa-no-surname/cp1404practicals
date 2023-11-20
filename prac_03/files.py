# Part 1.
OUT_FILE = "name.txt"
out_file = open(OUT_FILE, "w")

name = input("Enter name: ").title()
out_file.write(name + "\n")

out_file.close()

# Part 2.
OUT_FILE = "name.txt"
out_file = open(OUT_FILE,"r")

name = out_file.readline()
print(f"Your name is {name}")

out_file.close()



