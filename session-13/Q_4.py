"""Pick any categorical column from the 'titanic' dataset (like 'class' or 'sex') and use catplot to display the survival rate for each group with confidence intervals.
"""



import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

sns.catplot(
    data=df,
    x="class",
    y="survived",
    kind="point",
    errorbar=("ci", 95),
    color="teal"
)

plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.show()
