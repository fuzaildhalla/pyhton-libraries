"""
Given a 4x4 NumPy matrix representing the pixel brightness of a small Instagram image, use transpose (T) to rotate the image and then calculate the mean, median, standard deviation, and variance of the pixel values.
"""
import numpy as np

instagram_image = np.arange(1,17).reshape(4,4)
print(instagram_image)

pixel = np.transpose(instagram_image)
print(pixel)

print("mean: ",np.mean(pixel))
print("median: ",np.median(pixel))
print("STD: ",np.std(pixel))
print("variance: ",np.var(pixel))
