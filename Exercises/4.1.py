import numpy as np
import matplotlib.pyplot as plt

# Grid and discretization parameters
N = 1000
dx = 1.0 / (N - 1)
dt = 0.05
dy = 0.5

# Tridiagonal matrix A
A = np.zeros((N, N))
for i in range(1, N - 1):
    A[i, i-1] = -dt / dx**2
    A[i, i] = 1 + 2 * dt / dx**2
    A[i, i+1] = -dt / dx**2

# Boundary conditions
A[0, 0] = 1
A[-1, -1] = 1 + dt / dx**2
A[-1, -2] = -dt / dx**2

# Initial condition
f_t = np.exp(-5 * np.linspace(0, 1, N))

# Time evolution and plotting
times_to_plot = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
current_time = 0.0
x_values = np.linspace(0, 1, N)

plt.figure(figsize=(10, 6))
for _ in range(int(3/dt) + 1):  # loop until t = 3
    if current_time in times_to_plot:
        plt.plot(x_values, f_t, label=f't = {current_time}')
    b = f_t.copy()
    b[0] = 1  # Dirichlet boundary condition on the left
    f_t = np.linalg.solve(A, b)
    current_time += dy

plt.xlabel('x')
plt.ylabel('f(x, t)')
plt.title('Heat equation evolution')
plt.legend()
plt.grid(True)
plt.show()


