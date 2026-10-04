"""3.
Create a NumPy array of IPL team scores for 8 matches. Use fancy indexing to select the scores from matches 2, 5, and 7, and print them."""
import numpy as np
ipl_team_scores = np.array([120,200,130,210,140,220,150,230,])

scores = ipl_team_scores[[1,4,7]]
print(scores)