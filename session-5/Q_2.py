"""Use pd.read_sql_query() to fetch only the 'name' and 'rating' columns from a 'movies' table (think BookMyShow-like data) where rating is above 8, and print the resulting DataFrame.<br><br><em><strong>Hint:</strong> Write a custom SQL SELECT query as the first argument to pd.read_sql_query().</em>
"""
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+pymysql://root:fuzail.1712@localhost:3306/movies"
)

print(pd.read_sql_query("select name,rating from movies where rating > 8" , engine))

