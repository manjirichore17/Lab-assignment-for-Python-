# Copy file without comments

source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

# open files
f1 = open(source, "r")
f2 = open(destination, "w")

for line in f1:
    # skip comments
    if not line.strip().startswith("#"):
        f2.write(line)

# close files
f1.close()
f2.close()

# print both files
print("\nSource File Content:")
f1 = open(source, "r")
print(f1.read())
f1.close()

print("\nDestination File Content (without comments):")
f2 = open(destination, "r")
print(f2.read())
f2.close()