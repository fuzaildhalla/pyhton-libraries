"""2.
Given a list of Flipkart product reviews with some duplicate entries, use value_counts() in pandas to identify which review texts are repeated most often and display the top 3 most common duplicate reviews"""


import pandas as pd


df = pd.read_csv(r"C:\Users\Om\Downloads\flipkart_product_reviews_duplicates (1).csv")

df = df.review_text.value_counts()
print(df.head(3))