#Part 1.
OUT_FILE = "name.txt"
out_file = open(OUT_FILE, "a")

name = input("Enter name: ")
out_file.write(name+"\n")

out_file.close()



