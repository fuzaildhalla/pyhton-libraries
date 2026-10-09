"""Pick any one auto-EDA tool (pandas-profiling, Sweetviz, or D-Tale) and use ChatGPT or Copilot to generate a code snippet that loads a Swiggy food order CSV and produces a summary report. Run the code and attach the generated report or a screenshot as proof.
"""


import pandas as pd
import sweetviz as sv

# Load the Swiggy food-order CSV
df = pd.read_csv("swiggy_food_orders_sample.csv")

# Generate an interactive auto-EDA report
report = sv.analyze(df)
report.show_html("swiggy_sweetviz_report.html", open_browser=True)