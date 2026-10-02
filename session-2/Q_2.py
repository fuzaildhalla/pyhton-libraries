"""Given a NumPy array of daily steps tracked for 10 days, use boolean indexing to select only the days where the steps were greater than 8000.<br><br><em><strong>Hint:</strong> Use an array like steps = np.array([7500, 8200, 9000, ...]) and apply a boolean condition.</em>"""

import numpy as np

daily_steps = np.arange(7000,16000,1000).reshape(3,3)
print_steps = daily_steps>8000

print(daily_steps[print_steps])