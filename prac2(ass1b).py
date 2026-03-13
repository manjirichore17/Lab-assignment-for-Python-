# Program to calculate current and show its nature

# Take input from user
voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter Resistance (R): "))

# Calculate current using Ohm's Law
current = voltage / resistance

# Display current
print("Current (I) =", current, "Ampere")

# Check nature of current
if current < 0.5:
    print("Low current")
elif current >= 0.5 and current <= 2:
    print("Normal current")
else:
    print("High current")