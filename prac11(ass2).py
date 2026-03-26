import matplotlib.pyplot as plt

companies = ["IBM","Amdocs","Google"]
data = [40,30,50]

# Bar
plt.bar(companies, data)
plt.show()

# Pie
plt.pie(data, labels=companies)
plt.show()

# Doughnut
plt.pie(data)
circle = plt.Circle((0,0),0.5)
plt.gca().add_artist(circle)
plt.show()