"""2.
Simulate a Spotify-like 'Recommended Songs' feature: Given two 3x3 matrices representing user-song interaction scores (user preferences and song popularity), use dot() and matmul() to compute the final recommendation matrix and explain the difference between the two results."""

import numpy as np

user_preferences = np.array([[1,2,3],
                            [4,5,6],
                            [7,8,9]
                             ])

song_popularity = np.array([[9,8,7],
                            [6,5,4],
                            [3,2,1]
                            ])

print(np.dot(user_preferences,song_popularity))

print(np.matmul(user_preferences,song_popularity))

"""
matmul() is specifically for matrix multiplication, while dot() is a more general dot-product operation whose behavior depends on the dimensions of the arrays.
"""