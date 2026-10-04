"""4.
You have two CSV files: 'orders.csv' (order_id, user_id, amount) and 'users.csv' (user_id, username). Load both into DataFrames using pathlib for file paths, then merge them on 'user_id' to show a combined table with username and amount."""
from pathlib import Path

current_folder = Path.cwd()

# print(current_folder)

order_path = current_folder / "orders.CSV"
users_path = current_folder / "users.CSV"

# print(order_path)
# print(users_path)

import pandas as pd

order_df = pd.read_csv(order_path)
# print(order_df.head())

users_df = pd.read_csv(users_path)
# print(users_df.head())

print(pd.merge(order_df,users_df, on = "user_id"))

