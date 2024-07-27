import numpy as np
import matplotlib.pyplot as plt


v = np.array([2., 2., 4.])

u1 = np.array([1., 0, 0])
u2 = np.array([0, 1., 0])
u3 = np.array([0, 0, 1.])

e0 = v.dot(u1)
e1 = v.dot(u2)
e2 = v.dot(u3)

print(e0)

print(e1)

print(e2)