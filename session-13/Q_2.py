"""Using the 'flights' dataset from Seaborn, generate a heatmap showing the correlation between months and years based on the number of passengers.<br><br><em><strong>Hint:</strong> Use pivot_table to reshape the data before plotting the heatmap.</em>
"""

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("flights")

pivot_data = df.pivot_table(
    index="month",
    columns="year",
    values="passengers"
)

sns.heatmap(pivot_data, annot=True, fmt="d", cmap="YlGnBu")

plt.title("Monthly Flight Passengers by Year")
plt.xlabel("Year")
plt.ylabel("Month")
plt.show()