"""3.
You have a TSV (tab-separated values) file containing Zomato restaurant data. Use pd.read_csv() with the correct separator to load the data, and then use df.describe(include='all') to generate summary statistics.<br><br><em><strong>Hint:</strong> The separator for TSV files is '\t'.</em>
"""

import pandas as pd

zometo_res_ratings = pd.read_csv(r"C:\Users\Om\Downloads\zomato_restaurant_data.tsv", sep="\t")

zometo_res_ratings.describe(include='all')
print(zometo_res_ratings)