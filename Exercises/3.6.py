import numpy as np
import matplotlib.pyplot as plt

# Define parameters
D = 2

# Define the advection velocity function v(x)
def v(x):
    return -np.sin(x) / (1 + x**2)  # Bounded advection velocity

# Define the spatial domain and grid points
L = 25                      # Length of spatial domain
N = 1000                    # #Grid points
dx = L / (N - 1)            # Grid spacing
x = np.linspace(0, L, N)

# Initialize the solution array
f = np.zeros(N)

# Set initial and boundary conditions
f[0] = 1
f[L] = 0

# Define the time step and total time
dt = 0.001
total_time = 1

# Time stepping loop with Crank-Nicolson method
num_time_steps = int(total_time / dt)
for t in range(num_time_steps):
    f_new = np.copy(f)

    for i in range(1, N - 1):
        alpha = 0.5 * D * dt / dx**2
        beta = 0.5 * v(x[i]) * dt / dx
        
        A = -alpha + beta
        B = 1 + 2 * alpha
        C = alpha - beta
        
        f_new[i] = (f[i + 1] * A + f[i] * B + f[i - 1] * C) / (A + B + C)

    f = np.copy(f_new)

# Calculate analytical solution for pure diffusion
t_initial = 0.001
t_final = t_initial + total_time
analytical_solution = np.exp(-x**2 / (4 * D * t_final))

# Plot the numerical and analytical solutions
plt.plot(x, f, label='Numerical Solution')
plt.plot(x, analytical_solution, '--', label='Analytical Solution (Diffusion)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Solution of Diffusion-Advection Equation (D=2)')
plt.legend()
plt.grid(True)
plt.show()


