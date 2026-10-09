"""1.
Given a list of delivery timestamps as strings (e.g., ['2024-06-01 14:30', '2024-06-02 09:15', '2024-06-03 20:45']), use pandas and pd.to_datetime() to convert them into datetime objects and print the result."""


import pandas as pd

df = pd.DataFrame({
    "transaction_date": [
        "2026-10-01",
        "2026-10-05",
        "2026-10-08"
    ]
})

df = pd.to_datetime(df["transaction_date"])
print(df)