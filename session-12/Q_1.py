"""Install Seaborn in your Python environment and use it to create a histplot showing the distribution of delivery times (in minutes) for 50 Zomato food orders. Generate random data if needed.
"""


import seaborn as sns
import matplotlib.pyplot as plt
import random

delivery_times = [random.randint(15, 60) for _ in range(50)]

sns.histplot(delivery_times, bins=10, color="orange", edgecolor="black")

plt.title("Zomato Delivery Time Distribution")
plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Number of Orders")

plt.show()
