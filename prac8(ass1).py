# Read from file and write in uppercase

# open source file
f1 = open("input.txt", "r")

# read content
data = f1.read()

# convert to uppercase
data_upper = data.upper()

# open new file
f2 = open("output.txt", "w")

# write uppercase data
f2.write(data_upper)

# close files
f1.close()
f2.close()

print("File converted to uppercase successfully!")