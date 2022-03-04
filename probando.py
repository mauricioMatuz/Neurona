import numpy as np

mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat)

mat = np.insert(mat, 0, (0, 0, 0), axis=1)

print(mat, "<-agrego")
