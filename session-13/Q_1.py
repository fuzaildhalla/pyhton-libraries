"""Load the 'tips' dataset from Seaborn and create a pairplot to quickly visualize relationships between all numeric variables.
"""



import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
df = sns.load_dataset("tips")

# Create pairplot for numeric columns
sns.pairplot(df)

plt.show()
