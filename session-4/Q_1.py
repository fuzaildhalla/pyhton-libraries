"""1.
Download a sample CSV file of IPL cricket match scores from Kaggle or any public dataset, and use pd.read_csv() to load it into a DataFrame. Print the first 5 rows to verify the data."""

import pandas as pd

csv_load = pd.read_csv(r"C:\Users\Om\Downloads\ipl_match_scores_sample.csv")
pd.DataFrame(csv_load)

print(csv_load.head())