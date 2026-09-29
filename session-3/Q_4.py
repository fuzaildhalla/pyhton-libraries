"""
Take a 3x3 NumPy matrix representing a Zomato restaurant rating correlation grid and use np.linalg.inv(), np.linalg.det(), and np.linalg.eig() to compute its inverse, determinant, and eigenvalues/eigenvectors.<br><br><em><strong>Hint:</strong> If the matrix is not invertible, modify one value and try again.</em>
"""

import numpy as np

zometo_restaurant_ratings = np.array([[5,4,3],[3,2,1],[1,2,3]])
print(zometo_restaurant_ratings)

print(np.linalg.inv(zometo_restaurant_ratings))
print(np.linalg.det(zometo_restaurant_ratings))

values,vectors = np.linalg.eig(zometo_restaurant_ratings)


print("eig values : ",values)
print("vectors values :", vectors)

