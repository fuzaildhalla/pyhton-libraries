""".
Using the loaded IPL player stats DataFrame, apply dropna(axis=0, how='any') to remove all rows with any missing data and display the shape of the DataFrame before and after dropping."""

import pandas as pd

IPL_csv = pd.read_csv(r"C:\Users\Om\Downloads\ipl_player_stats.csv")
print("before:" ,IPL_csv.shape)
IPL_csv = IPL_csv.dropna(axis=0, how="any") 
print("after : ",IPL_csv.shape)
print(IPL_csv)