import numpy as np

##a = np.array([ [1, 1],
##                      [0, 1] ])
##b = np.arange(4).reshape((2,2))
##print(a)
##print(b)
##
##c = a * b
##c_dot = np.dot(a, b)
##c_dot2 = a.dot(b)
##print(c)
##print(c_dot)
##print(c_dot2)

s = np.random.random((2, 4))
print(s)

print(np.sum(s, axis = 1))
print(np.min(s, axis = 0))
print(np.max(s, axis = 0))
