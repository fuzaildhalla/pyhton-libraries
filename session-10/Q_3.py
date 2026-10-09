"""Build a bar chart that shows the number of orders you or your friends placed on Swiggy, Zomato, and Domino’s in the last month. Use different colors for each bar and add a legend.
"""


import matplotlib.pyplot as plt

apps = ["Swiggy", "Zomato", "Domino's"]
orders = [8, 12, 5]

colors = ["orange", "red", "blue"]

plt.bar(apps, orders, color=colors, label="Number of Orders")

plt.title("Food Delivery Orders in the Last Month")
plt.xlabel("Food Delivery App")
plt.ylabel("Number of Orders")

plt.legend()
plt.show()
