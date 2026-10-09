"""Install the pandas-profiling library and generate a profile report for the 'Spotify Top 100 Songs' dataset (CSV available on Kaggle); open the HTML report and note any missing values or data type issues.
"""


import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("Spotify 2010 - 2019 Top 100.csv")

profile = ProfileReport(
    df,
    title="Spotify Top 100 Songs Report",
    explorative=True
)

profile.to_file("spotify_profile_report.html")

print("DATA TYPES:")
print(df.dtypes)

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nTotal missing values:", df.isnull().sum().sum())
