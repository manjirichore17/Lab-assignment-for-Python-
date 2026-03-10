s = input("Enter a string: ")

print("Total number of characters:", len(s))
print("String repeated 10 times:", s * 10)

if len(s) >= 1:
    print("First character:", s[0])

if len(s) >= 3:
    print("First three characters:", s[0:3])
else:
    print("First three characters: String too short")

if len(s) >= 3:
    print("Last three characters:", s[-3:])
else:
    print("Last three characters: String too short")

print("String backwards:", s[::-1])

if len(s) >= 6:
    print("Seventh character:", s[6])
else:
    print("Seventh character: String not long enough")

if len(s) >= 2:
    print("String with first and last character removed:", s[1:-1])