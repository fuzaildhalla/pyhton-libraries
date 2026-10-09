"""4.
Suppose you have a DataFrame of Instagram usernames where some entries have typos (like 'insta_queen', 'insta-queen', 'instaqueen'). Use the replace() function to standardize all these variants to 'instaqueen'."""

import pandas as pd

data = {
    "username": [
        "fuzail_dhalla",
        "fuzail_dhala",   
        "john_doe",
        "john_d0e",         
        "sarah_music",
        "sarah_musik",      
        "alex_travels",
        "alex_travels"
    ]
}

df = pd.DataFrame(data)

# print(df)


data = df["username"].replace({
    "fuzail_dhala" : "fuzail_dhalla",
    "john_d0e" : "john_doe",
    "sarah_musik" : "sarah_music",
    "alex_travels" : "alex_travels"
})

print(data.drop_duplicates())