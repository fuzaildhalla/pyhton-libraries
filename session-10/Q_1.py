"""**1.**
Install Matplotlib in your Python environment and create a simple line plot showing the number of daily steps you took over the last 7 days. Save the chart as steps_lineplot.png."""


import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [4200, 6500, 5800, 8100, 7300, 10200, 9000]

plt.plot(days, steps, marker="o")

plt.title("Daily Steps Over the Last 7 Days")
plt.xlabel("Day")
plt.ylabel("Number of Steps")

plt.grid(True)

plt.savefig("steps_lineplot.png", dpi=150)

plt.show()
