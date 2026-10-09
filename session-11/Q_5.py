"""Add a custom text annotation to a Matplotlib chart showing Flipkart's monthly sales, marking the highest sales point with the label 'Big Billion Days'.<br><br><em><strong>Hint:</strong> Use the ax.annotate() function to place the label at the correct data point.</em>
"""


import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 120, 150, 130, 300, 180]

fig, ax = plt.subplots()
ax.plot(months, sales, marker="o")

ax.annotate("Big Billion Days", xy=("May", 300),
            xytext=("Mar", 280),
            arrowprops=dict(arrowstyle="->"))

ax.set_title("Flipkart Monthly Sales")
ax.set_ylabel("Sales (₹)")
plt.show()