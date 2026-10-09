"""Use Seaborn's kdeplot to visualize the distribution of daily step counts for a week, as if analyzing data from a fitness app. Apply the 'whitegrid' theme and customize the plot color.
"""



import seaborn as sns
import matplotlib.pyplot as plt

# Daily step counts for one week
steps = [4200, 6500, 5800, 8100, 7300, 10200, 9000]

# Apply theme
sns.set_theme(style="whitegrid")

# Create KDE plot
sns.kdeplot(x=steps, color="purple", fill=True)

plt.title("Daily Step Count Distribution")
plt.xlabel("Number of Steps")
plt.ylabel("Density")

plt.show()
