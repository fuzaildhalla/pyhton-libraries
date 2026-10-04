"""2.
Find a small JSON dataset of trending songs (for example, from Spotify's API samples or any open JSON file), and use pd.read_json() to import it into a DataFrame. Display the DataFrame's column names and data types using df.info()."""

import pandas as pd
json_load = pd.read_json(r"C:\Users\Om\Downloads\spotify_trending_songs.json")
pd.DataFrame(json_load)
# print(json_load)
json_load.info()
print(json_load)