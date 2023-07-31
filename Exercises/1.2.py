import numpy as np
from scipy import linalg

# a.) solve the equationsystem
#define coefficient matrix A and the constant vector b
a_1 = np.array([[1, 3, -8],[3, 0, -1],[0, 10, 3]])
b_1 = np.array([1, 0, 7])
x_1 = linalg.solve(a_1, b_1) #solve for x
x_1

# b.) Sample a 1000 × 1000 random matrix A and a random vector 𝒃
a_2 = np.random.randn(1000, 1000)
b_2 = np.random.randn(1000)
x_2 = linalg.solve(a_2, b_2) #solve for x
x_2

# c.) 
linalg.inv(a)