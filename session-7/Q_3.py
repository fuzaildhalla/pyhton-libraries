"""3.
Apply winsorization to the 'transaction_amount' column in a Paytm transactions DataFrame to cap all values above the 95th percentile and below the 5th percentile, then display the updated column statistics."""

import pandas as pd

df = pd.DataFrame({
    "transaction_id": range(1, 16),
    "transaction_amount": [
        200, 350, 500, 250, 400,
        600, 300, 450, 700, 550,
        350, 500, 1, 800, 50000
    ]
})

print(df.describe())

upper_limit = (df["transaction_amount"].quantile(0.95))
lower_limit = (df["transaction_amount"].quantile(0.05))


df['transaction_amount'] = (df['transaction_amount'].clip(lower= lower_limit,
upper=upper_limit))

print(df["transaction_amount"].describe)
