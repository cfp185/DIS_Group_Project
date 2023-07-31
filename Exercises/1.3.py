import numpy as np

# Exercise a)
def construct_matrixA(N):
    A = np.zeros((N, N))
    for i in range(N):
        if i > 0:
            A[i][i-1] = -0.5
        if i < N - 1:
            A[i][i+1] = 0.5
    return A

# Exercise b)
def construct_matrixB(N):
    B = np.zeros((N, N))
    for i in range(N):
        B[i][i] = -2
        if i > 0:
            B[i][i-1] = 1
        if i < N - 1:
            B[i][i+1] = 1
    return B

# Set N to 10 for a 10x10 matrix
N = 10
matrixA = construct_matrixA(N)
matrixB = construct_matrixB(N)

# Exercise c)
matrixB[0][0] = 1
for j in range(1, len(matrixB[0])):
    matrixB[0][j] = 0

matrixB[N-1][N-1] = 1
matrixB[N-1][N-2] = 0

print("Matrix A:")
print(matrixA)

# Print the matrix
print("Matrix B:")
print(matrixB)

