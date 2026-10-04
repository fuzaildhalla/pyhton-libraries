"""3.
For the 'runs' column in your IPL player stats DataFrame, use fillna() to replace missing values with the mean of the column. Print the updated column to verify the changes."""

import pandas as pd


IPL_csv = pd.read_csv(r"C:\Users\Om\Downloads\ipl_player_stats.csv")

mean_runs = IPL_csv["runs"].mean()

print(mean_runs)

IPL_csv["runs"] = IPL_csv["runs"].fillna(mean_runs)

print(IPL_csv["runs"])

