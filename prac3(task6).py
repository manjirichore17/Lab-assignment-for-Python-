# Task 6 - Star Pattern

rows = 5

# Upper part
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Lower part
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()