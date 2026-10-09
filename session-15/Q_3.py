"""Open the Myntra product listings dataset in D-Tale, explore the interface, and use it to filter products with a price above ₹2000. Take a screenshot of the filtered view and note the number of such products."""



import pandas as pd
import dtale

# Load your dataset
df = pd.read_csv("myntra_products.csv")

# Open the dataset in D-Tale
d = dtale.show(df)
d.open_browser()

filtered = df[df["price"] > 2000]

print("Products priced above ₹2000:", len(filtered))
print(filtered)

