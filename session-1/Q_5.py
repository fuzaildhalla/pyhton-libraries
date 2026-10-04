"""Convert a Python list of cricket scores [45, 67, 120, 89, 54] to a NumPy array, then use the .itemsize attribute to print how many bytes each score takes in memory.<br><br><em><strong>Hint:</strong> Use np.array() for conversion and .itemsize for memory size.</em>"""

cricket_scores = [45, 67, 120, 89, 54]

import numpy as np
new_array = np.array(cricket_scores)
print(type(new_array), new_array)

print(new_array.itemsize)