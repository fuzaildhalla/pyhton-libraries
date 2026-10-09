"""2.
Load a CSV file containing order dates from a Flipkart-style order history (column: 'order_date', format: 'YYYY-MM-DD HH:MM:SS'). Extract the year, month, and weekday for each order and add them as new columns in the DataFrame."""


import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv(r"C:\Users\Om\Downloads\flipkart_order_dates.csv")

# Step 2: Convert order_date into datetime format
df["order_date"] = pd.to_datetime(
    df["order_date"],
    format="%Y-%m-%d %H:%M:%S"
)

df["year"] = df["order_date"].dt.year

df["month"] = df["order_date"].dt.month

df["weekday"] = df["order_date"].dt.day_name()

print(df.head())

print(df)



