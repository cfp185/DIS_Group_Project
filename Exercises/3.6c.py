import numpy as np
import matplotlib.pyplot as plt

# Define parameters
D_values = [15, 0.5]  # Different diffusion coefficients
#D_values = [2, 0.5]  # Different diffusion coefficients
D_values = [15, 2]  # Different diffusion coefficients

# Define the advection velocity function v(x)
def v(x):
    return -np.sin(x) / (1 + x**2)  # Bounded advection velocity

# Define the spatial domain and grid points
L = 25
N = 1000
dx = L / (N - 1)
x = np.linspace(0, L, N)

# Define the time step and total time
dt = 0.001
total_time = 1

# Initialize the plot
plt.figure()

# Plot the solutions for different D values
for D in D_values:
    # Initialize the solution array
    f = np.zeros(N)
    f[0] = 1
    f[N - 1] = 0

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

    # Normalize the function for plotting
    f_normalized = (f - np.min(f)) / (np.max(f) - np.min(f))
    plt.plot(x, f_normalized, '--',label=f'D = {D}')

# Customize the plot
plt.xlabel('x')
plt.ylabel('Normalized f(x)')
plt.title('Comparison of Diffusion-Advection Solutions for Different D Values')
plt.legend()
plt.grid(True)
plt.show()

