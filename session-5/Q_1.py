"""1.
Connect to a MySQL or PostgreSQL database using SQLAlchemy and pandas, then use pd.read_sql() to load the entire 'restaurants' table (imagine Zomato backend) into a DataFrame and display the first 5 rows."""

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+pymysql://root:fuzail.1712@localhost:3306/restaurent_Data"
)
df = pd.read_sql("select * from restaurants", engine)
print(df.head())
