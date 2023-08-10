import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the coordinates of the points A, B, C, and D
A = (-1, -1, -1)
B = (1, 1, -1)
C = (-1, 1, 1)
D = (1, -1, 1)

# Extract coordinates for plotting ropes
rope_x = [A[0], B[0], C[0], D[0], A[0]]
rope_y = [A[1], B[1], C[1], D[1], A[1]]
rope_z = [A[2], B[2], C[2], D[2], A[2]]

# Create a meshgrid for plotting the solution surface
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
Z = np.full_like(X, -1)  # Constant value -1 for the solution surface

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the solution surface
ax.plot_surface(X, Y, Z, cmap='viridis', antialiased=False)

# Plot the ropes
ax.plot(rope_x, rope_y, rope_z, marker='o', color='red')

# Set labels for axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set title
ax.set_title('Square Sun Sail Solution and Ropes in 3D')

plt.show()


