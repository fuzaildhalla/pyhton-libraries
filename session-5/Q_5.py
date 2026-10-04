"""Concatenate two DataFrames representing 'today_orders' and 'yesterday_orders' (each with columns: order_id, item, price), and display the combined DataFrame.<br><br><em><strong>Constraint:</strong> Use pd.concat() and reset the index after concatenation.</em>"""

import pandas as pd

today_orders = pd.read_csv("today_orders.csv")
# print(today_orders)
yesterday_orders = pd.read_csv("yesterday_orders.csv")
# print(yesterday_orders)
combined_orders = pd.concat(
    [yesterday_orders,today_orders]
)
# print(combined_orders)

combined_orders = combined_orders.reset_index(drop=True)

print(combined_orders)