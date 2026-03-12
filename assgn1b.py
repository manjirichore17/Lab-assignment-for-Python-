# Program to store Vendor details and calculate Annual Purchase

# Taking Vendor details
name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

# Monthly purchases
jan = float(input("Enter January Purchase: "))
feb = float(input("Enter February Purchase: "))
mar = float(input("Enter March Purchase: "))
apr = float(input("Enter April Purchase: "))
may = float(input("Enter May Purchase: "))
jun = float(input("Enter June Purchase: "))
jul = float(input("Enter July Purchase: "))
aug = float(input("Enter August Purchase: "))
sep = float(input("Enter September Purchase: "))
oct = float(input("Enter October Purchase: "))
nov = float(input("Enter November Purchase: "))
dec = float(input("Enter December Purchase: "))

# Annual purchase calculation
annual_purchase = (jan + feb + mar + apr + may + jun +
                   jul + aug + sep + oct + nov + dec)

# Display Vendor Report
print("\n------ Vendor Annual Purchase Report ------")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Total Annual Purchase:", annual_purchase)