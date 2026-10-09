"""Download a small dataset of IPL cricket matches (CSV or Excel), load it into a pandas DataFrame, and perform univariate analysis by printing the summary statistics (mean, median, min, max, std) for the 'total_runs' column.
"""


import pandas as pd

# Load the CSV file
df = pd.read_csv(r"C:\Users\Om\Downloads\ipl_matches.csv")

# Analyze the total_runs column
runs = df["total_runs"]

print("Mean:", runs.mean())
print("Median:", runs.median())
print("Minimum:", runs.min())
print("Maximum:", runs.max())
print("Standard Deviation:", runs.std())
