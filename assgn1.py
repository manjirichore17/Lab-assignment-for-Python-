# Program to store employee information and calculate salary

# Taking employee details as input
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")

# Input basic salary
basic_salary = float(input("Enter Basic Salary: "))

# Calculations
DA = 0.92 * basic_salary      # 92% of Basic Salary
HRA = 0.58 * basic_salary     # 58% of Basic Salary
TA = 0.30 * basic_salary      # 30% of Basic Salary
LIC = 500                     # Fixed deduction

# Gross Salary
gross_salary = basic_salary + DA + HRA + TA

# Net Salary
net_salary = gross_salary - LIC

# Display results
print("\n----- Employee Salary Details -----")
print("Employee Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)

print("\nBasic Salary:", basic_salary)
print("DA:", DA)
print("HRA:", HRA)
print("TA:", TA)
print("LIC Deduction:", LIC)

print("\nGross Salary:", gross_salary)
print("Net Salary:", net_salary)