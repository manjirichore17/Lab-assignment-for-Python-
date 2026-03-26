import pandas as pd

# Create data
df = pd.DataFrame({
    "ID":[101,102,103,104],
    "Name":["Ram","Shyam","Amit","Neha"],
    "Dept":["Auto","IT","Auto","HR"],
    "Role":["Dev","Dev","Manager","Dev"]
})

# a) Employees in Automotive
print("Automotive Employees:")
print(df[df["Dept"]=="Auto"])

# b) Employee details by ID
eid = 101
print("\nEmployee with ID 101:")
print(df[df["ID"]==eid])

# c) All Developers
print("\nDevelopers:")
print(df[df["Role"]=="Dev"])