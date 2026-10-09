"""Customize a Matplotlib figure by creating a plot with two subplots: one line plot showing your daily Instagram screen time for a week, and one bar chart showing the number of posts you liked each day. Add appropriate titles, axis labels, and save the figure as social_media_usage.png.<br><br><em><strong>Hint:</strong> Use plt.subplots() to create multiple axes in one figure.</em>
"""



import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
screen_time = [60, 90, 75, 120, 100, 150, 130]  
posts_liked = [20, 35, 25, 40, 30, 50, 45]      

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(days, screen_time, marker="o", color="purple")
axes[0].set_title("Daily Instagram Screen Time")
axes[0].set_xlabel("Day")
axes[0].set_ylabel("Screen Time (minutes)")

axes[1].bar(days, posts_liked, color="orange")
axes[1].set_title("Instagram Posts Liked Each Day")
axes[1].set_xlabel("Day")
axes[1].set_ylabel("Number of Posts Liked")

plt.tight_layout()

# Save the complete figure
plt.savefig("social_media_usage.png", dpi=150)

plt.show()
