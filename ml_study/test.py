import numpy as np

np_array_1 = np.array([[1, 2]])
np_array_2 = np.array([[1, 2], [3, -4]])
np_array_3 = np.array([[0, 1, 0], [2, 0, 3]])
print(np.dot(np.dot(np_array_1, np_array_2), np_array_3))
