"""Given a NumPy array of user ratings (can be negative, zero, or positive) for songs on Spotify, use boolean masking to set all negative ratings to zero, keeping other ratings unchanged."""
import numpy as np
user_ratings = np.array([3,2,-2,-4,5,6,-7,8,10,-10])
negative_ratings = user_ratings < 0
new_ratings = user_ratings[negative_ratings] = 0
print(user_ratings)

