"""Take a dataset of Zomato restaurant listings (with 'average_cost_for_two' and 'user_rating' columns) and create a scatterplot to visualize the relationship between cost and user rating.<br><br><em><strong>Hint:</strong> Use seaborn's scatterplot() function and label the axes clearly.</em>
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "average_cost_for_two": [500, 350, 800, 600, 1200, 700, 450, 1800, 250, 1500, 300, 950],
    "user_rating": [4.2, 3.8, 4.4, 4.0, 4.5, 4.1, 3.9, 4.7, 3.5, 4.3, 4.0, 4.2]
}

df = pd.DataFrame(data)

sns.scatterplot(
    data=df,
    x="average_cost_for_two",
    y="user_rating"
)

plt.title("Restaurant Cost vs User Rating")
plt.xlabel("Average Cost for Two")
plt.ylabel("User Rating (out of 5)")
plt.show()