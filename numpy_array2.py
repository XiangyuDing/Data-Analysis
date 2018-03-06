import numpy as np

A = np.arange(2, 14).reshape((3, 4))

print(A)
print(A.dot(A.T)) # transpose of matrix A
print(np.clip(A, 5, 9)) # set elements <= 5 --> 5 and >= 9 --> 9
print(np.mean(A, axis = 0)) # column mean
print(np.mean(A, axis = 1)) # row mean
print(A[2]) # print row 2
print(A[1][1]) # print row 1 col 1
print(A[1, 1:3]) # print row 1 col 1 and 2

# for loop to print every row
for row in A:
    print(row)
# for loop to print every column
for column in A.T:
    print(column)
print(A.flatten()) # transform A to one row matrix
# transform A to one row matrix, then print every elements
for item in A.flat:
    print(item)
