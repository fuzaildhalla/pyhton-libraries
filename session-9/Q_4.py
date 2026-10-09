"""Suppose you have a DataFrame of Instagram posts with a 'posted_at' column in UTC. Convert these timestamps to 'Asia/Kolkata' timezone and display the first 5 converted times.
"""


import pandas as pd

df = pd.DataFrame({
    "posted_at": [
        "2026-10-01 08:30:00",
        "2026-10-02 12:45:00",
        "2026-10-03 16:20:00",
        "2026-10-04 05:15:00",
        "2026-10-05 20:10:00",
        "2026-10-06 09:00:00"
    ]
})

df["posted_at"] = pd.to_datetime(df["posted_at"], utc=True)

df["posted_at"] = df["posted_at"].dt.tz_convert("Asia/Kolkata")

print(df.head())
