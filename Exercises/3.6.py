import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

# Define parameters
D = [2]

# Define the advection velocity function v(x)
def v(x):
    return -np.sin(x)   # Bounded advection velocity

# Define the spatial domain and grid points
L = 25                      # Length of spatial domain
N = 1000                    # #Grid points
x = np.linspace(0, L, N)
dx = x[1] - x[0]            # Grid spacing

# Initialize the solution array
f = np.zeros(N)

# Set initial condition
f[0] = 1

# Define the time step and total time
dt = 0.001
total_time = 1

# Here we get the matrices to solve the problem
D1 = np.diag(np.ones(N - 1), 1) - np.diag(np.ones(N), 0)
D1[-1, -1] = 0
D1 = D1 / dx

D2 = np.diag(np.ones(N - 1), 1) - 2 * np.diag(np.ones(N), 0) + np.diag(np.ones(N - 1), -1)
D2 /= dx**2

# Construct A_matrix
def A_matrix(D, v): #this will create the A matrix that will essentially give the f
    return D * D2 - np.dot(D1, np.diag(v))

plt.figure(figsize=(12, 8))

for i, D in enumerate(D):
    vel = v(x)
    A_D = A_matrix(D, vel)

     # Here we put the boundary conditions
    A_D[0, 0] = 1
    A_D[0, 1] = 0
    A_D[-1, -1] = 1
    A_D[-1, -2] = 0

    # Solve the system
    right = np.zeros(N)
    right[0] = 1

    De = linalg.solve(A_D, right)

    plt.plot(x, De, label=f'D={D}')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Diffusion-Advection Equation Solutions for Different D Values')
plt.legend()
plt.grid()
plt.show()





