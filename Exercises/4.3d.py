import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the points A, B, C, and D
A = (-1, -1, -1)
B = (1, 1, -1)
C = (-1, 1, 1)
D = (1, -1, 1)

# Create a meshgrid for plotting the solution surface
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)

# Initialize the solution array
Z = np.zeros((100, 100))
Z = np.full_like(X, -1)  # Constant value -1 for the solution surface

# Boundary conditions
Z[0,:] = np.linspace(-1, 1, 100)  # Bottom
Z[-1,:] = np.linspace(1, -1, 100) # Top
Z[:,0] = np.linspace(-1, 1, 100)  # Left
Z[:,-1] = np.linspace(1, -1, 100) # Right

tolerance = 1e-4
error = 1

while error > tolerance:
    Z_old = Z.copy()
    for i in range(1, 100-1):
        for j in range(1, 100-1):
            Z[i,j] = 0.25 * (Z_old[i+1, j] + Z_old[i-1, j] + Z_old[i, j+1] + Z_old[i, j-1])

    error = np.max(np.abs(Z - Z_old))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot the solution surface
ax.plot_surface(X, Y, Z, cmap='viridis', antialiased=False)

# Plotting the ropes again on top of the surface
ax.plot([A[0], C[0]], [A[1], C[1]], [A[2], C[2]], label='_nolegend_', color='r')  # Use _nolegend_ to suppress label for ropes
ax.plot([A[0], D[0]], [A[1], D[1]], [A[2], D[2]], label='_nolegend_', color='r')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], label='_nolegend_', color='r')
ax.plot([B[0], D[0]], [B[1], D[1]], [B[2], D[2]], label='_nolegend_', color='r')

# Setting the labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set title
ax.set_title('Square Sun Sail Solution and Ropes in 3D')

plt.show()

