# Task 5 pattern

rows = 5

for i in range(1, rows + 1):
    
    # print spaces
    for j in range(rows - i):
        print(" ", end=" ")
    
    # print stars
    for k in range(2*i - 1):
        print("*", end=" ")
        
    print()