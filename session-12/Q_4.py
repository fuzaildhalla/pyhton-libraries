"""Create a countplot that displays the number of songs per genre from a list of 40 Spotify tracks, with at least 4 different genres represented.<br><br><em><strong>Hint:</strong> Use a Python list or pandas DataFrame to store your data, then plot with Seaborn.</em>
"""


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

genres = [
    "Pop", "Rock", "Hip-Hop", "Jazz", "Pop",
    "Rock", "Pop", "Hip-Hop", "Jazz", "Pop",
    "Rock", "Hip-Hop", "Pop", "Jazz", "Rock",
    "Pop", "Hip-Hop", "Rock", "Jazz", "Pop",
    "Rock", "Pop", "Hip-Hop", "Jazz", "Rock",
    "Pop", "Hip-Hop", "Pop", "Rock", "Jazz",
    "Pop", "Rock", "Hip-Hop", "Pop", "Jazz",
    "Rock", "Pop", "Hip-Hop", "Jazz", "Pop"
]

df = pd.DataFrame({"Genre": genres})

sns.countplot(data=df, x="Genre", hue="Genre", legend=False, palette="Set2")

plt.title("Number of Spotify Songs per Genre")
plt.xlabel("Music Genre")
plt.ylabel("Number of Songs")

plt.show()
