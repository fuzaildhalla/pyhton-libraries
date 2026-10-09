
"""Use plt.subplots() to create a 2x2 grid of subplots and plot four different types of charts (line, bar, scatter, and pie) using any sample data of your choice."""

import matplotlib.pyplot as plt

# Sample data
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
steps = [4000, 6000, 5000, 8000, 10000]

apps = ["Instagram", "YouTube", "Spotify", "Netflix"]
usage = [3, 5, 2, 4]

ratings = [3.5, 4.0, 4.5, 3.8, 4.8]
prices = [200, 350, 500, 280, 600]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].plot(days, steps, marker="o", color="blue")
axes[0, 0].set_title("Daily Steps")
axes[0, 0].set_xlabel("Day")
axes[0, 0].set_ylabel("Number of Steps")

axes[0, 1].bar(apps, usage, color="orange")
axes[0, 1].set_title("Daily App Usage")
axes[0, 1].set_xlabel("App")
axes[0, 1].set_ylabel("Hours")
axes[0, 1].tick_params(axis="x", rotation=15)

axes[1, 0].scatter(ratings, prices, color="green")
axes[1, 0].set_title("Ratings vs Price")
axes[1, 0].set_xlabel("Rating")
axes[1, 0].set_ylabel("Price (₹)")

axes[1, 1].pie(
    usage,
    labels=apps,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 1].set_title("App Usage Distribution")

# Adjust layout and display
plt.tight_layout()
plt.show()
