"""5.
Fix the following code snippet where the 'is_premium' column in a Spotify user DataFrame is a mix of boolean, string, and integer types. Convert the entire column to boolean type, treating 'True', 1, and 'yes' as True, and everything else as False."""


import pandas as pd

df = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 5, 6, 7],
    "is_premium": [True, "True", 1, "yes", "False", 0, "no"]
})

df["is_premium"] = df["is_premium"].apply(
    lambda x: str(x).lower() in ["true", "1", "yes"]
)

print(df)
print(df.dtypes)
