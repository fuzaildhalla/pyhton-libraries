"""Create a NumPy array of shape (2, 6) representing the number of orders placed on Swiggy in two cities over 6 days. Reshape it to (3, 4), flatten it, split it into two equal parts, and then stack both parts vertically."""


import numpy as np

shape = np.arange(1,13).reshape(2,6)
print(shape)
reshape = shape.reshape(3,4)
flatten = reshape.flatten()
print(" flatten array : " , flatten)

first_half, second_half = np.split(flatten,2)

print("first_half :  ",first_half)
print("second_half:  ",second_half )

