"""Use jointplot on the 'penguins' dataset to visualize the relationship between bill_length_mm and flipper_length_mm, and fit a regression line on the scatter plot.<br><br><em><strong>Hint:</strong> Set kind='reg' in jointplot for regression line.</em>
"""



import seaborn as sns
import matplotlib.pyplot as plt

# Load penguins dataset
df = sns.load_dataset("penguins")

sns.jointplot(
    data=df,
    x="bill_length_mm",
    y="flipper_length_mm",
    kind="reg",
    color="purple"
)

plt.show()
