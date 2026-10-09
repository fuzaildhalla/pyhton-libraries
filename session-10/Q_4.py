"""Create a histogram of the durations (in minutes) of your last 20 Spotify listening sessions using Matplotlib. Set the number of bins to 5 and customize the color of the bars.
"""



import matplotlib.pyplot as plt

durations = [
    15, 25, 30, 45, 20,
    35, 60, 40, 50, 25,
    70, 55, 30, 45, 80,
    20, 65, 35, 50, 90
]

plt.hist(durations, bins=5, color="mediumseagreen", edgecolor="black")

plt.title("Spotify Listening Session Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Sessions")

plt.show()
