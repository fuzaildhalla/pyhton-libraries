"""Create a boxplot for the 'order_amount' column from a Swiggy orders dataset using matplotlib, and visually identify any outliers present.<br><br><em><strong>Hint:</strong> Use plt.boxplot() and label your axes for clarity.</em>
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Om\Downloads\zomato_ratings_with_outliers.csv")

plt.boxplot(df["rating"])

plt.title("rating")
plt.xlabel("Rating")
plt.ylabel("Rating_count")

plt.show()

                    