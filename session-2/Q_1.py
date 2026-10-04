"""Create a 2D NumPy array representing the ratings (out of 5) given by 4 users to 5 different food items on Zomato. Use slicing to extract the ratings given by the second and third users only."""
import numpy as np
ratings = np.array([
    [4, 5, 3, 4, 2],  # User 1
    [5, 4, 4, 3, 5],  # User 2
    [3, 5, 4, 5, 4],  # User 3
    [4, 3, 5, 4, 5]   # User 4
])

extract_users = ratings[1:3] 
for i , customer in enumerate(extract_users,start= 1):
    print(f"{i}st customer ratings:", customer)
    