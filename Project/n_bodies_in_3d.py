import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def getAcc(pos, mass, G, softening):
    N = pos.shape[0]
    a = np.zeros((N, 3))

    for i in range(N):
        for j in range(N):
            if i != j:  # Avoid self-interaction
                dx = pos[j, 0] - pos[i, 0]
                dy = pos[j, 1] - pos[i, 1]
                dz = pos[j, 2] - pos[i, 2]
                inv_r3 = (dx**2 + dy**2 + dz**2 + softening**2)**(-1.5)
                a[i, 0] += G * (dx * inv_r3) * mass[j]
                a[i, 1] += G * (dy * inv_r3) * mass[j]
                a[i, 2] += G * (dz * inv_r3) * mass[j]

    return a

# Number of particles
N = 10

# Generate random initial positions and masses
np.random.seed(0)
pos = np.random.randn(N, 3)
mass = np.random.rand(N)
G = 1.0
softening = 0.1

# Simulation parameters
time_steps = 100
dt = 0.01

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Scatter plot for initial positions
scatter = ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2], c="b", marker="o")

# Set plot labels and title
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Particle Motion Simulation")

# Animation loop
for step in range(time_steps):
    a = getAcc(pos, mass, G, softening)
    pos += a * dt

    # Update scatter plot data
    scatter._offsets3d = (pos[:, 0], pos[:, 1], pos[:, 2])

    plt.pause(0.05)

plt.show()

