"""For a BookMyShow movie dataset (with 'genre' and 'box_office_collection' columns), use groupby analysis to find the average box office collection for each genre and display the results as a sorted table.
"""



import pandas as pd

data = {
    "movie": [
        "Movie A", "Movie B", "Movie C", "Movie D",
        "Movie E", "Movie F", "Movie G", "Movie H"
    ],
    "genre": [
        "Action", "Comedy", "Action", "Drama",
        "Comedy", "Drama", "Action", "Comedy"
    ],
    "box_office_collection": [
        500, 200, 700, 300, 250, 400, 600, 150
    ]
}

df = pd.DataFrame(data)

print(df)




result = df.groupby("genre")["box_office_collection"].mean()

result = result.sort_values(ascending=False)

print(result)
