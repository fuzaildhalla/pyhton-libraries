"""
Use ChatGPT or Copilot to generate a Python code snippet that reads a semicolon-separated CSV of Paytm transactions, detects missing values, and prints out which columns have nulls. Test the code with a small sample file and fix any errors you encounter"""


import pandas as pd

# Read the semicolon-separated CSV
df = pd.read_csv(r"C:\Users\Om\Downloads\paytm_transactions.csv", sep=";")

# Display the data
print(df)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())