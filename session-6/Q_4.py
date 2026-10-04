"""Simulate a Zomato-style restaurant ratings dataset with some missing ratings. Use forward fill (method='ffill') to fill missing values in the ratings column, then use backward fill (method='bfill') for any remaining missing values. Show the before and after results.
"""
import pandas as pd


df = pd.read_csv(r"C:\Users\Om\Downloads\zomato_restaurant_ratings.csv")

# Before filling
print("Before:")
print(df["rating"])

# Forward fill first
df["rating"] = df["rating"].fillna(method="ffill")

# Backward fill any remaining missing values
df["rating"] = df["rating"].fillna(method="bfill")

# After filling
print("\nAfter:")
print(df["rating"])