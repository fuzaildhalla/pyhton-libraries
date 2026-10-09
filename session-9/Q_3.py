"""3.
Set the 'order_date' column as the index of your DataFrame and use resampling to calculate the total number of orders placed each week.<br><br><em><strong>Hint:</strong> Use df.resample('W').size() after setting the datetime index.</em>"""



import pandas as pd

df = pd.read_csv(r"C:\Users\Om\Downloads\flipkart_order_dates.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

df = df.set_index("order_date")

weekly_orders = df.resample("W").size()

print(weekly_orders)
