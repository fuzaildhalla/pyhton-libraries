"""5.
You have a DataFrame column for payment status from a Paytm-like app with mixed values: 'Yes', 'yes', 'Y', 'No', 'no', 'N', and some with extra spaces. Write code to unify this column so all paid statuses become 1 and all unpaid statuses become 0, trimming whitespace and fixing capitalization where needed.<br><br><em><strong>Hint:</strong> Use str.strip(), str.lower(), and map/replace methods in pandas.</em>"""


import pandas as pd

data = {
    "payment_status": [
        "Yes",
        "yes",
        "Y",
        "No",
        "no",
        "N",
        " Yes ",
        "  no",
        "Y ",
        " N ",
        "YES",
        "NO"
    ]
}

df = pd.DataFrame(data)

# print(df)

df = ((df["payment_status"].str.strip()).str.lower().map({"yes": 1, "no": 0, "y": 1, "n": 0}))

print(df)

