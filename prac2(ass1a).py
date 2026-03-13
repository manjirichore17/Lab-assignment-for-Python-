# Program to calculate current using Ohm's Law

# Take input from user
voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter Resistance (R): "))

# Calculate current
current = voltage / resistance

# Display result
print("Current (I) =", current, "Ampere")