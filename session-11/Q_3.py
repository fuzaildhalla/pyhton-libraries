"""Create a multi-axis chart that shows the number of Instagram followers (left y-axis) and average daily posts (right y-axis) for five influencers. Use different colors and markers for each axis.
"""


import matplotlib.pyplot as plt

# Sample data for five influencers
influencers = ["Influencer A", "Influencer B", "Influencer C",
               "Influencer D", "Influencer E"]

followers = [120000, 250000, 180000, 400000, 320000]
daily_posts = [2, 4, 3, 5, 2.5]

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(
    influencers, followers,
    color="blue", marker="o",
    linestyle="-", linewidth=2,
    label="Followers"
)
ax1.set_xlabel("Influencers")
ax1.set_ylabel("Number of Followers", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

ax2 = ax1.twinx()
ax2.plot(
    influencers, daily_posts,
    color="red", marker="s",
    linestyle="--", linewidth=2,
    label="Average Daily Posts"
)
ax2.set_ylabel("Average Daily Posts", color="red")
ax2.tick_params(axis="y", labelcolor="red")

plt.title("Instagram Followers vs Average Daily Posts")

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

plt.tight_layout()
plt.show()
