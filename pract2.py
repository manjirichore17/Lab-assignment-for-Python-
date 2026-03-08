t = float(input("Enter temperature in degree Celsius: "))

if t < -273.15:
    print("Invalid temperature: below absolute zero")

elif t == -273.15:
    print("Temperature is absolute zero")

elif t > -273.15 and t < 0:
    print("Temperature is below freezing")

elif t == 0:
    print("Temperature is at freezing point")

elif t > 0 and t < 100:
    print("Temperature is in the normal range")

elif t == 100:
    print("Temperature is at the boiling point")

elif t > 100:
    print("Temperature is above the boiling point")