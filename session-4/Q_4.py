"""4.
Download a large Excel file (at least 10,000 rows) of Flipkart product listings. Use pd.read_excel() with the chunksize parameter to read the file in chunks of 2000 rows, and print the number of rows in each chunk as you iterate."""

import pandas as pd
import  openpyxl
flipkart_product_listing = pd.read_excel(r"C:\Users\Om\Downloads\flipkart_products_10k.xlsx", nrows=2000 )

print(flipkart_product_listing)