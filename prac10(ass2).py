import pandas as pd

# Create data
data = {
    "State": ["Maharashtra", "Gujarat", "Karnataka", "Rajasthan", "Kerala"],
    "Area": [307713, 196024, 191791, 342239, 38863],
    "Population": [112374333, 60439692, 61095297, 68548437, 33406061]
}

df = pd.DataFrame(data)

# a) Complete info
print("State Information:\n", df)

# b) Largest Area
print("\nState with Largest Area:")
print(df.loc[df["Area"].idxmax()]["State"])

# c) Largest Population
print("\nState with Largest Population:")
print(df.loc[df["Population"].idxmax()]["State"])

# d) Population Density
df["Density"] = df["Population"] / df["Area"]
print("\nWith Density:\n", df)

# e) Highest Density
print("\nState with Highest Density:")
print(df.loc[df["Density"].idxmax()]["State"])