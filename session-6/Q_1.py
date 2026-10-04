"""Download a sample CSV file of IPL player stats (include columns like player name, runs, matches, and some missing values). Load it into a pandas DataFrame and use isnull() and notnull() to print how many missing values are present in each column.
"""

import pandas as pd

IPL_csv = pd.read_csv(r"C:\Users\Om\Downloads\ipl_player_stats.csv")
# print(IPL_csv)

print("missing values :",
      pd.isnull(IPL_csv).sum())
print("existing values :" ,
      pd.notnull(IPL_csv).sum())