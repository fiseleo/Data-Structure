# Two Dimensional Arrays # (Matrices) Operations  Numpy Version
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 4], [3, 1]])

C = A + B
print("A + B =", C)
C = np.dot(A, B)
print("A * B =", C)
C = A-B
print("A - B =", C)