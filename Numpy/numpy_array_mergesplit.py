import numpy as np

# Merge ops
##A = np.array([1, 1, 1])
##B = np.array([2, 2, 2])
##C = np.vstack((A, B)) # vertical stack
##D = np.hstack((A, B)) # horizontal stack
##AT = A[:, np.newaxis]
##BT = B[:, np.newaxis]
##E = np.hstack((AT, BT))
##F = np.concatenate((A, B, B, A), axis = 0) # multiple stack
##print(F)

# Split ops
##A = np.arange(12).reshape((3, 4))
##print(A)
##
##print(np.array_split(A, 3, axis = 1))
##print(np.vsplit(A, 3))
##print(np.hsplit(A, 2))

# Copy ops
A = np.arange(4)
B = A # copy
C = A
D = B # still copy B copy A
A[0] = 11
D[1:3] = [22, 33] # any op changes A,B,C,D
print(B)
print(B is A)
print(D is A)
b = A.copy() # deep copy
A[3] = 44 # b won't change
print(b)
