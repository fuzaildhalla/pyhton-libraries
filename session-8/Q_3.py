"""3.
Create a DataFrame with mock data for Spotify playlists, including playlist names and creator usernames, where some rows are exact duplicates. Use drop_duplicates() to remove duplicate playlists and print the cleaned DataFrame."""

import pandas as pd

data = {
    "playlist_name": [
        "Chill Vibes",
        "Workout Hits",
        "Late Night Drive",
        "Chill Vibes",
        "Focus Music",
        "Workout Hits",
        "Party Anthems",
        "Late Night Drive"
    ],
    "creator_username": [
        "alex_music",
        "john_beats",
        "sarah_tunes",
        "alex_music",
        "emma_sounds",
        "john_beats",
        "mike_mix",
        "sarah_tunes"
    ]
}

data = pd.DataFrame(data)
# print(data)

print("cleaned data : " ,data.drop_duplicates())