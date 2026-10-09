"""Plot a comparison of average delivery times for Zomato, Swiggy, and Domino's using a bar chart, and style each bar with a different color, linestyle, and linewidth using Matplotlib plot styling options.
"""


import matplotlib.pyplot as plt

apps = ["Zomato", "Swiggy", "Domino's"]
delivery_times = [30, 25, 35]

colors = ["red", "orange", "blue"]

bars = plt.bar(apps, delivery_times, color=colors)

linestyles = ["solid", "dashed", "dotted"]
linewidths = [2, 3, 4]

for bar, style, width in zip(bars, linestyles, linewidths):
    bar.set_linestyle(style)
    bar.set_linewidth(width)
    bar.set_edgecolor("black")

plt.title("Average Food Delivery Time Comparison")
plt.xlabel("Food Delivery App")
plt.ylabel("Average Delivery Time (minutes)")

plt.show()
