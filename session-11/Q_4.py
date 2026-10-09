"""Plot the number of tickets sold for five recent Bollywood movies (categorical) versus their IMDB ratings (numeric) using a scatter plot. Add annotations to display the movie names above each point.
"""


import matplotlib.pyplot as plt

movies = ["Jawan", "Pathaan", "Animal", "Dunki", "Stree 2"]
tickets = [30, 28, 25, 12, 20]  # Millions
ratings = [6.9, 5.8, 6.1, 6.5, 7.0]

plt.scatter(tickets, ratings, color="purple")

for movie, x, y in zip(movies, tickets, ratings):
    plt.annotate(movie, (x, y), xytext=(0, 5),
                 textcoords="offset points", ha="center")

plt.xlabel("Tickets Sold (Millions)")
plt.ylabel("IMDb Rating")
plt.title("Movie Tickets vs IMDb Ratings")
plt.tight_layout()
plt.show()
