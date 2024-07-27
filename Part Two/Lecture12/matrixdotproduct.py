import numpy as np

#1
n = np.array([[6,-9,1], [4,24,8]])
s = 2
print('First Solution :\n', s*n)


#2
n2 = np.array([[1,0],[0,1]])
dotOfn2n = n2.dot(n)
print('Second Solution :\n', dotOfn2n)

#3
n3 = np.array([[4,3],[3,2]])
n4 = np.array([[-2,3],[3,-4]])
dotn3n4 = n3.dot(n4)
print("Third solution: \n", dotn3n4)