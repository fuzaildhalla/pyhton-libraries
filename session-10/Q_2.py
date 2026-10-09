"""2.
Using Matplotlib, create a scatter plot of 10 restaurants from your city with their Zomato ratings on the x-axis and average meal price on the y-axis. Add axis labels and a title to the chart."""



import matplotlib.pyplot as plt

restaurants = [
    "Spice Garden", "Urban Tadka", "Pizza Corner",
    "Royal Biryani", "Green Leaf Cafe", "Mumbai Masala",
    "Cafe Aroma", "Desi Kitchen", "The Burger House",
    "Taste of India"
]

ratings = [4.3, 4.1, 3.8, 4.5, 4.2, 3.9, 4.0, 4.4, 3.7, 4.1]

average_meal_price = [
    500, 450, 350, 600, 300, 400, 250, 550, 280, 480
]

plt.figure(figsize=(9, 6))
plt.scatter(ratings, average_meal_price)

plt.title("Zomato Ratings vs Average Meal Price in Ahmedabad")
plt.xlabel("Zomato Rating")
plt.ylabel("Average Meal Price (₹)")

plt.grid(True, alpha=0.3)

plt.savefig("restaurant_ratings_scatter.png", dpi=150)

plt.show()
