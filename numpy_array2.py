import numpy as np

A = np.arange(2, 14).reshape((3, 4))

print(A)
print(A.dot(A.T)) # transpose of matrix A
print(np.clip(A, 5, 9)) # set elements <= 5 --> 5 and >= 9 --> 9
print(np.mean(A, axis = 0)) # column mean
print(np.mean(A, axis = 1)) # row mean
