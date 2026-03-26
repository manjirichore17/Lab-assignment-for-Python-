import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]
profit = [2000,3000,2500,4000]

# Line Plot
plt.plot(months, profit)
plt.show()

# Multiline
facecream = [1000,1200,1100,1300]
facewash = [800,900,850,950]
plt.plot(months, facecream)
plt.plot(months, facewash)
plt.show()

# Bar Chart
plt.bar(months, facecream)
plt.show()

# Pie Chart
plt.pie([sum(facecream), sum(facewash)], labels=["Cream","Wash"])
plt.show()