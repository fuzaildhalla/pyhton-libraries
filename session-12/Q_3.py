"""Simulate IPL match scores for 8 teams and use a violinplot to compare the run distributions per team. Style your plot using the 'darkgrid' Seaborn theme.
"""


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import random

sns.set_theme(style="darkgrid")

teams = ["CSK", "MI", "RCB", "KKR", "SRH", "DC", "PBKS", "RR"]

data = {
    "Team": [team for team in teams for _ in range(20)],
    "Runs": [random.randint(100, 220) for _ in range(160)]
}

df = pd.DataFrame(data)

sns.violinplot(data=df, x="Team", y="Runs", palette="Set2", hue="Team", legend=False)

plt.title("IPL Run Distribution by Team")
plt.xlabel("IPL Team")
plt.ylabel("Runs Scored")

plt.show()
