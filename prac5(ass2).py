# Take prices of items
prices = tuple(map(int, input("Enter prices of sold items: ").split()))

print("Prices:", prices)

# a) Total number of items sold
print("Total number of items sold:", len(prices))

# b) Cheapest item price
print("Cheapest item price:", min(prices))

# c) Costliest item price
print("Costliest item price:", max(prices))

# d) Price list in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items
costliest = max(prices)
count = prices.count(costliest)

print("Number of costliest items sold:", count)