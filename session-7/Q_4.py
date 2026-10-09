"""
You have a DataFrame of Flipkart product prices stored as strings with currency symbols (e.g., '₹1,299'). Convert this column to numeric type using pandas, ensuring all non-numeric characters are removed.<br><br><em><strong>Hint:</strong> Use str.replace() and astype().</em>"""

import pandas as pd

df = pd.DataFrame({
    "product": ["Phone", "Laptop", "Headphones"],
    "price": ["₹1,299", "₹54,999", "₹2,499"]
})

df["price"] = df["price"].str.replace(r"[^\d.]", "", regex=True)


df["price"] = df["price"].astype(float)

print(df)

