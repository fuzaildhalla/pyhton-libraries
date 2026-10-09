"""
Use Sweetviz to create a comparison report between two CSV files: one containing Zomato restaurant data for Mumbai and another for Delhi. Briefly describe one key difference you spot in the visual report.<br><br><em><strong>Hint:</strong> Use analyze() for single file and compare() for two datasets.</em>
"""




import pandas as pd
import sweetviz as sv

mumbai = pd.read_csv("zomato_mumbai.csv")
delhi = pd.read_csv("zomato_delhi.csv")

report = sv.compare(
    [mumbai, "Mumbai"],
    [delhi, "Delhi"]
)

report.show_html("zomato_comparison_report.html")

print("Comparison report generated!")
