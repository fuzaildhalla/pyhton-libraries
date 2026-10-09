"""Using a dataset of Flipkart product reviews (at least columns: 'rating', 'category'), create a bar plot showing the count of reviews for each rating (1-5 stars) using matplotlib or seaborn.
"""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Om\Downloads\flipkart_reviews.csv")

rating_counts = df["rating"].value_counts().reindex(
    [1, 2, 3, 4, 5], fill_value=0
)

rating_counts.plot(kind="bar")

plt.title("Flipkart Reviews by Rating")
plt.xlabel("Rating (Stars)")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.show()
