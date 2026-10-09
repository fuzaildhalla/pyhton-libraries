"""Load the 'tips' dataset from Seaborn and create a boxplot to visualize the distribution of total bill amounts by day of the week, similar to how Zomato might analyze spending patterns across weekdays.
"""


import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.boxplot(data=df, x="day", y="total_bill", color="skyblue")

plt.title("Total Bill Distribution by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")

plt.show()
