"""Use the seaborn 'pairplot' function on a Spotify songs dataset (with at least 'danceability', 'energy', 'valence', and 'popularity' columns) to visualize pairwise relationships between these features. Briefly describe one interesting pattern you observe.
"""



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "danceability": [0.80, 0.65, 0.72, 0.40, 0.55, 0.88, 0.35, 0.70],
    "energy":       [0.75, 0.60, 0.85, 0.30, 0.45, 0.90, 0.25, 0.70],
    "valence":      [0.78, 0.55, 0.70, 0.20, 0.40, 0.85, 0.25, 0.65],
    "popularity":   [85, 70, 90, 45, 60, 95, 35, 78]
}

df = pd.DataFrame(data)
df.to_csv("spotify_songs.csv", index=False)

sns.pairplot(df, diag_kind="hist")
plt.show()
