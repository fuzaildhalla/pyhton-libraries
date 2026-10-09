"""1.
Download a small sample of your recent Zomato order history as a CSV (or create a mock CSV with restaurant names and order dates), then use pandas' duplicated() function to find and print any duplicate orders based on restaurant name and date."""

import pandas as pd

df = pd.read_csv(r"C:\Users\Om\Downloads\zomato_orders_duplicates_practice.csv")

# df = df.duplicated()
new_df = (df[df.duplicated()])


print(new_df)