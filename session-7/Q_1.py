"""Given a CSV file containing Zomato restaurant ratings, use pandas to detect outliers in the 'user_rating' column using the IQR method and print the indices of the detected outliers.
"""

import pandas as pd

df = pd.read_csv(r"C:\Users\Om\Downloads\zomato_ratings_with_outliers.csv")
df = pd.DataFrame(df)
# print(df.describe)


        #calculating Q1 and Q3
Q1 = df.rating_count.quantile(0.25)
Q3 = df.rating_count.quantile(0.75)
print("Q1 :",Q1)
print("Q3: ",Q3)

IQR = Q3-Q1
print("IQR = ", IQR)

upper_limits =  Q3 +  1.5*IQR
lower_limits =  Q1 -  1.5*IQR

print("lower_limits: ", lower_limits)
print("upper_limits", upper_limits)



outliers = df[(df.rating_count < lower_limits)]
outliers = df[(df.rating_count > upper_limits)]

print("outlier columns : ", outliers.index.tolist())





