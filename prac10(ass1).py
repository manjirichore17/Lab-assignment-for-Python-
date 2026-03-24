import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Complete report
print("Complete Book Report:\n", df)

# b) Books by given author
author_name = "AuthorA"
print("\nBooks by", author_name)
print(df[df["Author"] == author_name])

# c) Books by given publisher
pub_name = "Pub2"
print("\nBooks by Publisher", pub_name)
print(df[df["Publisher"] == pub_name])

# d) Cheapest & Costliest book
print("\nCheapest Book:")
print(df.loc[df["Price"].idxmin()]["Title"])

print("\nCostliest Book:")
print(df.loc[df["Price"].idxmax()]["Title"])

# e) Sort by year
print("\nSorted by Year:")
print(df.sort_values("Year"))