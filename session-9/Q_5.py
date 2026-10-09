"""Create a new feature called 'is_weekend' in your DataFrame that marks True if an order was placed on Saturday or Sunday, and False otherwise.<br><br><em><strong>Constraint:</strong> Do not use any external libraries except pandas and numpy.</em>"""


import pandas as pd

# Read the CSV file
df = pd.read_csv(r"C:\Users\Om\OneDrive\Desktop\pandas assignments\flipkart_orders_with_date_parts.csv")

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Create the is_weekend feature
df["is_weekend"] = df["order_date"].dt.dayofweek >= 5

# Display the first 10 rows
print(df.head(10))
