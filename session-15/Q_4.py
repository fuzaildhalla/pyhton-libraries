"""Given a pandas-profiling report for a Flipkart product reviews dataset, interpret and list two columns that may need cleaning or transformation before further analysis.<br><br><em><strong>Hint:</strong> Look for columns with high cardinality, missing values, or warnings in the report.</em>
"""

import pandas as pd

df = pd.read_csv(r"C:\Users\Om\OneDrive\Desktop\pandas assignments\spotify_songs.csv")

print("Missing review texts:")
print(df["review_text"].isnull().sum())

df["review_text"] = df["review_text"].fillna("")

df["review_text"] = df["review_text"].str.strip()

print("Unique product names:", df["product_name"].nunique())

df["product_name"] = (
    df["product_name"]
    .fillna("Unknown")
    .str.strip()
    .str.lower()
)

print(df[["review_text", "product_name"]].head())