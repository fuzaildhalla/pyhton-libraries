"""3.
Read a JSON dataset from the URL https://jsonplaceholder.typicode.com/users using pandas, convert it into a DataFrame, and print the usernames column.<br><br><em><strong>Hint:</strong> Use pd.read_json() directly with the URL.</em>"""

import pandas as pd

Json_data = pd.read_json("https://jsonplaceholder.typicode.com/users")
df =(pd.DataFrame(Json_data))
print(df["username"])