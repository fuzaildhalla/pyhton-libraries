"""Create a relplot using the 'fmri' dataset from Seaborn to visualize how the signal changes over time for different event types.
"""



import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("fmri")

sns.relplot(
    data=df,
    x="timepoint",
    y="signal",
    hue="event",
    kind="line"
)

plt.title("FMRI Signal Over Time by Event Type")
plt.show()
