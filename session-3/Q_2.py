"""2.
Simulate a Spotify-like 'Recommended Songs' feature: Given two 3x3 matrices representing user-song interaction scores (user preferences and song popularity), use dot() and matmul() to compute the final recommendation matrix and explain the difference between the two results."""
import numpy as np

user_preferences = np.array([[5,4,3],[1,2,3],[4,3,1]])

song_popularity = np.array([[1,2,3],[5,4,3],[5,1,2]])

print(np.dot(user_preferences,song_popularity))
