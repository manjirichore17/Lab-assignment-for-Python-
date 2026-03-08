# Code

N = input("Name: ")
D = input("Department: ")
Y = input("Year: ")
S = input("Semester: ")
Se = input("Section: ")
RN = input("Roll No: ")

S1 = float(input("Enter marks for Subject 1: "))
S2 = float(input("Enter marks for Subject 2: "))
S3 = float(input("Enter marks for Subject 3: "))
S4 = float(input("Enter marks for Subject 4: "))
S5 = float(input("Enter marks for Subject 5: "))

T = S1 + S2 + S3 + S4 + S5
P = float(T/5)

print("STUDENT MARKSHEET")
print("Name:", N)
print("Department:", D)
print("Year:", Y)
print("Semester:", S)
print("Section:", Se)
print("Roll Number:", RN)

print("Subject 1 Marks:", S1)
print("Subject 3 Marks:", S3)
print("Subject 4 Marks:", S4)
print("Subject 5 Marks:", S5)

print("Total Marks:", T)
print(f"Percentage: {P:.2f}%")